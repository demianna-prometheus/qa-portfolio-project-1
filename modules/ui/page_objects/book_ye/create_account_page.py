from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class CreateAccountPage(BasePage):
    URL = 'https://book-ye.com.ua/customer/account/create/'

    def go_to_create_account_page(self):
        self.driver.get(CreateAccountPage.URL)
    
    def fill_create_account_form(self, first_name, last_name, email, phoneNumber, password):
        first_name_elem = self.driver.find_element(By.ID, "firstname")
        first_name_elem.send_keys(first_name)

        last_name_elem = self.driver.find_element(By.ID, "lastname")
        last_name_elem.send_keys(last_name)

        email_elem = self.driver.find_element(By.ID, "email_address")
        email_elem.send_keys(email)

        phone_number_elem = self.driver.find_element(By.ID, "phone")
        phone_number_elem.send_keys(phoneNumber)

        password_elem = self.driver.find_element(By.ID, "password") 
        password_elem.send_keys(password)

        confirm_password_elem = self.driver.find_element(By.ID, "password-confirmation")
        confirm_password_elem.send_keys(password)

        tick_elem = self.driver.find_element(By.ID, "consent_to_personal_data")
        tick_elem.get_attribute("checked")

        signup_btn_elem = self.driver.find_element(By.ID, "send2")
        signup_btn_elem.click()
    
    def check_created_profile(self, expected_title):
        return self.driver.title == expected_title



