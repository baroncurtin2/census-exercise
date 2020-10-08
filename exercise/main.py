from exercise.database_ops import *
from exercise.datapull import *


def main():
    creds = get_db_creds()
    create_tables(creds)

    api_key = get_census_key()
    data = pull_census_data(api_key)
    formatted_data = format_data(data)

    # insert data into tables
    for tbl, sql in INSERT_COMMANDS.items():
        insert_into(sql, formatted_data[tbl])

    # run query commands
    results = [run_query(query) for query in QUERY_COMMANDS]
    print(results)


if __name__ == '__main__':
    main()
