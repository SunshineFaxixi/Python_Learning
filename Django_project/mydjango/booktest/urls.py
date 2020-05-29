from django.urls import include, path
from booktest import views

urlpatterns = [
    path('index1', views.index1),
    path('index2', views.index2),
    path('index3', views.index3),
    #path('index4', views.index4),
    path('showargs<num>', views.show_args),
    path('create', views.create),
    path('delete<\d+>', views.delete),
    # path('areas', views.areas),
    path('login', views.login),
    path('login_check', views.login_check),
    path('test_ajax', views.ajax_test),
    path('ajax_handle', views.ajax_handle),
    path('set_cookie', views.set_cookie),
    path('get_cookie', views.get_cookie),
    path('set_session', views.set_session),
    path('get_session', views.get_session),
    path('clear_session', views.clear_session),
    path('temp_var', views.temp_var),
    path('temp_tags', views.temp_tags),
    path('child', views.child),
    path('html_escape', views.html_escape),
    path('change_pwd', views.change_pwd),
    path('change_pwd_action', views.change_pwd_action),
    path('verify_code', views.verify_code),
    path('url_reverse', views.url_reverse),
    # path('show_args/<a>/<b>', views.show_args, name='show_args'), # 捕获位置参数
    # path('show_kwargs/<c>/<d>', views.show_kwargs, name='show_kwargs'),
    path('static_test', views.static_test),
    path('index', views.index),
    # path('scd', views.scd),
    path('upload_pic', views.upload_pic),
    path('upload_handle', views.upload_handle),
    path('show_area<pindex>', views.show_area),
    path('areas', views.areas),
    path('prov', views.prov), # 获取所有省级地区的信息
    path('city<pid>', views.city), # 获取省下面的市的信息
    path('dis<pid>', views.city), # 获取市下面的县的信息
    path('set_session', views.set_session), # 设置session
    path('get_session', views.get_session),
]
