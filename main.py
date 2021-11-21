# Author: Andras Kulisov
# Copyright: Peter Kulisov <peter.kulisov@gmail.com>
# If there are any issues contact me on the email above.
#
# Version 1.0
# Date: 2021-11-18

import os
import pandas as pd 
import urllib


from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located, presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from dotenv import load_dotenv
load_dotenv()

from settings import *

from fill_form import filling_forms

from utils import (
    create_template,
    data_quality_check,
    user_login,
    create_shipment,
)



# Creating template file
decision = input("Do you want to create template file? (yes/no): ") 
if decision == "yes":
    create_template()
else:
    print("Ok, step skiped")


# Starting filling the forms
decision_2 = input("Do you want to fill the forms? (yes/no): ") 
if decision_2 == "yes":

    # Importing excel file, parsing the file
    file = FILE_NAME
    data = pd.ExcelFile(file)
    df = data.parse(data.sheet_names[0])

    # Check the data quality
    data_quality_check(df)
    decision_3 = input("Data looks right? (yes/no): ")
    
    # Filling the forms
    if decision_3 == "yes":
        with webdriver.Chrome(ChromeDriverManager().install()) as driver:
            driver.get(URL_ENDPOINT)
            wait = WebDriverWait(driver, 10)

            # Login user
            user_login(wait)

            # Open the menu, create a shipment
            create_shipment(wait)

            for i in range(df.index.stop):
                row = df.iloc[i]
                print(f"Processing form with id: {row.loc['id']}, ref_num: {row.loc['ref_num']}")
                filling_forms(driver, wait, row)
    else:
        print("Ok, go correct the data")

