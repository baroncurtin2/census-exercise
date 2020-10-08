# standard imports
from collections import defaultdict
from pathlib import Path
import json

# third party imports
from census import Census
from us import states

# app imports
from .database_ops import get_db_creds

CENSUS_CREDS = Path(__file__).parents[0] / 'creds/census_creds.json'

# population total, population below poverty level, median household income
CENSUS_VARIABLES = ('B01003_001E', 'B17001_002E', 'B19013_001E')
HEADERS = ('population', 'poverty', 'median_income')


def get_census_key(filepath=CENSUS_CREDS):
    # read json file
    with filepath.open(mode='r') as file:
        data = json.load(file)
        key = data['api_key']

    if key:
        return key
    else:
        raise Exception('API key not found')


def pull_census_data(api_key, fields=CENSUS_VARIABLES):
    c = Census(api_key)
    return c.acs5.zipcode(fields, Census.ALL)


def format_data(data):
    formatted_data = defaultdict(list)

    for row in data:
        formatted_data['zipcodes'].append({'zip_code': row['zip code tabulation area']})

        formatted_data['income'].append({'zip_code': row['zip code tabulation area'],
                                         'median_income': row['B19013_001E']})

        formatted_data['population'].append({'zip_code': row['zip code tabulation area'],
                                             'population': row['B01003_001E']})

        formatted_data['poverty'].append({'zip_code': row['zip code tabulation area'],
                                          'population': row['B17001_002E']})

    return formatted_data
