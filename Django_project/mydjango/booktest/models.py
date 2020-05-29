from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
class GoodsTest(models.Model):
    """测试模型类"""
    STATUS_CHOICES = (
        (0, '下架'),
        (1, '上架')
    )
    status = models.SmallIntegerField(default=1, choices=STATUS_CHOICES, verbose_name='商品状态')
    detail = UEditorField(verbose_name='商品详情')

    class Meta:
        db_table = 'df_goods_test'
        verbose_name = '商品'
        verbose_name_plural = verbose_name

class BookInfoManager(models.Manager):
    '''图书模型管理器'''
    # 1.改变查询的结果集
    def all(self):
        # 1. 调用父类的all方法，获取所有数据
        books = super().all()
        # 2. 对数据进行过滤
        books = books.filter(is_delete=0)
        # 3. 返回books
        return books

    # 2. 添加其它的方法
    def create_book(self, btitle, bpub_date):
        # 1. 创建一个图书对象
        # 获取self所在模型类的类名
        book = self.model
        # book = BookInfo()
        book.btitle = btitle
        book.bpub_date = bpub_date
        # 2. 保存进数据库
        book.save()
        # 3. 返回
        return book


# 一对多
class BookInfo(models.Model):
    '''图书模型类'''
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False) # 删除标记
    #book = models.Manager() # 自定义一个Manager类对象
    objects = BookInfoManager()

    class Meta:
        db_table = 'bookinfo' # 指定模型类对应的表名


class HeroInfo(models.Model):
    '''英雄人物模型类'''
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=200)
    # 关系属性
    hbook = models.ForeignKey('BookInfo', on_delete=None)
    is_delete = models.BooleanField(default=False)  # 删除标记

    class Meta:
        db_table = 'heroinfo'
'''
class NewsType(models.Model):
    ''新闻类型类''
    # 类型名
    type_name = models.CharField(max_length=128)
    # 关系属性，代表类型下面的新闻
    type_news = models.ManyToManyField('NewsInfo')

class NewsInfo(models.Model):
    ''新闻内容类''
    # 新闻标题
    title = models.CharField(max_length=128)
    # 创建时间
    pub_date = models.DateTimeField(auto_now_add=True)
    # 新闻内容
    content = models.TextField()
    # 关系属性，代表信息所属的类型
    # news_type = models.ManyToManyField('NewsType')

# 一对一
class EmployeeBasicInfo(models.Model):
    ''员工基本信息类''
    # 姓名
    name = models.CharField(max_length=20)
    # 年龄
    age = models.IntegerField()
    # 性别
    gender = models.BooleanField(default=False)
    # 关系属性，代表员工详细信息
    # employee_detail = models.OneToOneField('EmployeeDetailInfo')

class EmployeeDetailInfo(models.Model):
    ''员工详细信息类''
    # 联系方式
    addr = models.CharField(max_length=256)
    # 教育经历
    # 关系属性, 代表员工基本信息
    employee_basic = models.OneToOneField('EmployeeBasicInfo')
'''

class AreaInfo(models.Model):
    '''地区模型类'''
    # 地区名称
    atitle = models.CharField(max_length=120)
    # 关系属性，代表父级地区
    aparent = models.ForeignKey('self', null=True, blank=True, on_delete=None)

    def __str__(self):
        return self.atitle

    def title(self):
        return self.atitle

    def parent(self):
        if self.aparent is None:
            return ''
        return self.aparent.atitle

    title.admin_order_field = 'atitle'
    title.short_description = '地区名称'
    title.short_description = '父级地区名称'


class PicTest(models.Model):
    '''上传图片'''
    goods_pic = models.ImageField(upload_to='booktest')

