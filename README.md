# PytestAutoTestFrameWork
    结构说明：
        1.pom设计模式 
        2.selenium+pytest+Chrome+htmlreport
    框架优点:
        1.提高测试脚本的可读性
        2.提高代码复用性，减少代码的重复
        3.提高测试用例的可维护性，特别是针对UI变动频繁的项目
        4.可拓展性强，pytest可结合requests、appium，Jenkins等完成其他的测试需求
    框架缺点:
        1.基于流程进行了模块化的拆分，所以结构会稍复杂
    环境需求：
        1.依赖相关:requirements.txt
        2.需安装python 3++以上版本
        3.需安装selenium 2++以上版本
        4.需安装火狐或谷歌浏览器及对应驱动
        5.需对发送测试报告邮件的邮箱正确配置
    运行项目：
        1.统一运行入口: run.py
    修改说明：
        1.None
