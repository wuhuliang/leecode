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

# def max_w(a,b,c):
#     MAX = a
#     if (b > a):
#         MAX = b
#         if (c > MAX):
#             MAX = c
#     return MAX
#
#
# x = int(raw_input("请输入第一个数："))
# y = int(raw_input("请输入第二个数："))
# z = int(raw_input("请输入第三个数: "))
#
#
# print ("%d,%d,%d,三个数字中,最大的是 %d:" %(x,y,z,max_w(x,y,z)))

'''
    demo4:这是一个函数版模拟用户注册登录
'''

# 定义保存用户名和密码的字典
userInfo = {}

# 是否登录的标志
islog = False

# 注册方法
def register():
    uname = raw_input("添加用户名: ")
    upass = raw_input("添加密码: ")
    userInfo[str(uname)] = upass
    print("注册成功")

# 登录方法
def login():
    for i in range(3):
        global islog
        if(islog):
            break
        username_input = raw_input('请输入用户名:')
        userpass_input = raw_input("请输入密码:")
        login_count = 2-i  # 判断还能输入多少次。
        for key in userInfo.keys():
            if(str(username_input) == key and userInfo[key]== userpass_input):
                print("欢迎 %s 登录"%key)
                islog = True
                break
            else:
                # 最后一次是 0 不再提示
                if login_count != 0:
                    print("用户名或密码错误，还可以输入 %d 次"%login_count)
        if(i==2):
            print("登录超过 3 次，半个小时后再登录")


register()
login()