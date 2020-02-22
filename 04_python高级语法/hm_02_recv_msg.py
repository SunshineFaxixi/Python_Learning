#coding=utf-8
from hm_02_common import RECV_DATA_LIST
import hm_02_common


def recv_msg():
    """模拟接收到数据，添加到hm_02_common模块的列表中"""
    print("-------->recv_msg")
    for i in range(5):
        RECV_DATA_LIST.append(i)


def test_recv_data():
    """测试接收到的数据"""
    print("--------->test_recv_data")
    print(RECV_DATA_LIST)

def recv_msg_next():
    """已经处理完数据，再接收另外的其它数据"""
    print("---------->recv_msg_next")
    if hm_02_common.HANDLE_FLAG:
        print("---------之前的数据处理完成---------")
    else:
        print("---------之前的数据未处理完成----------")
