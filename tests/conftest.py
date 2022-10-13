import pytest
from selenium import webdriver
import json


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox', choices=["chrome", "firefox"])
    parser.addoption('--executor', action='store', default='192.168.1.230')
    parser.addoption('--br_version', action='store', default='')


@pytest.fixture
def get_webdriver(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption('--executor')
    br_version = request.config.getoption('--br_version')
    capabilities = {
        "browserName": browser,
        "browserVersion": br_version,
        "selenoid:options": {
            "enableVNC": False,
            "enableVideo": False
        }
    }
    driver = webdriver.Remote(
        command_executor=f'http://{executor}:4444/wd/hub',
        desired_capabilities=capabilities
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


@pytest.fixture(autouse=True)
def create_allure_env():
    environment = ['Browser=Firefox\n', 'Mozilla=Firefox 105.0.3\n', 'Stand=Test\n', 'python.Version=3.8.10\n']
    with open('allure/environment.properties', 'w+') as outfile:
        for listitem in environment:
            outfile.write(listitem)


@pytest.fixture
def create_allure_category():
    category = [{
        "name": "Skipped tests",
        "messageRegex": ".*",
        "matchedStatuses": ["skipped"]
        },
        {
        "name": "Element not found",
        "traceRegex": ".*NoSuchElementError.*",
        "matchedStatuses": ["failed"]
        },
        {
        "name": "Broken tests",
        "traceRegex": "Error.*",
        "matchedStatuses": ["failed"]
        },
        {
        "name": "Test defect",
        "messageRegex": ".*Expected is not a String or a RegExp.*",
        "matchedStatuses": ["failed"]
        },
        {
        "name": "Product defect",
        "traceRegex": ".*Failed expectation.*",
        "matchedStatuses": ["failed"]
        },
        {
        "name": "Passed tests",
        "matchedStatuses": ["passed"]
        }]
    with open('allure/category.json', 'w') as outfile:
        json.dump(category, outfile)
