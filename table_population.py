import psycopg2
from psycopg2 import Error
from sqlalchemy import create_engine, text
import pandas as pd
import numpy as np
from pathlib import Path


def main():
    DATADIR = str(Path(__file__).parent.parent) # for relative path 
    print("Data directory: ", DATADIR)

    # *********************************************
    # Credentials to connect to Postgres database *
    # *********************************************
    database= 'FILL_IN_BEFORE_USE' 
    user= 'FILL_IN_BEFORE_USE'       
    password= 'FILL_IN_BEFORE_USE' 
    host= 'FILL_IN_BEFORE_USE'
    port=  'FILL_IN_BEFORE_USE'

    # ****************************************************************************************
    # Establish the connection to Postgres and creating tables in the database with SQL file *
    # ****************************************************************************************
    try:
        # **********************************************************************
        # Connect the postgres database from your local machine using psycopg2 *
        # **********************************************************************
        connection = psycopg2.connect(
                                        database=database,              
                                        user=user,       
                                        password=password,   
                                        host=host,
                                        port=port
                                    )
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        # Executing a SQL query
        cursor.execute("SELECT version();")
        # Fetch result
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

        # ****************************************************************************
        # Populating tables in the database with SQLAlchemy and table_population.sql *
        # ****************************************************************************
        # Step 1: Connect to db using SQLAlchemy create_engine()
        DIALECT = 'postgresql+psycopg2://'
        db_uri = "%s:%s@%s/%s" % (user, password, host, database)
        print(DIALECT+db_uri) # postgresql+psycopg2://test_admin:pssword@localhost/tutorial4
        engine = create_engine(DIALECT + db_uri)
        psql_conn  = engine.connect()

        # Step 2: Read CSV files and populating tables with pandas dataframe
        CSV_  = ".csv"

        tables = ["VaccineData", # list of tables in the database that need to be populated
                "Manufacturer", 
                "MedicalFacility", 
                "VaccinationBatch", 
                "TransportationLog", 
                "StaffMember", 
                "VaccinationShift", 
                "VaccinationEvent", 
                "Patient", 
                "Symptom", 
                "Diagnosed", 
                "Attend"]

        for table in tables:
            filename = table + CSV_ # create actual csv filename. E.g., CSV file Manufacturer.csv

            # use pandas to read the csv file and load the data into dataframes
            df = pd.read_csv(DATADIR + '/data/CSVs/{}'.format(filename), sep=',', quotechar='"',dtype='unicode')

            # use pandas dataframe to loading data into tables in Postgres database
            # note: .lower() is used to decapitalize because everything in Postgres is in lowercase
            df.to_sql(table.lower(), con=psql_conn, if_exists='append', index=False)

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            psql_conn.close()
            # cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


main()