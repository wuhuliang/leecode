#--coding:utf-8--


'''
    demo1:列表末尾插入一条数据
'''

list1 = ['wu', 'wang', 'du']
print ("初始数据为：%s" % list1)

def add_shuju(shuju):
    list1.append(shuju)
    print ("新数据为：%s" % list1)

new = 'liu'
add_shuju(new)

#push github