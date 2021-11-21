# Author: Andras Kulisov
# Copyright: Peter Kulisov <peter.kulisov@gmail.com>
# If there are any issues contact me on the email above.
#
# Version 1.0
# Date: 2021-11-18

# Info
For navigation between folders, use "cd", "cd ..", "dir"

# Execution process
1. isntall python
download it from python website or microsoft app store

2. execute
pip3 install virtualenv

3. create virtual envitement
virtualenv venv

4. enter your envirement
venv\Scripts\Activate

5. download python libraries
pip install -r requirements.txt

5. execute python script
(venv)
python main.py

# Possible errors
1. install this package: python-dotenv
2. virtualenv not working: restart cmd

# Notes
Script using a username + password provided by user
Script do not save any password, so the file with credentials should be provided by the user
