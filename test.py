#--coding:utf-8--

# 定义保存用户名和密码的字典
userInfo = {}

# 是否登录的标志
islog = False

# 注册方法
def register():
    uname = raw_input("添加用户名: ")
    upass = raw_input("添加密码: ")
    userInfo[uname] = upass
    print("注册成功")
    print userInfo

register()