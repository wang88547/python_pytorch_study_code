#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
print("传智播客,股票代码：%d，当前股价：%.2f\n"
      "每日增长系数是：%.1f，经过7天增长后，股价达到了：%.1f" %
      (1,(3/2),3,4))
i = 0
name = "aabbbbb"
for x in name:
    if x=='a':
        i+=1

print(i)
name = 12
name = float(name)
print(name)

tinydict = {'name': 'runoob','code':6734, 'dept': 'sales'}

print (tinydict['name'])


def printinfo(name, age=0):
    "打印任何传入的字符串"
    print ("Name: ", name)
    print ("Age ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="miki")
printinfo(name="miki")


def printinfo(*vartuple):
    "打印任何传入的参数"
    print ("输出: ")
#    print (arg1)
    for var in vartuple:
        print (var)
    return

# 调用printinfo 函数
printinfo( 10 )
printinfo( 70, 60, 50 )

"""



class Person:
    name = None
    age = None

stu_1 = Person

stu_1.age = 12
stu_1.name = "miki"

print(stu_1)





