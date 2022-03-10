# coding=utf-8
from web_tester.common.const import USER1, PASSWORD1
from web_tester.common.base import *
from selenium.webdriver.common.by import By
from web_tester.common.base import BasePage


class gwpage(BasePage):

    fyj_logo_btn = (By.XPATH, '//*[@id="hd"]/div/div/div/div[1]/a/img')
    sy_btn = (By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul/li[1]/a')
    swhz_btn = (By.XPATH,'//*[@id="bs-example-navbar-collapse-1"]/ul/li[2]/a')
    jrwm_btn = (By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul/li[3]/a')
    gywm_btn = (By.XPATH,'//*[@id="bs-example-navbar-collapse-1"]/ul/li[4]/a')
    qyzx_btn = (By.ID, 'companycenter')
    bzwd_btn = (By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/div/a[2]')
    assert_t1 = (By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/p")

    def gwzy(self):
        logging.info(f"-----------测试用例执行步骤-----------")
        self.click_element(gwpage.fyj_logo_btn, doc="点击方圆间logo")
        self.click_element(gwpage.sy_btn,  doc="点击首页按钮")
        self.click_element(gwpage.swhz_btn, doc="点击商务合作按钮")
        self.click_element(gwpage.jrwm_btn, doc="点击加入我们按钮")
        self.click_element(gwpage.gywm_btn, doc="点击关于我们按钮")

    def assert_ok1(self):
        return self.assert_text(gwpage.assert_t1)

    def gw_qyzx(self):
        logging.info(f"-----------测试用例执行步骤-----------")
        self.click_element(gwpage.qyzx_btn, doc="点击企业中心按钮")


    def gw_help(self):
        logging.info(f"-----------测试用例执行步骤-----------")
        self.click_element(gwpage.bzwd_btn, doc="点击帮助文档按钮")

