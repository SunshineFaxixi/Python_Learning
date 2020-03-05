# coding:utf-8
from pymysql import connect


class JD(object):
    def __init__(self): 
        # 创建connection连接
        self.conn = connect(host='localhost', port=3306, user='root', password='mysql', database='jingdong', charset='utf8')
        # 获得Cursor对象
        self.cursor = self.conn.cursor()

    def __del__(self):  
        # 关闭Cursor对象
        self.cursor.close()
        # 关闭连接
        self.conn.close()
    
    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_items(self):
        """显示所有的商品"""
        # 执行select语句
        sql = "select * from goods;"
        self.execute_sql(sql)

    def show_cates(self):
        """显示所有的商品"""
        # 执行select语句
        sql = "select name from goods_cates;"
        self.execute_sql(sql)

    def add_cates(self, add_item):
        """添加商品种类"""
        # add_item = input("请输入要添加的商品种类:")
        sql = """insert into goods_cates (name) values ("%s")""" % add_item
        self.cursor.execute(sql)
        self.conn.commit()

    def get_info_by_name(self):
        find_name = input("请输入要查询的商品的名字:")
        # sql = """select * from goods where name = '%s'""" % find_name
        # print("----------->%s<-----------")
        # self.execute_sql(sql)
        sql = "select * from goods where name=%s"
        self.cursor.execute(sql, [find_name])
        print(self.cursor.fetchall())

    @staticmethod
    def print_temp(): 
        print("------京东商城--------")
        print("------显示所有商品-----")
        print("------显示所有商品分类-----")
        print("------添加商品种类-------")
        print("------根据名字查询一个商品-------")
        return input("请输入选择序号：")

    def run(self):
        while True:
            num = self.print_temp()
            if num == 1:
                self.show_all_items()
            elif num == 2:
                self.show_cates()
            elif num == 3:
                add_item = input("请输入添加的商品种类：")
                self.add_cates(add_item)
            elif num == 4:
                self.get_info_by_name()
            else:
                print("输入有误，请重新输入---")

def main():
    # 创建对象
    jd = JD()

    # 调用run方法
    jd.run()


if __name__ == "__main__":
    main()
