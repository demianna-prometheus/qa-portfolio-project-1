import pytest
from modules.ui.page_objects.bookye.login_page import LoginPage

@pytest.mark.bookye
def test_correct_login():
    login_page = LoginPage()
    login_page.go_to_login_page()
    login_page.fill_login_form(
        email = "j.anna.shevchuk@gmail.com",
        password = "Qwerty12345"
    )

    assert login_page.check_logged_in_profile("Мій профіль")
