import json
import datetime
import pymysql
import logging
class DB:
    pymysqlObj = None
    query = None
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    def __init__(self, id = -1):
        DB.pymysqlObj = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            db="security",
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor

        )
        if(id == -1):
            DB.query = "SELECT * FROM products"
        else:
            DB.query = "SELECT * FROM products WHERE id = {}".format(id)

    def setQueryGetAll(self):
        DB.query = "SELECT * FROM products"

    def getPySQL(self):
        try:
            with DB.pymysqlObj.cursor() as cursor:
                cursor.execute(DB.query)
                result = cursor.fetchall()
        finally:
            DB.pymysqlObj.close()
        return result

    def convertToJSON(self, aList):
        return json.dumps(aList, default=self.datetime_handler)

    def datetime_handler(self, x):
        if isinstance(x, datetime.datetime):
            return x.isoformat()
        raise TypeError("Unknown type")

obj = DB(44)
print obj.getPySQL()

def lambda_handler(event, context):
    obj = DB(event.id)
    return obj.getPySQL()
