from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(10)
    IsThereAButton = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert IsThereAButton, "No button add to basket"