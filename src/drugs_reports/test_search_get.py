import json
import pytest
import requests
import logging

def test_search_success(get_token):   
    parameters = {'term': 'BAXTER CORPORATION', 'limit': 1, 'offset': 0}
    headers = {'auth-token': get_token}
    url = 'https://www.drugshortagescanada.ca/api/v1/search'
    r = requests.get(url, headers=headers, params=parameters)
    logging.info(f'status_code = {r.status_code}')
    if r.status_code == 200:
        responseJson = r.json()
        reports = responseJson['data']
      
    for s_company in reports:
        logging.info(f'reports={s_company["drug"]["company"]}')
        actual_city = s_company["drug"]["company"]["city"]

    expected_city = "MISSISSAUGA"
    assert actual_city == expected_city, f'The is wrong, actual = {actual_city}'