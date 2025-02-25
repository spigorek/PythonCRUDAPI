import json
import pytest
import requests
import logging
from creds.drugs_creds import drugs

def test_login_success():
    data = {'email': drugs['email'], 'password': drugs['password']}
    url = 'https://www.drugshortagescanada.ca/api/v1/login'
    r = requests.post(url, data=data)
    assert r.status_code == 200, print("Wrong status code --- ", r.status_code)
    print(r.status_code)
    authToken = r.headers['auth-token']
    print(authToken)
