import math


def area_calc(height, width, coverage):
    area = height * width
    res = math.ceil(area / coverage)
    print(f"You'll need {res} cans of paint")


test_h = int(input("the height of the wall"))
test_w = int(input("the width of the wall"))
test_c = int(input("the coverage of the scan"))
area_calc(height=test_h, width=test_w, coverage=test_c)
