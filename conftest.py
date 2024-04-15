import pytest
from selenium import webdriver
import requests


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def api_client():
    return requests.Session()
