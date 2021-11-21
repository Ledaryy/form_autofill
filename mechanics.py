# Author: Andras Kulisov
# Copyright: Peter Kulisov <peter.kulisov@gmail.com>
# If there are any issues contact me on the email above.
#
# Version 1.0
# Date: 2021-11

import os

from time import sleep
from selenium.webdriver.common.by import By


from urllib.request import urlopen
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.expected_conditions import (
    presence_of_all_elements_located, presence_of_element_located
)

from utils import (
    find_elements_with_text,
    find_and_click_button,
    click_button,
    find_checkbox_parent_with_text,
    fill_form,
)

from settings import (
    COMPANY_NAME,
    LENGTH,
    WIDTH,
    HEIGHT,
    WEIGHT,
    GOODS_DESCRIPTION,
)


def filling_forms(driver, wait, row):
    try:
        # Parent elements
        receiver_form = find_elements_with_text(wait, '//div[@class="shipment"]', 'Receiver')
        box_form = find_elements_with_text(wait, '//div[@class="__c-section"]', 'Shipment details')
        
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


        # "Find prices" button click
        find_and_click_button(wait, "//button[@data-e2e-id='mytnt.createShipment.showQuotes']")

        # Find all prices elements, found one with "BEST PRICE" and click it
        best_price = find_elements_with_text(wait, '//div[@class="service-all"]', "BEST PRICE")
        best_price.click()

    except Exception as e:
        raise Exception(f"Filling form id: {row.loc['id']} failed, details {e}")

def save_shipment(driver, wait, row):
    try:

        # Find "Save shipment" button and click it
        find_and_click_button(wait, "//button[@data-e2e-id='mytnt.createShipment.pending']")


        # Parent elements checkboxes
        checkbox = find_checkbox_parent_with_text(wait, '//input[@type="checkbox"]', "Consignment note")
        checkbox.click()
        
        # Find and click Generate document button
        generate_documents = find_elements_with_text(wait, '//span', 'Generate documents')
        generate_documents.click()
                    
        # Get url and save pdf document
        generate_labels = wait.until(presence_of_element_located((By.XPATH, "//a[@class='__c-btn __u-mb--m' and @target='_blank']")))
        pdf_url = generate_labels.get_attribute("href")
        cwd = os.getcwd()
        destination = cwd + '/pdf/'

        response = urlopen(pdf_url)
        file = open(f"{destination}{row.loc['ref_num']}.pdf", 'wb')
        file.write(response.read())
        file.close()

        driver.get('https://mytnt.tnt.com/?locale=en_GB#/create-shipment')

    except Exception as e:
        raise Exception(f"Saving shipment id: {row.loc['id']} failed, details {e}")

def data_parser(df):
    if df.empty:
        raise Exception("No data to process")
    if not df.loc[df['id'].isnull()].empty:
        raise Exception("ID is empty")
    if not df.loc[df['postcode'].isnull()].empty:
        raise Exception("Postcode is empty")
    if not df.loc[df['name_surname'].isnull()].empty:
        raise Exception("Name and surname is empty")
    if not df.loc[df['phone'].isnull()].empty:
        raise Exception("Phone number is empty")
    if not df.loc[df['address'].isnull()].empty:
        raise Exception("Address is empty")
    if not df.loc[df['ref_num'].isnull()].empty:
        raise Exception("Reference number is empty")
    
    # Removing whitespaces from postcode
    for i in range(len(df)):
        post_code = df.loc[i, 'postcode']
        post_code = ''.join(post_code.split())
        df.loc[i, 'postcode'] = post_code
        
    return df
         