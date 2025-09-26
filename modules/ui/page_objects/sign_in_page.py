from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password): 
        login_elem = self.driver.find_element(By.ID, "login_field")  # Find the field for entering username or email
        login_elem.send_keys(username)  # Enter username or email
        pass_elem = self.driver.find_element(By.ID, "password")  # Find the field for entering password
        pass_elem.send_keys(password)  # Enter password
        btn_elem = self.driver.find_element(By.NAME, "commit")  # Find the sign in button
        btn_elem.click()  # Simulate left mouse button click

    def check_title(self, expected_title):
        return self.driver.title == expected_title

    

