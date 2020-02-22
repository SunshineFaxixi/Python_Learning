#coding=utf-8
from hm_02_recv_msg import *
import hm_02_common


def handle_data():
    """模拟处理recv_msg模块接收的数据"""
    print("------>handle_data")
    for i in RECV_DATA_LIST:
        print(i)
    hm_02_common.HANDLE_FLAG = True


def test_handle_data():
    """测试处理是否完成，变量是否设置为True"""
    print("------->test_handle_data")
    if hm_02_common.HANDLE_FLAG:
        print("====已经处理完成====")
    else:
        print("====未处理完成=====")
