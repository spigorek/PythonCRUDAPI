import json
import os
import pytest
import requests
import logging
from src.users_params import base_url, ep_users

user_amount = 3
id_starts_with = "777"
name_starts_with = "auto_777"

@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.functional
def test_create_users_success():
    test_case ="""
    Test case: Create users with success
    Steps:              
    1. Create users with success
    2. Delete users with success       
    """
    logging.info(test_case)    
    all_user_ids = []
    failed_id_status_codes = {}
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
        if response.status_code != 200: 
            failed_id_status_codes[id] = response.status_code 
        print(response.text)
    
    for id in all_user_ids:
        url = os.path.join(base_url, ep_users, id)
        payload = ""
        headers = {}

        response = requests.request("DELETE", url, headers=headers, data=payload)
        print(response.text)

    assert len(failed_id_status_codes) == 0, f"Some users were not been created {failed_id_status_codes}"


@pytest.mark.regression
@pytest.mark.performance
def test_create_users_unsuccess():
    test_case ="""
    Test case: Create users with unsuccess
    Steps:
    1. Create users with unsuccess
    2. Delete users with success

    """
    
    all_user_ids = [] 
    success_id_status_codes = {} 
    url = os.path.join(base_url, ep_users) 
    for n_user in range(user_amount):    
        id = f"{id_starts_with}{n_user}"
        name = f"{name_starts_with}{n_user}"
        # Wrong payload as a dictionary instead of Json
        payload = {
                "name": name,
                "id": id 
            }
 
        headers = {
               'Content-Type': 'application/json'
                }
        response = requests.request("POST", url, headers=headers, data=payload)
        all_user_ids.append(id)
        if response.status_code == 200: 
            success_id_status_codes[id] = response.status_code
        logging.info(f"status code for unsuccess creation = {response.status_code}")
    
    for id, status in success_id_status_codes:
        url = os.path.join(base_url, ep_users, id)
        payload = ""
        headers = {}

        response = requests.request("DELETE", url, headers=headers, data=payload)
        logging.info(f"status code for deletion = {response.status_code}")

    assert len(success_id_status_codes) == 0, f"Some users have been created {success_id_status_codes}"