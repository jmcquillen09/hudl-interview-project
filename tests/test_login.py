from pages.login_page import LoginPage
from pages.home_page import HomePage


class TestLoginPageUI:
    def test_hudl_logo_is_displayed(self, login_page_ui):
        assert login_page_ui.find(login_page_ui._LOGO) is not None

    def test_log_in_heading_is_displayed(self, login_page_ui):
        assert login_page_ui.is_visible(login_page_ui._HEADING)

    def test_google_login_option_is_clickable(self, login_page_ui):
        assert login_page_ui.find_clickable(login_page_ui._GOOGLE_BTN) is not None

    def test_facebook_login_option_is_clickable(self, login_page_ui):
        assert login_page_ui.find_clickable(login_page_ui._FACEBOOK_BTN) is not None

    def test_apple_login_option_is_clickable(self, login_page_ui):
        assert login_page_ui.find_clickable(login_page_ui._APPLE_BTN) is not None

    def test_create_account_link_is_displayed(self, login_page_ui):
        assert login_page_ui.find_clickable(login_page_ui._CREATE_ACCOUNT) is not None

    def test_privacy_policy_link_is_clickable(self, login_page_ui):
        assert login_page_ui.find_clickable(login_page_ui._PRIVACY_POLICY) is not None

    def test_terms_of_service_link_is_clickable(self, login_page_ui):
        assert login_page_ui.find_clickable(login_page_ui._TERMS_OF_SERVICE) is not None


class TestLogin:
    def test_successful_login(self, driver, credentials):
        page = LoginPage(driver)
        page.open()
        page.login(credentials["username"], credentials["password"])
        page.wait_until_logged_in()
        assert "hudl.com/home" in page.url or "app.hudl.com" in page.url

        home = HomePage(driver)
        assert home.get_display_name() != ""
        home.open_user_menu()
        assert home.get_user_email() == credentials["username"]

    def test_login_with_invalid_password(self, driver, credentials):
        page = LoginPage(driver)
        page.open()
        page.login(credentials["username"], "wrongpassword")
        assert page.is_error_displayed()

    def test_login_with_invalid_email(self, driver, credentials):
        page = LoginPage(driver)
        page.open()
        page.login("notareal@email.com", credentials["password"])
        assert page.is_error_displayed()

    def test_login_with_empty_credentials(self, driver):
        page = LoginPage(driver)
        page.open()
        page.submit_username("")
        assert page.is_error_displayed()
