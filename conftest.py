import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox", "safari"],
        help="Browser to run tests against",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode",
    )


@pytest.fixture(scope="session")
def browser_name(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def headless(request):
    return request.config.getoption("--headless")


@pytest.fixture(scope="session")
def credentials():
    return {
        "username": os.environ["HUDL_USERNAME"],
        "password": os.environ["HUDL_PASSWORD"],
    }


def _make_driver(browser_name, headless):
    if browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        d = webdriver.Firefox(options=options)
    elif browser_name == "safari":
        if headless:
            raise ValueError("Safari does not support headless mode")
        # safaridriver ships with macOS — no driver download needed.
        # Enable via: safaridriver --enable (run once in terminal)
        d = webdriver.Safari()
    else:
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        d = webdriver.Chrome(options=options)
    d.implicitly_wait(10)
    d.maximize_window()
    return d


@pytest.fixture
def driver(browser_name, headless):
    d = _make_driver(browser_name, headless)
    yield d
    d.quit()


@pytest.fixture(scope="class")
def class_driver(browser_name, headless):
    d = _make_driver(browser_name, headless)
    yield d
    d.quit()


@pytest.fixture(scope="class")
def login_page_ui(class_driver):
    from pages.login_page import LoginPage
    page = LoginPage(class_driver)
    page.open()
    return page
