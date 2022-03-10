import time
import pytest
from web_tester.pages.gwang_pages.fyj_gwang_page import gwpage


class Testwg:


    def test_01(self,guanwang_driver):
        """官网跳转到企业中心功能测试"""
        page = gwpage(guanwang_driver)
        page.gw_qyzx()
        time.sleep(1)
        guanwang_driver.switch_to.window(guanwang_driver.window_handles[1])
        assert guanwang_driver.title == "企业中心"

    def test_02(self,guanwang_driver):
        """官网跳转到帮助中心功能测试"""
        page = gwpage(guanwang_driver)
        time.sleep(1)
        page.close_switch(1)
        page.gw_help()
        time.sleep(1)
        guanwang_driver.switch_to.window(guanwang_driver.window_handles[1])
        time.sleep(1)
        assert guanwang_driver.title == "方圆间平台帮助手册 · 方圆间"

    def test_03(self,guanwang_driver):
        """首页，fyjlogo,商务合作，加入我们，关于我们等页面加载测试"""
        page = gwpage(guanwang_driver)
        time.sleep(1)
        page.close_switch(1)
        page.gwzy()
        time.sleep(1)
        assert page.assert_ok1() == "我们只追求服务好每一家企业，成为他们坚实的后盾111"

if __name__ == '__main__':
    pytest.main()
