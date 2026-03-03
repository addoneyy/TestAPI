import yagmail
import traceback
from src.utils.logger import logger

class Mail:


    def __init__(self):
        from  src.utils.yamlloader import YamlLoader
        self.mail_conf = YamlLoader().load(r"conf/mail.yaml")


    def send_mail(self, subject, content, attachments=None):
        """
            发送邮件
        """
        if self.mail_conf["active"]:
            logger.info("开始发送邮件！")
            try:
                yag_mail = yagmail.SMTP(**self.mail_conf["sender"])
                yag_mail.send(to=self.mail_conf["receiver"], subject=subject, contents=content, attachments=attachments)
                logger.success("邮件发送成功！")
                return True
            except:
                logger.error(f"邮件发送失败!\n{traceback.format_exc()}")
                traceback.print_exc()
                return False
        else:
            logger.warning("未启用邮件!")
