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

from utils import (
    create_template,
    data_quality_check,
    fill_form,
    user_login,
    create_shipment,
    find_elements_with_text,
    find_and_click_button,
    click_button,
    find_checkbox_parent_with_text
)

from settings import *


def filling_forms(driver, wait, row):

    # Parent elements
    receiver_form = find_elements_with_text(wait, '//div[@class="shipment"]', 'Receiver')
    box_form = find_elements_with_text(wait, '//div[@class="__c-section"]', 'Shipment details')

    if receiver_form and box_form:            
        # Postcode
        fill_form(receiver_form, "ID", "postcodeView", row.loc['postcode'])


        # Name and surname
        fill_form(receiver_form, "NAME", "name", row.loc['name_surname'])

        # Phone number
        fill_form(receiver_form, "NAME", "phoneNumber", row.loc['phone'])

        # Address
        fill_form(receiver_form, "NAME", "addressLine1", row.loc['address'])

        # Company name
        fill_form(receiver_form, "NAME", "company", COMPANY_NAME)

        # Box
        fill_form(box_form, "NAME", "length", LENGTH)
        fill_form(box_form, "NAME", "width", WIDTH)
        fill_form(box_form, "NAME", "height", HEIGHT)
        fill_form(box_form, "NAME", "weight", WEIGHT)

        # Goods description
        fill_form(box_form, "NAME", "goodsDescription", GOODS_DESCRIPTION)
        fill_form(box_form, "NAME", "customerReference", row.loc['ref_num'])

    else:
        raise Exception("Error occured, I cannot find elements, contact Peter")

    # "Find prices" button click
    find_and_click_button(wait, "//button[@data-e2e-id='mytnt.createShipment.showQuotes']")

    # Find all prices elements, found one with "BEST PRICE" and click it
    best_price = find_elements_with_text(wait, '//div[@class="service-all"]', "BEST PRICE")
    best_price.click()


    
    # Find "Save shipment" button and click it
    find_and_click_button(wait, "//button[@data-e2e-id='mytnt.createShipment.pending']")


    # Parent elements checkboxes
    checkbox = find_checkbox_parent_with_text(wait, '//input[@type="checkbox"]', "Consignment note")
    checkbox.click()
    
    # Find and click Generate document button
    generate_documents = find_elements_with_text(wait, '//span', 'Generate documents')
    generate_documents.click()
                
    # Find and click generate labels button
    #generate_labels = find_elements_with_text(wait, '//span[@class="__c-btn__text"]', 'Shipping labels (A6)')
    #print("generate labels", generate_labels.text)
    sleep(2)
    driver.get('https://mytnt.tnt.com/?locale=en_GB#/create-shipment')

    #testfile = urllib.URLopener()
    #testfile.retrieve("http://randomsite.com/file.gz", "file.gz")

    #import wget

    #file_url = 'http://johndoe.com/download.zip'

    #file_name = wget.download(file_url)

    #print(file_name)


     

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

