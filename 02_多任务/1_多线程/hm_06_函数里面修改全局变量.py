# 如果需要在函数内部对全局变量的指向进行修改，则必须使用global进行声明，如不可变类型：数字、元祖、字符串
# 如果只是对指向空间中的数据进行修改，则不需要global，如可变类型：列表、字典

num = 100
nums = [11, 22]

def test():
    global num
    num += 100


def test2():
    nums.append(33)

print(num)
print(nums)

test()
test2()

print(num)
print(nums)
