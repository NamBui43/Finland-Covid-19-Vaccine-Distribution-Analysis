import psycopg2
from psycopg2 import Error
from sqlalchemy import create_engine, text
import pandas as pd
import numpy as np
from pathlib import Path

def run_sql_from_file(sql_file, psql_conn):
    '''
	read a SQL file with multiple stmts and process it
	adapted from an idea by JF Santos
	Note: not really needed when using dataframes.
    '''
    sql_command = ''
    for line in sql_file:
        #if line.startswith('VALUES'):        
     # Ignore commented lines
        if not line.startswith('--') and line.strip('\n'):        
        # Append line to the command string, prefix with space
           sql_command +=  ' ' + line.strip('\n')
           #sql_command = ' ' + sql_command + line.strip('\n')
        # If the command string ends with ';', it is a full statement
        if sql_command.endswith(';'):
            # Try to execute statement and commit it
            try:
                #print("running " + sql_command+".") 
                psql_conn.execute(text(sql_command))
                #psql_conn.commit()
            # Assert in case of error
            except:
                print('Error at command:'+sql_command + ".")
                ret_ =  False
            # Finally, clear command string
            finally:
                sql_command = ''           
                ret_ = True
    return ret_

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
    port= 'FILL_IN_BEFORE_USE'

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

        # **********************************************************************
        # Create tables in the database with SQLAlchemy and table_creation.sql *
        # **********************************************************************
        # Step 1: Connect to db using SQLAlchemy create_engine()
        DIALECT = 'postgresql+psycopg2://'
        db_uri = "%s:%s@%s/%s" % (user, password, host, database)
        print(DIALECT+db_uri)
        engine = create_engine(DIALECT + db_uri)
        sql_file1  = open(DATADIR + '/code/table_creation.sql')
        psql_conn  = engine.connect()

        # Step 2: Read SQL files for CREATE TABLE 
        run_sql_from_file (sql_file1, psql_conn)

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            psql_conn.close()
            connection.close()
            print("PostgreSQL connection is closed")


main()
