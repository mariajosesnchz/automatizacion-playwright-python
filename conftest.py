import pytest
from playwright.sync_api import sync_playwright
from utils.config import HEADLESS

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=HEADLESS,
            slow_mo=1000 if not HEADLESS else 0
        )
        page = browser.new_page()

        yield page

        browser.close()