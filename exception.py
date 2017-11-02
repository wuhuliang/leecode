#--coding:utf-8--

"""
除数不能为零：ZeroDivisionError
"""
# print ("Give me two numbers, and I'll divide them.")
# print ("Enter 'q' to quit.")
#
# while True:
#     first_number = raw_input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = raw_input("Second number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except  ZeroDivisionError:
#         print("You can not divide by 0.")
#     else:    #如果try代码块执行成功，--依赖--他成功执行的代码都放在else代码块中
#         print (answer)

"""
文件找不到IOError
"""
# filename = 'alice.txt'
# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except IOError:
#     msg = "Sorry, the file " + filename +" does not exist."
#     print (msg)

"""
分析文本
"""
# filename = 'computer.log'
# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except IOError:
#     msg = "Sorry, the file " + filename +" does not exist."
#     print (msg)
# else: #统计单词个数
#     words_list = contents.split()   #split()函数，以空格为分隔符把字符串拆分开，并存储为一个列表
#     count = len(words_list)
#     print ("The file "+ filename + " has about " + str(count) + " words.")

"""
使用多个文件
"""
# def count_words(filename):
#     try:
#         with open(filename) as f_obj:
#             contents = f_obj.read()
#     except IOError:
#         msg = "Sorry, the file " + filename +" does not exist."
#         print (msg)
#     else: #统计单词个数
#         words_list = contents.split()
#         count = len(words_list)
#         print ("The file "+ filename + " has about " + str(count) + " words.")
#
# file_list = ['computer.log','middleware.log','network.log']
# for file in file_list:
#     count_words(file)

"""
失败时一声不吭pass语句
"""
def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except IOError:
        pass  #充当占位符
    else:
        words_list = contents.split()
        count = len(words_list)
        print ("The file "+ filename + " has about " + str(count) + " words.")

file_list = ['computer.log','middleware.log','network.log']
for file in file_list:
    count_words(file)