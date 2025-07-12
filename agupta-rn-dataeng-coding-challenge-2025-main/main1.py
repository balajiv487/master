from sqlalchemy import create_engine, text
import os
from sqlalchemy.exc import SQLAlchemyError
from pathlib import Path

def create_table(engine):
    table=""" create table if not exists a (
    id integer,
    name Varchar(100));"""

    insert_queries=""" insert into a values(1,'Trishul') """

    with engine.begin() as conn:
        conn.execute(text(table))
        conn.execute(text(insert_queries))
        print("Table created successfully!")

def load_data_from_csv(engine,data_dir='data/ ', full_refresh=False):
    data_dir=Path(data_dir)
    print(f"data_dir:{data_dir}")




if __name__=="__main__":
    DB_USER = os.getenv('POSTGRES_USER')
    print(f"DB_USER :{DB_USER}")
    DB_PASSWORD =os.getenv('POSTGRES_PASSWORD')
    DB_NAME = os.getenv('POSTGRES_DB')
    print(f"DB_NAME:{DB_NAME}")
    DB_HOST = os.getenv('POSTGRES_HOST')
    print(f"DB_HOST:{DB_HOST}")
    DB_PORT = os.getenv('POSTGRES_PORT')
    print(f"DB_PORT:{DB_PORT}")
    SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    try:
        with engine.connect():
            print("Database connection successful!")
            create_table(engine)
            load_data_from_csv(engine, data_dir='data/ ', full_refresh=False)
    except SQLAlchemyError as e:
        print(e)
        raise
