import pymysql.connections
import pymysql.cursors
MYSQL_HOSTS = "127.0.0.1"
MYSQL_USER = "root"
MYSQL_PASSWORD = "fengfei"
MYSQL_PORT = 3306
MYSQL_DB = "JD_test"

connect = pymysql.Connect(
    host = MYSQL_HOSTS,
    port = MYSQL_PORT,
    user = MYSQL_USER,
    passwd = MYSQL_PASSWORD,
    database = MYSQL_DB,
    charset="utf8"
)

cursor = connect.cursor()
# # 插入数据
class Sql:

    @classmethod
    def insert_JD_name(cls,id, name, shop_name, price, link,
                               comment_num ,score1count, score2count, score3count, score4count, score5count):
        sql = "INSERT INTO jd_name (good_id, name, comment, shop_name, price, link ,score1count, score2count," \
              " score3count, score4count, score5count) VALUES ( %(id)s, %(name)s, %(comment_num)s, %(shop_name)s, %(price)s" \
              ", %(link)s,  %(score1count)s, %(score2count)s, %(score3count)s, %(score4count)s, %(score5count)s )"
        value = {
            'id' : id,
            'name' : name,
            'comment' : comment_num,
            'shop_name' : shop_name,
            'price' : price,
            'link' : link,
            'comment_num' : comment_num,
            'score1count' : score1count,
            'score2count' : score2count,
            'score3count' : score3count,
            'score4count' : score4count,
            'score5count' : score5count,
        }
        cursor.execute(sql, value)
        connect.commit()
        # print('成功插入', cursor.rowcount, '条数据')
