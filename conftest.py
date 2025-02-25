import json
import pytest
import requests
import logging
import os
from creds.drugs_creds import drugs
from src.users_params import base_url, ep_users, n_created_users




@pytest.fixture(scope='session')
def get_token():
    data = {'email': drugs['email'], 'password': drugs['password']}
    url = 'https://www.drugshortagescanada.ca/api/v1/login'
    r = requests.post(url, data=data)
    assert r.status_code == 200, print("Wrong status code --- ", r.status_code)
    authToken = r.headers['auth-token']
    return authToken

@pytest.fixture(scope='session')
def create_x_users():
    all_user_ids = []
    url = os.path.join(base_url, ep_users) 
    for n_user in range(n_created_users):    
        id = f"1222{n_user}"
        name = f"auto_{n_user}"
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
        assert response.status_code == 200, print("Wrong status code --- ", r.status_code)
        print(response.text)
    
    print('before yeld')
    yield all_user_ids
    print('after yeld')
    for id in all_user_ids:
        url = os.path.join(base_url, ep_users, id)
        payload = ""
        headers = {}

        response = requests.request("DELETE", url, headers=headers, data=payload)
        assert response.status_code == 200, print("Wrong status code --- ", r.status_code)
        print(response.text)

