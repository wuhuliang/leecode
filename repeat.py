#--coding:utf-8--


'''
    这是一个函数版模拟用户注册登录
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
