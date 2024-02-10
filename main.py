from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

chrome_options = webdriver.ChromeOptions ( )
chrome_options.add_argument('--incognito')
chrome_options.add_argument ( '--start-maximized' )
driver = webdriver.Chrome (options = chrome_options)
ChromeOption = path="C:\\Users\\pavel\\PycharmProjects\\WebSiteTest\\webdriver\\chromedriver-win64\\chromedriver.exe"




driver.get("https://analysis-qa.geneyx.com/Account/Logon")
print(driver.title)
user = driver.find_element(By.CSS_SELECTOR, '#workareaContainer > div > div > div:nth-child(2) > div > div >'
                                            ' section > form > fieldset > div:nth-child(3)'
                                            ' > div > input').send_keys('test@geneyx.com')
passw = driver.find_element(By.CSS_SELECTOR, '#workareaContainer > div > div > div:nth-child(2) > '
                                             'div > div > section > form > fieldset >'
                                             ' div:nth-child(4) > div > input').send_keys('Test@123!')
btn = driver.find_element(By.CSS_SELECTOR, '#workareaContainer > div > div > '
                                           'div:nth-child(2) > div > div >'
                                           ' section > form > fieldset > '
                                           'div:nth-child(5) > div > button').click()
element = WebDriverWait ( driver, 10 ).until (
    EC.visibility_of_element_located ((By.CSS_SELECTOR, 'body > div.app.app-header-fixed.'
                                                        'app-aside-fixed.bg-light.hidden-xs > header '
                                                        '> nav > a > img.app-logo-text.inline-block') )
)
assert element

print(driver.title)

new_analysis = WebDriverWait ( driver, 10 ).until (
    EC.visibility_of_element_located ((By.CSS_SELECTOR,'#dashboard > section:nth-child(1) > div > div'
                                     ' > div.list > div > div.row.panel-tool-header '
                                     '> div.col-sm-5 > div > div > a > i.p-l-xs.ng-binding'))).click()
long_reads_analysis = WebDriverWait ( driver, 10 ).until (
    EC.visibility_of_element_located ((By.CSS_SELECTOR,'body > div.app.app-header-fixed.'
                                     'app-aside-fixed.bg-light.hidden-xs '
                                     '> div.app-content > div.app-content-body.ng-scope '
                                     '> div > div.row.row-eq-height > div.col-lg-8.col-md-12.p-r-none.col-eq-height '
                                     '> div > div > div.wizard-steps > div > div:nth-child(1) '
                                     '> section > div > div:nth-child(2) > div:nth-child(2) '
                                     '> div:nth-child(2) > div'))).click()

print(driver.title)
input_fields = driver.find_elements(By.TAG_NAME, "input")

# Iterate through the list of input elements
for input_field in input_fields:
    field_type = input_field.get_attribute("type")
    if field_type == "text":
        # For text, email, or password fields, fill them with a sample value
        input_field.send_keys("Sample Text")
    elif field_type == "checkbox":
        # For checkbox fields, check if it's already checked, if not, click it
        if not input_field.is_selected():
            input_field.click()
    elif field_type == "radio":
        # For radio buttons, check if it's already selected, if not, click it
        if not input_field.is_selected():
            input_field.click()
    # Add more conditions for handling other types of input fields as needed

    # Print the details of the input field
    print("Input Field Type:", field_type)
    print("Input Field Name:", input_field.get_attribute("name"))
    print("Input Field ID:", input_field.get_attribute("id"))
    print("Input Field Value:", input_field.get_attribute("value"))
    print("---------------------")

