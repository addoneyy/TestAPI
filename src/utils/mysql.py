import pymysql
import traceback
from src.utils.yamlloader import YamlLoader

DBCONFIG = YamlLoader().load(r"conf/mysql.yaml")["product"]

class MysqlClient:

    def query(self, sql):
        """"
            查询
        """
        db = pymysql.connect(**DBCONFIG)
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            query_result = cursor.fetchall()
            return query_result
        except:
            traceback.print_exc()
            cursor.close()
            db.close()

    def commit(self, sql):
        """"
            修改
        """
        db = pymysql.connect(**DBCONFIG)
        cursor = db.cursor()
        try:
            res = cursor.execute(sql)
            db.commit()
            return True if res else False
        except:
            traceback.print_exc()
            db.rollback()
            cursor.close()
            db.close()
            return False