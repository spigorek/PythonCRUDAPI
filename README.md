# Shell
install apps: 
gitbush  
powershell
Install WSL (Ubuntu)

# Create account in GitHub or use existing one and create new repository

# Create a Virtual Environment:
python3 -m venv <name of virtual env>
example: `python3 -m venv automation`

# Activate the Virtual Environment:
Run: <name of virtual env>\Scripts\activate
Linux: source <name of virtual env>/bin/activate
example: `source automation/bin/activate`

# Deactivate existing virtual env in the current folder:
Run: deactivate
examle`pip freeze > requirements.txt`
example `pip install -r requirements.txt`

# creds files
in root folder must be 'creds/drugs_creds.py' with dictionary named 'drugs':
eg. drugs = {'email':'<your_email>',
        'password':'<your_psw>'}  

