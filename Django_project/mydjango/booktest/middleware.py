from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class BlockedIPSMiddleware(MiddlewareMixin):
    '''中间件类'''
    # EXCLUDE_IPS = ['192.168.0.104']
    EXCLUDE_IPS = []
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        '''视图函数调用之前会调用'''
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in BlockedIPSMiddleware.EXCLUDE_IPS:
            return HttpResponse("<h1>Forbidden</h1>")

"""
class TestMiddleware(MiddlewareMixin):
    '''中间件类'''
    def __init__(self, request):
        '''服务器重启之后，接收第一个请求时调用'''
        print("----init----")

    def process_request(self, request):
        '''产生request之后，url匹配之前调用'''
        print("----process_request----")

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        '''url匹配之后，视图函数调用之前调用'''
        print("----process_view----")

    def get_response(self, request):
        '''视图函数调用之后，内容返回浏览器之前'''
        print("----process_response----")
        # return response
"""

















