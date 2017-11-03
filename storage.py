#--coding:utf-8--

import json

"""
存储数据
"""
# numbers = [2,3,5,7,11,13]
#
# filename = 'number.json'
# with open(filename,'w') as f:
#    json.dump(numbers,f) #函数json.dump(),把数字列表存储到文件中
#    number = json.load(f)

"""
读取数据
"""
# filename = 'number.json'
# with open(filename,'r') as f:
#     number = json.load(f)
#     print number

"""
保存和读取用户生成的数据
"""
# filename = 'username.json'
# try:
#     with open(filename) as f:
#         uname = json.load(f)
# except IOError:
#     username = raw_input("Please input your name:")
#     with open(filename,'w') as f:
#         json.dump(username,f)
#         print ("Information has been storaged.")
# else:
#     print ("Hello, " + uname)

"""
重构
"""
def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            uname = json.load(f)
    except IOError:
        return None
    else:
        return uname

def get_new_username():
    filename = 'username.json'
    username = raw_input("Please input your name:")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print ("Information has been storaged.")
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print ("Username is " + username + ". IF the username correct?(Y/N)")
        aswer = raw_input()
        if aswer == "Y":
            print ("Hello, " + username)
        else:
            get_new_username()
    else:
        get_new_username()


greet_user()

