# coding=utf-8
from web_tester.common.const import USER1, PASSWORD1
from web_tester.common.base import *
from selenium.webdriver.common.by import By
from web_tester.common.base import BasePage


class Loginpage(BasePage):

    username = (By.XPATH, '//*[@id="app"]/div[2]/div/div/div[3]/div[2]/div[1]/div[3]/div/input')
    password = (By.XPATH, '//*[@id="app"]/div[2]/div/div/div[3]/div[2]/div[2]/div[2]/div/input')
    tongyi_btn = (By.XPATH,'//*[@id="app"]/div[2]/div/div/div[3]/div[3]/div/div/div[1]/label/span[1]/span')
    login_btn = (By.XPATH, '//*[@id="app"]/div[2]/div/div/div[3]/div[3]/button')
    cfg_btn = (By.XPATH,'//*[@id="app"]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]')


    def login(self):
        logging.info(f"-----------测试用例执行步骤-----------")
        self.input_text(Loginpage.username, text=USER1, clear=2, doc="用户名")
        self.input_text(Loginpage.password, text=PASSWORD1, doc="密码")
        self.click_element(Loginpage.tongyi_btn, doc="同意按钮")
        self.click_element(Loginpage.login_btn, doc="登陆按钮")
        self.click_element(Loginpage.cfg_btn, doc="创富港企业按钮")

