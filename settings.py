# Author: Andras Kulisov
# Copyright: Peter Kulisov <peter.kulisov@gmail.com>
# If there are any issues contact me on the email above.
#
# Version 1.0
# Date: 2021-11

import os

from dotenv import load_dotenv

# Loading .env file
load_dotenv()

# User settings
USERNAME = os.environ["TNT_USERNAME"]
PASSWORD = os.environ["TNT_PASSWORD"]

# Configs
URL_ENDPOINT="https://mytnt.tnt.com"
FILE_NAME="data_entry_template.xlsx"

# Box config
LENGTH = "35"
WIDTH = "25"
HEIGHT = "15"
WEIGHT = "1"
GOODS_DESCRIPTION = "IT Equipment"


# Form settings
COMPANY_NAME = "Computacenter LTD"