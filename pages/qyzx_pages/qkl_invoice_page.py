from selenium.webdriver.common.by import By
from web_tester.common.base import *


class Qklpage(BasePage):
    yingyong_btn = (By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[1]/div[3]/a")
    qklfp_btn = (By.ID,'165')
    assert_t = (By.XPATH, "//*[@id=\"app\"]/div[2]/div/div[1]/form/div/div[1]/div[5]/button/span")

    def invoicetest(self):
        logging.info(f"-----------测试用例执行步骤-----------")
        self.click_element(Qklpage.yingyong_btn, doc="应用按钮")
        self.click_element(Qklpage.qklfp_btn, doc="区块链发票应用")

    def ok(self):
        return self.assert_text(Qklpage.assert_t)