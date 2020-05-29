from datetime import date
from django.conf import settings
from django.shortcuts import render, redirect
from booktest.models import BookInfo, AreaInfo, PicTest
from django.http import HttpResponse, HttpResponseRedirect, HttpResponse, JsonResponse
import datetime
from django.http.response import JsonResponse
from django.template import loader, RequestContext
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO


def login_required(view_func):
    '''登陆判断装饰器'''
    def wrapper(request, *view_args, **view_kwargs):
        # 判断用户是否登陆
        if request.session.has_key('islogin'):
            # 用户已登陆
            return view_func(request, *view_args, **view_kwargs)
        else:
            # 用户未登录，跳转到登录页
            return redirect('/login')
    return wrapper


def my_render(request, template_path, context={}):
    # 1. 加载模板文件，获取一个模板对象
    temp = loader.get_template(template_path)
    # 2. 定义模板上下文，给模板文件传数据
    context1 = context
    # 3. 模板渲染， 产生一个替换后的html内容
    res_html = temp.render(context1)
    # 4. 返回应答
    return HttpResponse(res_html)


# Create your views here.
def index3(request):
    #return my_render(request, 'booktest/index3.html')
    return render(request, 'booktest/index3.html')


#def index4(request):
#    return render(request, 'booktest/index4.html')

def index1(request):
    '''显示图书信息'''
    # 查询出所有的图书信息
    books = BookInfo.objects.all()
    # 使用模板
    return render(request, 'booktest/index1.html', {'books':books})


def create(request):
    '''新增一本书'''
    # 1. 创建BookInfo对象
    b = BookInfo()
    b.btitle = '流星蝴蝶剑'
    b.bpub_date = date(1990, 1, 1)
    # 2. 保存到数据库
    b.save()
    # 3. 返回应答，让浏览器再访问/index, 重定向
    #return HttpResponse('ok')
    #return HttpResponseRedirect('/index')
    return redirect('/index')


def delete(request, bid):
    '''删除点击的图书'''
    # 1. 通过bid获取要删除的图书
    book = BookInfo.objects.get(id=bid)
    # 2. 删除
    book.delete()

    # 3. 重定向
    # return HttpResponseRedirect('/index')
    return redirect('/index')


# def areas(request):
#     '''查询广州市对应的父级和子级地区'''
#     # 1. 查询广州市的信息
#     area = AreaInfo.objects.get(atitle='广州市')
#     # 2. 查询广州市的上级地区
#     parent = area.aparent
#     # 3. 查询广州市的下级地区
#     children = area.areainfo_set.all()
#     # 使用模板
#     return render(request, 'booktest/areas.html', {'area':area, 'parent':parent, 'children':children})


def index2(request):
    return render(request, 'booktest/index2.html')


def show_args(request, num):
    return HttpResponse(num)


def login(request):
    '''显示登录页面'''
    if request.session.has_key('islogin'):
        # 用户已登录，跳转到首页
        return redirect('/change_pwd')
    else:
        # 用户未登录
        # 获取cookie username
        if 'username' in request.COOKIES:
            # 获取记住的用户名
            username = request.COOKIES['username']
        else:
            username = ''

        return render(request, 'booktest/login.html')


def login_check(request):
    '''登录校验'''
    # request.POST 保存的是post方式提交的参数
    # request.GET 保存的是get方式提交的参数 -- QueryDict
    # 1. 获取提交的用户数据
    # print(request.method)
    # print(request.path)
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    # 2. 进行登录的校验
    if username == 'admin' and password == '123456':
        # 用户名密码正确，跳转到首页
        response = redirect('/change_pwd')
        # 判断是否需要记住用户名
        if remember == 'on':
            # 设置cookie username过期时间
            response.set_cookie('username', username, max_age=7*24*3600)
        # 记住用户登录状态
        # 只有session中有islogin，就认为用户已登录
        request.session['islogin'] = True
        # 记住登陆的用户名
        request.session['username'] = username
        # 用户名密码正确, 跳转到首页
        # return  redirect('/index')
        # 返回应答
        return response
    else:
        # 用户名密码不正确，跳转到登录页面
        return redirect('/login')


@login_required
def change_pwd(request):
    return render(request, 'booktest/change_pwd.html')


@login_required
def change_pwd_action(request):
    # 1. 获取新密码
    pwd = request.POST.get('pwd')
    username = request.session.get('username')
    return HttpResponse("%s修改密码为%s" %(username, pwd))


def ajax_test(request):
    '''显示ajax页面'''
    return render(request, 'booktest/test_ajax.html')


def ajax_handle(request):
    '''ajax处理'''
    # 返回的json数据
    return JsonResponse({'res':1})


def set_cookie(request):
    '''设置cookie信息'''
    response = HttpResponse('设置cookie')
    # 设置一个cookie信息，名字为num, 值为1
    # 两种方法设置cookie过期时间
    response.set_cookie('num', 1, max_age=14*24*3600)
    # response.set_cookie('num', 1, expires=datetime.now()+timedelta(days=14))
    # 返回response
    return response


