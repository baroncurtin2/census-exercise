# standard imports
import json
from collections import OrderedDict
from pathlib import Path

# third party imports
import psycopg2

DB_CREDS = Path(__file__).parents[0] / 'creds/db_creds.json'
POVERTY_THRESHOLDS = Path(__file__).parents[0] / 'data/poverty_line.csv'
CREATE_COMMANDS = (Path(__file__).parents[0] / 'sql_commands').glob('*create*.sql')
QUERY_COMMANDS = (Path(__file__).parents[0] / 'sql_commands').glob('*query*.sql')
INSERT_COMMANDS = OrderedDict([
    ('zipcodes', 'INSERT INTO zipcodes (zip_code) VALUES(%(zip_code)s)'),
    ('income', 'INSERT INTO income (zip_code, median_income) VALUES(%(zip_code)s, %(median_income)s)'),
    ('population', 'INSERT INTO population (zip_code, population) VALUES(%(zip_code)s, %(population)s)'),
    ('poverty', 'INSERT INTO poverty (zip_code, population) VALUES(%(zip_code)s, %(population)s)')
])


def get_db_creds(filename=DB_CREDS):
    # load credentials
    if filename:
        with filename.open(mode='r') as file:
            creds = json.load(file)
        return creds
    else:
        raise Exception('No credentials file found')


def create_tables(creds, command_files=CREATE_COMMANDS):
    conn = None

    try:
        # connect to postgres server
        conn = psycopg2.connect(**creds)
        cur = conn.cursor()

        for cmd_file in command_files:
            cmd = cmd_file.read_text()
            cur.execute(cmd)

        # close communications
        cur.close()

        # commit changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_poverty_thresholds(creds, data=POVERTY_THRESHOLDS, table='poverty_thresholds'):
    conn = None

    try:
        # connect to postgres server
        conn = psycopg2.connect(**creds)
        cur = conn.cursor()

        # copy from csv into table
        with data.open(mode='r') as file:
            cur.copy_from(file, table, sep=',')

        # close communications
        cur.close()

        # commit changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_into(sql, data):
    """ insert multiple entries into the specified table  """
    conn = None

    try:
        # read database configuration
        creds = get_db_creds()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**creds)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql, data)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def run_query(query):
    conn = None

    try:
        # read database configuration
        creds = get_db_creds()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**creds)
        # create a new cursor
        cur = conn.cursor()
        # execute the query statement
        sql = query.read_text()
        cur.execute(sql)
        data = cur.fetchall()
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()

        return data
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
