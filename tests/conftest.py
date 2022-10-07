import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox', choices=["chrome", "firefox"])
    parser.addoption('--executor', action='store', default='192.168.1.230')
    parser.addoption('--br_version', action='store', default='')


@pytest.fixture
def get_webdriver(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption('--executor')
    br_version = request.config.getoption('--br_version')
    caps = {
        "browserName": browser,
        "browserVersion": br_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }
    driver = webdriver.Remote(
        command_executor=f'http://{executor}:4444/wd/hub',
        desired_capabilities=caps,
    )
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://ostore.kg/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()
