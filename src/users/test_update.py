import json
import os
import pytest
import requests
import logging
from src.users_params import base_url, ep_users



@pytest.mark.smoke
@pytest.mark.regression
def test_update_users_success(create_x_users):
    test_case ="""
    Test case: Update users with success
    Steps:
    1. Create users with success from fixture    
    2. Update users with success    
    3. Delete users with success from fixture
    4. Check that all users were updated with success (assertion)   
    """
    logging.info(test_case)

    all_user_ids = create_x_users
    logging.info(f"all_user_ids= {all_user_ids}")
    failed_id_status_codes = {}
    for s_id in all_user_ids: 
        url = os.path.join(base_url, ep_users, s_id)   
        new_name = f"new_name_{s_id}"
        payload = json.dumps(
            {
                "name": new_name
            }
        )
        headers = {
                'Content-Type': 'application/json'
                 }
        response = requests.request("PUT", url, headers=headers, data=payload)
        if response.status_code != 200: 
            failed_id_status_codes[id] = response.status_code 
        logging.info(response.text)
   

    assert len(failed_id_status_codes) == 0, f"Some users were not been created {failed_id_status_codes}"

