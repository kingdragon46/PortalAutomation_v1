from http.server import executable
import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.chrome.options import Options
from WebConfig.web_config import TestData
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.utils import ChromeType


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    options = Options()
    options.set_capability("loggingPrefs", {'performance': 'ALL'})
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument("enable-automation")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--dns-prefetch-disable")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--incognito')
    # options.add_argument('--headless')
    options.add_argument("--allow-insecure-localhost")
    options.add_argument('--start-maximized')
    # options.add_argument('--window-size=1280,800')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    if request.param == "chrome":
        # web_driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=options)
 
       web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(100)
    yield 
    print("\nteardown")
    web_driver.close()