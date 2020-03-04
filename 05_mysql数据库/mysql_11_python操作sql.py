#coding:utf-8

from pymysql import *


def main():
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, user='root', password='mysql', database='jingdong', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()
    # 执行select语句,并返回受影响的行数：查询一条数据
    count = cs1.execute('select * from goods;')
    # 打印受影响的行数
    print(count)

    for i in range(count):
        # 获取查询的结果
        result = cs1.fetchone() # 查询一条数据
        print(result)

    # cs1.fetchmany(m) # 最多查询m条
    # cs1.fetchall() # 查询所有

    cs1.close()
    conn.close()




if __name__ == "__main__":
    main()
