from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators


class LoginPage:

    def __init__(self, context):
        self.context = context.browser
        self.find_ele = lambda loc, wait_time: WebDriverWait(self.context, wait_time).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, loc)))

    def enter_valid_login(self, username, password):
        self.find_ele(Locators.username, 10).send_keys(username)
        self.find_ele(Locators.password, 10).send_keys(password)
        self.context.find_element_by_css_selector(Locators.submitBtn).click()
