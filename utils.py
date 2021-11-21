# Author: Andras Kulisov
# Copyright: Peter Kulisov <peter.kulisov@gmail.com>
# If there are any issues contact me on the email above.
#
# Version 1.0
# Date: 2021-11


import random
import pandas as pd
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
    presence_of_all_elements_located, presence_of_element_located
)

from settings import (
    USERNAME,
    PASSWORD,
    FILE_NAME
)

def create_template():
    try:
        df = pd.DataFrame(columns=['id', 'ref_num', 'name_surname', 'phone', 'address', 'postcode', 'status'])
        df.to_excel(FILE_NAME, index=False)
        print("Success")
    except Exception as e:
        raise Exception(f"I cannot create template, Error details: {e}")

def data_quality_check(df):
    try:
        random_data = []
        for i in range(5):
            row_number = random.randint(0, (df.index.stop - 1))
            print(row_number)
            data_row = df.iloc[row_number]
            random_data.append(data_row)
        print("Some random samples of data: ")
        for i in random_data:
            print(i)
    except Exception as e:
        raise Exception(f"I cannot do data quality check, Error details: {e}")

def fill_form(parent_form, by_tag, id, data):
    try:
        timeout = time.time() + 2   # 2 sec from now
        while True:
            form = parent_form.find_element(getattr(By,by_tag), id)
            form.clear()
            form.send_keys(f"{data}")
            check_form = parent_form.find_element(getattr(By,by_tag), id)

            if str(data) == str(check_form.get_attribute("value")):
                break

            if time.time() > timeout:
                raise Exception("Fill form timed out")

    except Exception as e:
        raise Exception(f"I cannot fill form, Error details: {e}")

def user_login(wait):
    try:
        cookies_button = wait.until(presence_of_element_located((By.XPATH, "//button[@class='cc-button cc-button--acceptAll']")))

        email = wait.until(presence_of_element_located((By.ID, "email")))
        password = wait.until(presence_of_element_located((By.ID, "password")))
        login_button = wait.until(presence_of_element_located((By.CLASS_NAME, "__c-btn")))

        cookies_button.click()
        email.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        login_button.click()
    except Exception as e:
        raise Exception(f"I cannot login user, Error details: {e}")

def create_shipment(wait):
    try:
        # Menu
        menu_button = wait.until(presence_of_element_located((By.XPATH, "//a[@class='side-nav__toggle']")))
        menu_button.click()

        # Create shipment
        shipment_button = wait.until(presence_of_element_located((By.XPATH, "//a[@class='side-nav__block__button __c-btn __u-width--100']")))
        success_shipment_button = False
        while not success_shipment_button:
            try:
                shipment_button.click()
                success_shipment_button = True
            except Exception:
                pass
    except Exception as e:
        raise Exception(f"I cannot click on shipment button, Error details: {e}")

def find_elements_with_text(wait, xpath, value):
    try:
        all_forms = wait.until(presence_of_all_elements_located((By.XPATH, xpath)))
        result = None
        for form in all_forms:
            if f"{value}" in form.text:
                result = form
        return result
    except Exception as e:
        raise Exception(f"[Utils]: I cannot find elements with text, Error details: {e}")

def find_and_click_button(wait, xpath):
    try:
        button = wait.until(presence_of_element_located((
            By.XPATH, xpath
        )))
        timeout = time.time() + 2   # 2 sec from now
        while True:
            try:
                button.click()
            except Exception:
                break

            if time.time() > timeout:
                raise Exception("Click button timed out")

    except Exception as e:
        raise Exception(f"I cannot find and click button, Error details: {e}")

def click_button(button):
    try:
        while True:
            button.click()
    except Exception:
        pass

def find_checkbox_parent_with_text(wait, xpath, value):
    try:

        while True:
            checkboxes = wait.until(presence_of_all_elements_located((By.XPATH, xpath)))
            for checkbox in checkboxes:
                parent = checkbox.find_element_by_xpath('..')
                if f"{value}" in parent.text:
                    return checkbox
    except Exception as e:
        raise Exception(f"I cannot find checkbox parent with text, Error details: {e}")