# Author: Andras Kulisov
# Copyright: Peter Kulisov <peter.kulisov@gmail.com>
# If there are any issues contact me on the email above.
#
# Version 1.0
# Date: 2021-11

import pandas as pd 

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from settings import *

from mechanics import (
    filling_forms,
    save_shipment
)

from utils import (
    create_template,
    data_quality_check,
    user_login,
    create_shipment,
)

from datetime import datetime

#big fucking function
def main_function(
    excel_path=None,
    **value
):
    # Creating template file
    #print("mat tvou ebal",excel_path)
    #decision = "no"
    #decision = input("Do you want to create template file? (yes/no): ") 

    #if decision == "yes":
     #   create_template()
    #else: 
    #   print("Ok, step skiped")


    # Starting filling the forms
    decision_2 = "yes"
    #decision_2 = input("Do you want to fill the forms? (yes/no): ") 

    if decision_2 == "yes":

        # Importing excel file, parsing the file
        file = excel_path
        data = pd.ExcelFile(file)
        df = data.parse(data.sheet_names[0])

        # Check the data quality
        data_quality_check(df)

        # Filling the forms
        decision_3 = "yes"
        #decision_3 = input("Data looks right? (yes/no): ")
        
        if decision_3 == "yes":
            with webdriver.Chrome(ChromeDriverManager().install()) as driver:
                driver.get(URL_ENDPOINT)
                wait = WebDriverWait(driver, 10)

                # Login user
                user_login(wait)

                # Open the menu, create a shipment
                create_shipment(wait)

                # TODO remove me for i in range(df.index.stop):
                for i in range(df.index.stop):
                    row = df.iloc[i]
                    print(f"Processing form with id: {row.loc['id']}, ref_num: {row.loc['ref_num']}")
                    try:
                        filling_forms(driver, wait, row)
                        save_shipment(driver, wait, row)
                        row.loc['status'] = "Success"
                        df.loc[i] = row

                    except Exception as e:
                        print(f"Error {e} occured, skipping this form")
                        row.loc['status'] = "Failed"
                        df.loc[i] = row

            # Saving the status of the form
            time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            df.to_excel(f'report-{time_stamp}.xlsx', index=False)

            print(df)
            print("Data filling completed, number of errors: ", df[df.status == "Failed"].shape[0])
            print(f"Report was generated: report-{time_stamp}.xlsx")
            print("If you want to see the report, open the file in your excel")
            print("Thank you for using our amazing software")
        else:
            print("Ok, go correct the data")

