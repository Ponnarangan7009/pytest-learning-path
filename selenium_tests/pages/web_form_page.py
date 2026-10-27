from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class WebFormPage:
    URL = "https://www.selenium.dev/selenium/web/web-form.html"
    TEXT_FIELD = (By.NAME, "my-text")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button")
    MESSAGE = (By.ID, "message")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def enter_text(self, text):
        self.driver.find_element(*self.TEXT_FIELD).send_keys(text)

    def submit(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def get_message(self):
        message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.MESSAGE)
        )
        return message.text

    def is_text_field_displayed(self):
        return self.driver.find_element(*self.TEXT_FIELD).is_displayed()

    def get_text_field_value(self):
        return self.driver.find_element(*self.TEXT_FIELD).get_attribute("value")