def get_cookie(request):
    '''获取cookie信息'''
    # 取出cookie num的值
    num = request.COOKIES['num']
    return HttpResponse(num)


# def set_session(request):
#     '''设置session'''
#     request.session['username'] = 'smart'
#     request.session['age'] = 18
#     return HttpResponse('设置成功')
#
#
# def get_session(request):
#     '''获取session'''
#     username = request.session['username']
#     age = request.session['age']
#     return HttpResponse(username + ':' + str(age))


def clear_session(request):
    '''清除session'''
    # request.session.clear() # 清除session中的数据
    request.session.flush()
    return HttpResponse('清除成功')


def temp_var(request):
    my_dict = {'title': '字典键值'}
    my_list = [1, 2, 3]
    book = BookInfo.objects.get(id = 1)
    context = {'my_dict':my_dict, 'my_list':my_list, 'book':book}
    return render(request, 'booktest/temp_var.html', context)


def temp_tags(request):
    books = BookInfo.objects.all()
    return render(request, 'booktest/temp_tags.html', {'books':books})


def child(request):
    return render(request, 'booktest/child.html')


def html_escape(request):
    '''html转义'''
    return render(request, 'booktest/html_escape.html', {'content': '<h1>hello</h1>'})


# 验证码
def verify_code(request):
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('FreeMono.ttf', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'images/png')


def url_reverse(request):
    return render(request, 'booktest/url_reverse.html')


# def show_args(request, a, b):
#     return HttpResponse(a + ':' + b)


# def show_kwargs(request, c, d):
 #   return HttpResponse(c + ':' + d)

EXCLUDE_IPS = ['192.168.0.101']
def blocked_ips(view_func):
    def wrapper(request, *view_args, **view_kwargs):
        # 获取浏览器端的ip地址
        user_ip = request.META['REMOTE_ADDR']
        print(user_ip)
        if user_ip in EXCLUDE_IPS:
            return HttpResponse("<h1>Forbidden</h1>")
        else:
            return view_func(request, *view_args, **view_kwargs)
    return wrapper


#@blocked_ips
def static_test(request):
    return render(request, 'booktest/static_test.html')
    # print(settings.STATICFILES_FINDERS)


#@blocked_ips
def index(request):
    return render(request, 'booktest/index.html')


def upload_pic(request):
    '''显示上传图片页面'''
    return render(request, 'booktest/upload_pic.html')


def upload_handle(request):
    '''上传图片处理'''
    # 1. 获取上传文件的处理对象
    pic = request.FILES['pic']

    # 2. 创建一个文件
    save_path = '%s/booktest/%s'%(settings.MEDIA_ROOT, pic.name)
    # 3. 获取上传文件的内容并写到创建的文件中
    with open(save_path, 'wb') as f:
        for content in pic.chunks():
            f.write(content)

    # 4. 在数据库中保存上传记录
    PicTest.objects.create(goods_pic='booktest/%s'%pic.name)

    # 5. 返回
    return HttpResponse('ok')


from django.core.paginator import Paginator
# 前端使用时需要传递页码
def show_area(request, pindex):
    '''分页'''
    # 1. 查询出所有省级地区的信息
    areas = AreaInfo.objects.filter(aparent__isnull = True)

    # 2. 分页，每页显示10条
    paginator = Paginator(areas, 10)
    # print(paginator.num_pages)
    # print(paginator.page_range)

    # 3. 获取第pindex页的内容
    if pindex == '':
        pindex = 1
    else:
        pindex = int(pindex)
    # page是Page类的实例对象
    page = paginator.page(pindex)
    # print(page.number)

    return render(request, 'booktest/show_area.html', {'page':page})


def areas(request):
    '''省市县选择案例'''
    return render(request, 'booktest/areas.html')


def prov(request):
    '''获取所有省级地区的信息'''
    # 1. 获取所有省级地区的信息
    areas = AreaInfo.objects.filter(aparent__isnull=True)

    # 2. 拼接出json数据
    areas_list = []
    for area in areas:
        areas_list.append((area.id, area.atitle))

    # 3. 返回数据
    return JsonResponse({'data':areas_list})


def city(request, pid):
    '''获取pid对应地区的下级地区'''
    # 1. 获取pid对应地区的下级地区
    # AreaInfo.objects.get(id=pid)
    areas = AreaInfo.objects.filter(aparent__id=pid)

    # 2. 遍历areas并拼接出json数据：atitle id
    areas_list = []
    for area in areas:
        areas_list.append((area.id, area.atitle))

    # 3. 返回数据
    return JsonResponse({'data':areas_list})


def set_session(request):
    '''设置session'''
    request.session['name'] = 'itheima'
    request.session['age'] = 18
    return HttpResponse('设置session')


def get_session(request):
    '''获取session'''
    username = request.session['name']
    age = request.session['age']
    return HttpResponse(username + ':' + age)