#--coding:utf-8--


'''
    demo1:定义一个返回两个整数和的函数
'''
# def add(a, b):
#     return a + b
#
# print ("result is %d" % add(5,6))

'''
    demo2:将后一个姓名列表添加到第一个列表的末尾
'''

# #定义一个列表
# name_List = ['wuhuliang','wangxiang','dubowen']
# print ("原始姓名列表为： %s" %name_List)
#
# #定义函数：功能是向name_List列表尾部添加元素
# def name_Append(lists):
#     name_List.append(lists)#注意的是：append函数是列表内置函数，功能是向列表尾部添加元素
#     print ("添加后的姓名列表是： %s" %name_List)
#
# #传参用
# name_new = 'jinyunzhen'
# #调用函数，传入参数，会返回添加后的姓名列表
# name_Append(name_new)
#
#
# print("最终的姓名列表是: %s "%name_List)

'''
demo3：输入三个数，输出最大数
'''

def max_w(a,b,c):
    MAX = a
    if (b > a):
        MAX = b
        if (c > MAX):
            MAX = c
    return MAX


x = int(raw_input("请输入第一个数："))
y = int(raw_input("请输入第二个数："))
z = int(raw_input("请输入第三个数: "))


print ("%d,%d,%d,三个数字中,最大的是 %d:" %(x,y,z,max_w(x,y,z)))

