import os, re
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
from web_tester.common.const import FROM_ADDR, TO_ADDRS, SMTP_PORT, SMTP_SERVER, AUTHORIZATION_CODE


def connect():
    from_addr = FROM_ADDR
    authorization_code = AUTHORIZATION_CODE
    smtp_server = SMTP_SERVER
    smtp_port = SMTP_PORT
    # 配置服务器
    smtp = smtplib.SMTP_SSL(smtp_server, smtp_port)
    smtp.login(from_addr, authorization_code)
    return smtp


def send_file(file_new):
    from_addr = FROM_ADDR
    to_addrs = TO_ADDRS
    smtp = connect()
    subject = '自动化测试报告'  #邮件标题
    message = MIMEMultipart()
    message['From'] = formataddr(["FYJ test team", from_addr])
    message['To'] = to_addrs  # 收件人
    message['Subject'] = Header(subject, 'utf-8')
    message.attach(MIMEText('附件为测试报告，系统邮件，请勿回复！', 'plain', 'utf-8'))  # 邮件正文内容

    # 增加HTML附件
    atthtml = MIMEText(open(file_new, 'rb').read(), 'base64', 'utf-8')  # 文件放在同一路径，不放在同一路径改一下比如'D:\\test\\report.html
    atthtml["Content-Type"] = 'application/octet-stream'
    atthtml["Content-Disposition"] = 'attachment;filename = "{file_new}"'.format(file_new=file_new)
    message.attach(atthtml)
    try:
        smtp.sendmail(from_addr, to_addrs.split(','), message.as_string())  # 发送邮件,split分割后产生列表
    except Exception as e:
        print('邮件发送失败!' + str(e))
    print('邮件发送成功！')


def sendreport():
    result_dir = u"../web_tester/report/"
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "/" + fn)
    if not os.path.isdir(result_dir + "/" + fn) else 0)
    # 找到最新生成的文件
    file_new = os.path.join(result_dir, lists[-1])
    print(u'最新生成的测试报告:', file_new)
    send_file(file_new)


def Sandemail():
    """If there is a failed use case, send an email"""
    f = open("../web_tester/report/report.html", "r", encoding="utf-8").read()
    table = re.findall(r'<table id="results-table"(.*?)</table>', f, re.S)  # 查找html中table中的内容
    table1 = str(table)
    if table1.find("Failed") != -1:
        print("有用例测试失败了，请打开邮件查看！")
        sendreport()
    else:
        print("测试完成，详情请看report！")


if __name__ == '__main__':
    pass
