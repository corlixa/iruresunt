from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_Xpath(driver, timeout, xpath):
    try:
        # Wait until the element is clickable
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        # Click the element
        element.click()
        print(f"Clicked the element with Xpath: {xpath}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
update_btn_xpath = "//button[@id='update-btn']"
click_Xpath(driver, 10, update_btn_xpath)
