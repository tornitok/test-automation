import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages import CheckValidate, IndexPage
from config import URL

@pytest.fixture
def get_chrome_options():
    options = Options()
    options.add_argument('--headless')
    return options


@pytest.fixture
def get_web_driver(get_chrome_options):
    driver = webdriver.Chrome(
        options=get_chrome_options,
        service=Service(
            ChromeDriverManager().install()
        )
    )
    return driver

@pytest.fixture
def index_page(get_web_driver):
    get_web_driver.get(URL.BASE_URL)
    yield IndexPage(get_web_driver)
    get_web_driver.quit()

@pytest.fixture
def check_and_validate_page(get_web_driver):
    get_web_driver.get(URL.CHECK_AND_VALIDATE)
    yield CheckValidate(get_web_driver)
    get_web_driver.quit()