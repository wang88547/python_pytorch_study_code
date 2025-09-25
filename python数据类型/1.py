"""
print(666)
print(13.1)
print("niko")
"""
from sympy.physics.units import kilogram

# 单行注释


"""
print("niko")
"""

# print(type(123))
"""
name = type(123)

print(name)

name = 123

print(type(name))
"""


print(str(13))

print(type(str(13)))

#不用ASCII码存储
# num = int("a")
# print(num, type(num))

name = "123"

print("123" + name)

a_1 = 123
a_2 = 456
print("abc%s,abc%s" % (a_1, a_2))

"""
字符串格式化占位
"""

name = "Wang"

birthday = 20060121

kg = 57.5

print(f"My name is {name}, and my birthday is {birthday}, and my kg is {kg}")

print("My name is %s, and my birthday is %d, and my kg is %f" % (name, birthday, kg))










