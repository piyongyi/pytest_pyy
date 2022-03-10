import pytest
from web_tester.pages.qyzx_pages.qkl_invoice_page import Qklpage


class Testqklfp:

    def test_01(self, qyzx_login_driver):
        """区块链发票开票功能测试"""
        page = Qklpage(qyzx_login_driver)
        page.invoicetest()
        assert page.ok() == "开票11"


if __name__ == '__main__':
    pytest.main()
