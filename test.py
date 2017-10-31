#--coding:utf-8--

file_name = 'F:\python practice\\test_files\learning_python.txt'

"""
读取整个文件
"""
# with open(file_name) as f:
#     text = f.read()
#     print text

"""
遍历文件对象
"""
# with open(file_name) as f:
#     for hang in f:
#         print hang.strip()

"""
存储在列表中
"""
# with open(file_name) as f:
#     list = f.readlines()
#     print list
#
# for l in list:
#     print l.strip()

"""
修改文件内容
"""
with open(file_name) as f:
    list = f.readlines()
    print list


for l in list:
    h = l.strip().replace('Python','JAVA')
    print h
