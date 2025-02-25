login_success:
	pytest -v --capture=no --tb=long src/drugs_auth/test_login_post.py
search_success:
	pytest -v --capture=no --tb=long src/drugs_reports/test_search_get.py
create_users:
	pytest -v --capture=no --tb=long src/users/test_create.py