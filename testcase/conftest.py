from py._xmlgen import html
import pytest
from web_tester.common.const import TEST_LOGIN_URL, OW_URL
from web_tester.pages.qyzx_pages.login_qyzx_page import Loginpage
from web_tester.common.base import *



@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="openPicture(src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")


def capture_screenshot():
    return driver.get_screenshot_as_base64()


# driver = None
# autouse=True
@pytest.fixture(scope='package')
def qyzx_login_driver():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(TEST_LOGIN_URL)
    logging.info(f"开始测试")
    logging.info(f"打开测试地址:{TEST_LOGIN_URL}")
    time.sleep(2)
    page = Loginpage(driver)
    page.login()
    yield driver
    logging.info(f"测试结束")
    driver.quit()


@pytest.fixture(scope='package')
def guanwang_driver():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(OW_URL)
    logging.info(f"开始测试")
    logging.info(f"打开测试地址:{OW_URL}")
    time.sleep(2)
    yield driver
    logging.info(f"测试结束")
    driver.quit()


def pytest_configure(config):
    config._metadata['Browser'] = "Chrome"
    config._metadata["企业中心测试环境"] = "https://test.chuangfuka.com/web/companycenter/#/login"
    config._metadata['方圆间官网正式环境'] = "https://chuangfuka.com/website/fyj/index.html"
    config._metadata.pop("JAVA_HOME")
    config._metadata.pop("Packages")
    config._metadata.pop("Plugins")
    config._metadata.pop("Python")


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("项目名称: web自动化测试v1.1")])
    prefix.extend([html.p("所属部门: 测试组")])
    prefix.extend([html.p("测试人员: 皮永宜")])


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), class_='col-time'))
    cells.pop()
