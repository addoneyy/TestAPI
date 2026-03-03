import yagmail
import traceback

class Mail:


    def __init__(self):
        from  src.utils.yamlloader import YamlLoader
        self.mail_conf = YamlLoader().load(r"conf/mail.yaml")


    def send_mail(self, subject, content, attachments=None):
        """
            发送邮件
        """
        if self.mail_conf["active"]:
            try:
                yag_mail = yagmail.SMTP(**self.mail_conf["sender"])
                yag_mail.send(to=self.mail_conf["receiver"], subject=subject, contents=content, attachments=attachments)
                return True
            except:
                traceback.print_exc()
                return False
        else:
            print("未启用邮件！")
