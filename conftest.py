import json
import pytest
import requests
import logging
import os
from src.users_params import base_url, ep_users

def pytest_html_report_title(report): # this function is used to change the title of the report
    report.title = "Report Igor"

@pytest.fixture(scope='module') # scope='module' - the fixture is created once per module (Module, Session, Class, Function)
def create_x_users():
    user_amount = 1 # to do - add to params
    id_starts_with = "id_from_fixture_"
    name_starts_with = "name_from_fixture_"

    all_user_ids = []
    url = os.path.join(base_url, ep_users) 
    for n_user in range(user_amount):    
        id = f"{id_starts_with}{n_user}"
        name = f"{name_starts_with}{n_user}"
        payload = json.dumps(
            {
                "name": name,
                "id": id 
            }
        )
        headers = {
                'Content-Type': 'application/json'
                 }
        response = requests.request("POST", url, headers=headers, data=payload)
        all_user_ids.append(id)
        assert response.status_code == 200, print("Wrong status code --- ", response.status_code)
        logging.info(f"user created {response.text}")
        
    
    logging.info('before yeld')

    yield all_user_ids
    logging.info('after yeld')
    for id in all_user_ids:
        url = os.path.join(base_url, ep_users, id)
        payload = ""
        headers = {}

        response = requests.request("DELETE", url, headers=headers, data=payload)
        logging.info(f"user deleted {response.text}")

