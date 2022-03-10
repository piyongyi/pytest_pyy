from selenium.webdriver.common.by import By
from web_tester.common.const import SALARY_PATH
from web_tester.common.base import *


class Pushpage(BasePage):
    yingyong_btn = (By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[1]/div[3]/a")
    gzt_push_btn = (By.ID,'143')
    push_gzt_btn = (By.XPATH,'//*[@id="app"]/div[2]/div/div[1]/button')
    upload_btn =(By.XPATH,'//*[@id=\"app\"]/div[2]/div/div[2]/div[2]/div[2]/div/div/input')
    dr_btn = (By.XPATH,"//*[@id=\"app\"]/div[2]/div/div[2]/div[3]/button[2]")
    ljpush_btn = (By.XPATH,"//*[@id=\"app\"]/div[2]/div/div[1]/div[2]/button[1]")
    assert_t = (By.XPATH, "/html/body/div[2]/p")


    def Pushgzt(self):
        logging.info(f"-----------测试用例执行步骤-----------")
        self.click_element(Pushpage.yingyong_btn, doc="应用按钮")
        self.click_element(Pushpage.gzt_push_btn, doc="工资条推送应用")
        self.click_element(Pushpage.push_gzt_btn, doc="推送工资条按钮")
        self.input_text(Pushpage.upload_btn, text=SALARY_PATH, doc="上传推送工资表格")
        self.click_element(Pushpage.dr_btn, doc="导入按钮")
        time.sleep(3)
        self.click_element(Pushpage.ljpush_btn, doc="立即推送按钮")


    def push_ok(self):
        return self.assert_text(Pushpage.assert_t)