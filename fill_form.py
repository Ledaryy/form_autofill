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


    