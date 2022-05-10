from http.server import executable
import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.chrome.options import Options
from WebConfig.web_config import TestData
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    caps = DesiredCapabilities.CHROME
    caps['goog:loggingPrefs'] = {'performance': 'ALL'}
    options = Options()
    options.add_argument('--incognito')
    # options.add_argument('--headless')
    options.add_argument('--start-maximized')
    if request.param == "chrome":
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options, desired_capabilities=caps)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(100)
    yield 
    web_driver.close()



# #Test arguments
# @pytest.fixture
# def email_pytest_report(request):
#     "pytest fixture for device flag"
#     return request.config.getoption("--email_pytest_report")
 
# #Command line options:
# parser.addoption("--email_pytest_report",
# dest="email_pytest_report",
# help="Email pytest report: Y or N",
# default="N")
 
# def pytest_terminal_summary(terminalreporter, exitstatus):
#     "add additional section in terminal summary reporting."
#     if not hasattr(terminalreporter.config, 'workerinput'):
#         if terminalreporter.config.getoption("--email_pytest_report").lower() == 'y':
#             #Initialize the Email_Pytest_Report object
#             email_obj = Email_Pytest_Report()
#             # Send html formatted email body message with pytest report as an attachment
#             email_obj.send_test_report_email(html_body_flag=True,attachment_flag=True,report_file_path= 'default')