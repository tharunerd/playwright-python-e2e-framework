from playwright.sync_api import expect
from pages.login_page import LoginPage


def test_valid_login(page):

    login_page = LoginPage(page)

    login_page.navigate()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )