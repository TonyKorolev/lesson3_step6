from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(10)
    buttonArr = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert len(buttonArr) == 1, "No button add to basket"