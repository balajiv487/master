import os
from pathlib import Path
from datetime import datetime

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd


def create_diner_table(engine):
    create_table_sql = """
                       CREATE TABLE IF NOT EXISTS diner_activity 
                       ( 
                           diner_activity_key SERIAL PRIMARY KEY,
                           diner_key INTEGER NOT NULL, 
                           diner_name VARCHAR ( 100 ) NOT NULL,
                           diner_state CHAR ( 2 ) NOT NULL,
                           diner_programid INTEGER NOT NULL,
                           last_dined DATE NULL,
                           type2_start_date DATE NULL,
                           type2_end_date DATE,
                           type2_current_flag BOOLEAN,
                           etl_create_date TIMESTAMP,
                           etl_create_user VARCHAR ( 100 ),
                           etl_update_date TIMESTAMP,
                           etl_update_user VARCHAR ( 100 ),
                           source_file VARCHAR ( 255 ) NULL,
                           UNIQUE ( diner_key, type2_start_date ) -- Ensure one version per diner per start date
                           ); """

    with engine.connect() as conn:
        conn.execute(text(create_table_sql))
        conn.commit()
    print("Diner activity table created successfully")


def load_data_from_csv(engine, data_dir='data/initial_full_load', full_refresh=False):
    """Load data from CSV files into the diner_activity table, processing files in date order based on filename.

    Args:
        engine: SQLAlchemy engine
        data_dir: Directory containing CSV files with names like 'diner_data_YYYYMMDD.csv'
        full_refresh: If True, truncates the table before loading data
    """
    data_dir = Path(data_dir)

    # Get list of files to process
    csv_files = list(data_dir.glob('diner_data_*.csv'))

    if not csv_files:
        print(f"No CSV files found in the {data_dir} directory")
        return

    # Handle full refresh for initial load directory
    if full_refresh and 'initial_full_load' in str(data_dir):
        with engine.connect() as conn:
            print("Performing full refresh - truncating diner_activity table")
            conn.execute(text("TRUNCATE TABLE diner_activity RESTART IDENTITY CASCADE"))
            conn.commit()
            print("Successfully truncated diner_activity table")

    # Sort files by date in filename (format: diner_data_YYYYMMDD.csv)
    def get_date_from_filename(filename):
        try:
            # Extract the date part (YYYYMMDD) and convert to datetime
            date_str = filename.stem.split('_')[-1]
            return datetime.strptime(date_str, '%Y%m%d').date()
        except (ValueError, IndexError):
            # If date can't be parsed, return a very old date so these files come first
            return datetime.min.date()

    # Sort files by date in filename
    csv_files.sort(key=get_date_from_filename)

    print(f"Found {len(csv_files)} CSV files to process in {data_dir}")
    print(f"Processing order: {', '.join(f.name for f in csv_files)}")

    for file_path in csv_files:
        try:
            # Read the CSV file and load into a DataFrame
            df = pd.read_csv(file_path)

            # Add source file information
            df['source_file'] = file_path.name

            # Convert last_dined to datetime if it's not already
            if 'last_dined' in df.columns:
                df['last_dined'] = pd.to_datetime(df['last_dined']).dt.date

            # Get the file date for this batch
            file_date = get_date_from_filename(file_path)

            with engine.connect() as conn:

                # Now that data is in the dataframe, and DB connection established as conn, Design aImplement type2 step by step logic here

        except Exception as e:
            print(f"Error processing {file_path.name}: {str(e)}")

    print(f"\nProcessing complete.")


# Main execution
if __name__ == "__main__":
    # Database connection setup
    DB_USER = os.getenv('POSTGRES_USER')
    DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    DB_NAME = os.getenv('POSTGRES_DB')
    DB_HOST = os.getenv('POSTGRES_HOST')
    DB_PORT = os.getenv('POSTGRES_PORT')

    SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    try:
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        with engine.connect():
            print("Database connection successful!")

            # Create the table if it doesn't exist
            create_diner_table(engine)

            # Load data from initial full load directory first
            print("\n=== Loading initial full load data ===")
            load_data_from_csv(engine, data_dir='data/initial_full_load', full_refresh=True)

            # Then load data from incremental daily directory
            print("\n=== Loading incremental daily data ===")
            load_data_from_csv(engine, data_dir='data/incr_daily')

    except SQLAlchemyError as err:
        print(f"Database error: {err}")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise