from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    URL = 'https://book-ye.com.ua/customer/account/login/'

    def go_to_login_page(self):
        self.driver.get(LoginPage.URL)
    
    def fill_login_form(self, email, password):
        email_elem = self.driver.find_element(By.ID, "email")
        email_elem.send_keys(email)

        password_elem = self.driver.find_element(By.ID, "pass")
        password_elem.send_keys(password)

        remmember_me_elem = self.driver.find_element(By.ID, "remember-me-box")
        remmember_me_elem.get_attribute("checked")

        login_btn_elem = self.driver.find_element(By.ID, "send2")
        login_btn_elem.click()
    
    def check_logged_in_profile(self, expected_title):
        return self.driver.title == expected_title