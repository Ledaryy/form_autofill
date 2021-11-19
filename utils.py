import random
import pandas as pd

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
    presence_of_all_elements_located, presence_of_element_located
)

from settings import (
    USERNAME,
    PASSWORD,
)

def create_template():
    try:
        df = pd.DataFrame(columns=['id', 'ref_num', 'name_surname', 'phone', 'address', 'postcode'])
        df.to_excel('template.xlsx', index=False)
        print("Success")
    except Exception as e:
        print(f"Error details: {e}")
        print("Error occured, contact Peter")

def data_quality_check(df):
    random_data = []
    for i in range(5):
        row_number = random.randint(0, (df.index.stop - 1))
        print(row_number)
        data_row = df.iloc[row_number]
        random_data.append(data_row)
    print("Some random samples of data: ")
    for i in random_data:
        print(i)

def fill_form(parent_form, by_tag, id, data):
    while True:
        form = parent_form.find_element(getattr(By,by_tag), id)
        form.clear()
        form.send_keys(f"{data}")
        check_form = parent_form.find_element(getattr(By,by_tag), id)

        if str(data) == str(check_form.get_attribute("value")):
            break

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
    all_forms = wait.until(presence_of_all_elements_located((By.XPATH, xpath)))
    result = None
    for form in all_forms:
        if f"{value}" in form.text:
            result = form
    return result

def find_and_click_button(wait, xpath):
    button = wait.until(presence_of_element_located((
        By.XPATH, xpath
    )))
    try:
        while True:
            button.click()
    except Exception:
        pass

def click_button(button):
    try:
        while True:
            button.click()
    except Exception:
        pass

def find_checkbox_parent_with_text(wait, xpath, value):
    while True:
        checkboxes = wait.until(presence_of_all_elements_located((By.XPATH, xpath)))
        for checkbox in checkboxes:
            parent = checkbox.find_element_by_xpath('..')
            if f"{value}" in parent.text:
                return checkbox