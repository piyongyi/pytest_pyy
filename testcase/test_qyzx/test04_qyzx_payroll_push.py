import pytest
from web_tester.pages.qyzx_pages.payroll_push_page import Pushpage


class Testpush:

    def test_01(self, qyzx_login_driver):
        """推送工资条功能测试"""
        page = Pushpage(qyzx_login_driver)
        page.Pushgzt()
        assert page.push_ok() == "推送成功"


if __name__ == '__main__':
    pytest.main()
