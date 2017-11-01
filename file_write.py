#--coding:utf-8--

filename = 'F:\python practice\\test_files\programming.txt'

"""
写入空文件,多行
"""
# with open(filename,'w') as f:
#     f.write('I love programming.\n')
#     f.write('I love create new games.\n') #使用空格、制表符和空行来设置输出的格式

"""
附加到文件
"""
# with open(filename,'a') as f:
#     f.write('I also love finding meaning in large datasets.\n')
#     f.write('I love create apps that can run in a browser.\n')

"""
练习一：访客
"""
# username = 'F:\python practice\\test_files\username.txt'
# name = raw_input('Please input your name:')
# with open(username,'a') as f:
#     f.write(name)

"""
练习二：访客名单
"""
username = 'F:\python practice\\test_files\username.txt'
while 1 :
    name = raw_input('Please input your name:')
    print ("Hello, %s" % name)
    with open(username,'a') as f:
        f.write(name + '\n')


