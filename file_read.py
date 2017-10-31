#--coding:utf-8--

"""
读取整个文件
"""
# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()   #read()到达文件末尾时返回一个空字符串，空字符串显示出来就是一个空行
#     print contents       #可通过调用rstrip()方法删除字符串末尾的空行


"""
文件路径
"""
# file_path = 'F:\python practice\\test_files\pi_digits.txt'
# with open(file_path) as file_object:
#     contents = file_object.read()
#     print contents

"""
逐行读取
"""
# file_name = 'F:\python practice\\test_files\pi_digits.txt'
#
# with open(file_name) as file_object:
#     for hang in file_object:  #for循环逐行读取文件内容
#         print hang.rstrip()

"""
创建列表，包含文件各行内容
"""
# file_name = 'F:\python practice\\test_files\pi_digits.txt'
# with open(file_name) as file_object:
#     hangs = file_object.readlines()   #readlines()将文件每一行作为列表中的一个元素，会将所有内容加载进来。注意内存
#
# for h in hangs:
#     print h.rstrip()

"""
使用文件的内容
"""
file_name = 'F:\python practice\\test_files\pi_digits.txt'
with open(file_name) as file_object:
    hangs = file_object.readlines()

pi_string = ''
for h in hangs:
    pi_string += h.strip()  #当没有传入参数时，是默认去除首尾空格的

print pi_string
print len(pi_string)