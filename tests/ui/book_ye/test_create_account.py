import pytest

from modules.ui.page_objects.book_ye.create_account_page import CreateAccountPage

@pytest.mark.bookye
def test_correct_account_creation():
    create_account_page = CreateAccountPage()
    create_account_page.go_to_create_account_page()
    create_account_page.fill_create_account_form(
        first_name = "Anna",
        last_name = "Testing",
        email = "j.anna.shevchuk@gmail.com",
        phoneNumber = "0671234567",
        password = "Qwerty12345"
    )
    assert create_account_page.check_created_profile("Мій профіль")
