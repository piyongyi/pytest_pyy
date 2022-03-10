import datetime
import os
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging


class BasePage:

    def __init__(self,driver):
        self.driver = driver


    # 等待元素存在
    def wait_ele_presence(self, locator, center=True, timeout=15, doc=""):
        try:
            start = datetime.datetime.now()
            ele = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            end = datetime.datetime.now()
            logging.info("{}-元素{}已存在，等待{}秒".format(doc, locator, (end - start).seconds))
            self.driver.execute_script("arguments[0].scrollIntoViewIfNeeded(arguments[1]);", ele, center)
            return ele
        except:
            logging.exception("{}-元素不存在-{}".format(doc, locator))
            raise


    # 等待元素可见
    def wait_ele_visible(self, locator, center=True, timeout=15, doc=""):
        self.wait_ele_presence(locator, center, timeout, doc)
        try:
            start = datetime.datetime.now()
            ele = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            logging.info("{}-元素{}已可见，等待{}秒".format(doc, locator, (end - start).seconds))
            return ele
        except:
            logging.exception("{}-元素不可见-{}".format(doc, locator))
            raise

    # 点击操作
    def click_element(self, locator, center=True, mode=1, timeout=15, doc=""):
        ele = self.wait_ele_visible(locator, center, timeout, doc)
        try:
            if mode == 1:
                ele.click()
            if mode == 2:
                self.driver.execute_script("arguments[0].click();", ele)
            if mode == 3:
                ActionChains(self.driver).click(ele).perform()
            logging.info("{}-元素{}点击成功!".format(doc, locator))
        except:
            logging.exception("{}-元素点击失败-{}".format(doc, locator))
            raise

    # 输入操作
    def input_text(self, locator, text, clear="", center=True, timeout=15, doc=""):
        ele = self.wait_ele_presence(locator, center, timeout, doc)
        try:
            if clear == 1:
                ele.clear()
            elif clear ==  2:
                ele.send_keys(Keys.CONTROL, "a")
                ele.send_keys(Keys.DELETE)
            ele.send_keys(text)
            logging.info("{}-元素 {} 输入：{} 成功!".format(doc, locator, text))
        except:
            logging.exception("{}-元素输入失败-{}".format(doc, locator))
            raise

    # 下拉框处理
    def select_ele(self, locator, index=None, text=None, value=None, center=True, timeout=15, doc=""):
        ele = self.wait_ele_visible(locator, center, timeout, doc)
        try:
            if index:
                Select(ele).select_by_index(index)
            if text:
                Select(ele).select_by_visible_text(text)
            if value:
                Select(ele).select_by_value(value)
            logging.info("{}-下拉框元素{}选择：index-{}，text-{}，value-{}".format(doc, locator, index, text, value))
        except:
            logging.exception("{}-元素选择失败-{}".format(doc, locator))
            raise


    # 鼠标悬停
    def hover(self, locator, center=True, timeout=15, doc=""):
        ele = self.wait_ele_presence(locator, center, timeout, doc)
        try:

            ActionChains(self.driver).move_to_element(ele).perform()
            logging.info("{}-元素{}鼠标悬停".format(doc, locator))
        except:
            logging.exception("{}-元素悬停失败-{}".format(doc, locator))
            raise

    # 查找元素
    def get_element(self, locator, doc=""):
        try:
            logging.info("{}-查找元素：{}".format(doc, locator))
            return self.driver.find_element(*locator)
        except:
            logging.exception("{}-元素查找失败-{}".format(doc, locator))
            raise

    # 查找匹配元素
    def get_elements(self, locator, doc=""):
        try:
            logging.info("{}-查找所有匹配的元素：{}".format(doc, locator))
            return self.driver.find_elements(*locator)
        except:
            logging.exception("{}-元素集查找失败-{}".format(doc, locator))
            raise

    # 获取元素的属性
    def get_ele_attribute(self, locator, name, center=True, timeout=15, doc="获取元素的属性"):
        ele = self.wait_ele_presence(locator, center, timeout, doc)
        try:
            value = ele.get_attribute(name)
            logging.info("{}-元素{}的{}属性-{}".format(doc, locator, name, value))
            return value
        except:
            logging.exception("{}-元素获取属性{}失败-{}".format(doc, name, locator))
            raise

    # 获取元素的文本内容
    def get_text(self, locator, center=True, timeout=15, doc="获取元素的文本内容"):
        ele = self.wait_ele_presence(locator, center, timeout, doc)
        try:
            text = ele.text
            logging.info("{}-元素 {} 的文本内容为: {}".format(doc, locator, text))
            return text
        except:
            logging.exception("{}-元素获取文本失败-{}".format(doc, locator))
            raise

    # 获取元素的标签名
    def get_tag_name(self, locator, center=True, timeout=15, doc="获取元素的标签名"):
        ele = self.wait_ele_presence(locator, center, timeout, doc)
        try:
            tag_name = ele.tag_name
            logging.info("{}-元素{}的标签名-{} 成功".format(doc, locator, tag_name))
            return tag_name
        except:
            logging.exception("{}-元素获取标签名失败-{}".format(doc, locator))
            raise

    # iframe处理
    def switch_iframe(self, iframe_reference, timeout=60, doc=""):
        """"""
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, timeout).until(EC.frame_to_be_available_and_switch_to_it(iframe_reference))
            end = datetime.datetime.now()
            logging.info("{}-进入表单，等待{}秒".format(doc, (end - start).seconds))
        except:
            logging.exception("{}-进入表单失败-{}".format(doc, iframe_reference))
            raise

    # 退回上层表单
    def switch_parent_iframe(self, doc="退回上层表单"):
        self.driver.switch_to.parent_frame()
        logging.info(doc)

    # 退回初始表单
    def switch_default_iframe(self, doc="退回初始表单"):
        self.driver.switch_to.default_content()
        logging.info(doc)

    # 刷新页面
    def page_refresh(self, doc="刷新页面"):
        self.driver.refresh()
        # driver.execute_script("location.reload()")
        logging.info(doc)

    def driver_quit(self, doc="关闭浏览器"):
        self.driver.quit()
        # driver.execute_script("location.reload()")
        logging.info(doc)

    # 等待元素出现再消失
    def wait_ele_gone(self, locator, timeout=15, poll_frequency=0.5, doc=""):
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(locator))
            end = datetime.datetime.now()
            logging.info("{}-元素{}已存在，等待{}秒".format(doc, locator, (end - start).seconds))
            WebDriverWait(self.driver, timeout, poll_frequency).until_not(EC.presence_of_element_located(locator))
            end = datetime.datetime.now()
            logging.info("{}-元素{}已消失，等待{}秒".format(doc, locator, (end - start).seconds))
        except:
            logging.exception("{}-元素不消失-{}".format(doc, locator))

    # 断言元素文本包含指定值
    def assert_tt(self, locator, expect_text, center=True, timeout=60, doc=""):
        try:
            text = self.get_text(locator, center, timeout, doc)
            result = expect_text in text
            logging.info("{}-元素{}文本预期为: {}，实际为: {}，用例执行结果为: {}".format(doc, locator, expect_text, text, result))
        except:
            logging.exception("{}-获取文本失败，用例执行失败！！！".format(doc))
            return False

    def assert_text(self, locator, center=True, timeout=60, ):
        text = self.get_text(locator, center, timeout, )
        logging.info("断言文本为: {}".format(text))
        return text


    # 窗口切换
    # 说明：window_handles是获取所有窗口，witch_to.window是切换窗口。n是下坐标，0是第1个，1是第二个，以此类推。
    def switch(self, n):
        self.driver.switch_to.window(self.driver.window_handles[n])

    # 关闭页签
    def close_switch(self, n):
        self.driver.switch_to.window(self.driver.window_handles[n])  # 切换到新页签
        self.driver.close()  # 关闭新页签
        self.driver.switch_to.window(self.driver.window_handles[0])  # 然后切换回原始页签

if __name__ == '__main__':
    pass

