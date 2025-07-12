### RN Data Engineering Coding Challenge


This code repository contains two challenges:
* Part 1: Implement a type 2 Slowly Changing Dimension
* Part 2: Write a sql query that uses a window function and CTE format


### Preconfiguration

* 4 source files will be supplied


* The code will already have:
  * An initial full load file and 3 daily incremental files
    * The full load is the starting point of the table
    * The incremental files capture changes from that day (new/update/no change)
    * **This type 2 SCD does not need to handle deletes**
  * Scripts to import these files in order and extract the date from the file name
  * A local postgres database that will persist the data
  * Connectors and credentials to the local database
  * A full-refresh (truncate) option by default for clean runs on every run (can be disabled by the function call in main)
  * A pre-defined target table configured for Type 2 SCD


When you're code is completed or to test, run your application with:
`docker compose up --build`
* This will build the database AND run the application


### Database Access

You can view the results and run queries using pgadmin while the Docker container is running:

While your application is running, go to http://localhost:5050.

Your pgadmin password can be found in the compose.yaml file

Register the server using the credentials in the .env file




### Requirements and Assumptions for Type 2 SCD

* Provide the logic that implements change tracking in a Type 2 SCD:
  * You are responsible for the step-by-step implementation, transformation and SQL queries that satisfy a type2 scd
  * You can implement it all in main.py, or add modules as you see fit


    * Transform the diner_state into all-caps
    * The diner_key is the natural key
    * The diner_activity_key on the Table (not in the files) is the auto-incremented PK
    * Type2 start date is the file date
    * Type2 end date is null for current version
    * Type2 end date is [filedate]-1 for expired records



* Pandas and sqlalchemy are included in the requirements.txt, additional packages are not needed but feel free to add any others that you would like to use


* Do not worry about tracking deletion of records (a record that does not exist in the incremental file does not mean it was deleted)


* Feel free to ask any clarifying questions


### Code Challenge Part 2 - SQL CTE & Window Function

* Build the query from the type2 SCD table populated by Part 1 (diner_activity)
* See the file sql_cte_challenge for instructions
* Run the query in your local pgadmin (instructions above in Database Access)
* Copy the query into the sql_cte_challenge to submit