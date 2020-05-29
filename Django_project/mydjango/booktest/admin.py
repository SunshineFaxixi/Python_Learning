from django.contrib import admin
from booktest.models import GoodsTest, AreaInfo, PicTest


class AreaStackedInline(admin.StackedInline):
    # 写多类的名字
    model = AreaInfo
    extra = 2


class AreaTabularInline(admin.TabularInline):
    model = AreaInfo
    extra = 2


class AreaInfoAdmin(admin.ModelAdmin):
    '''地区模型管理类'''
    list_per_page = 10 # 每页显示10条
    list_display = ['id', 'atitle', 'title', 'parent'] # 可以显示模型类的属性和方法
    actions_on_bottom = True
    actions_on_top = False
    list_filter = ['atitle'] # 列表页右侧的过滤栏
    search_fields = ['atitle'] # 列表页上侧的搜索框

    fields = ['aparent', 'atitle'] # 显示编辑页显示字段顺序
    """
    fieldsets={
        ('基本', {'fields':['atitle']}),
        ('高级', {'fields':['aparent']}),
    }
    """

    # inlines = [AreaStackedInline]
    inlines = [AreaTabularInline]

# Register your models here.
admin.site.register(GoodsTest)
admin.site.register(AreaInfo, AreaInfoAdmin)
admin.site.register(PicTest)