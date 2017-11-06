#--coding:utf-8--

"""
测试函数
"""
# def get_full_name(firstName,lastName,middleName=''):
#     if middleName:
#         full_name = firstName + ' ' + middleName + ' ' + lastName
#     else:
#         full_name = firstName + ' ' + lastName
#     return full_name.title()

"""
测试类
"""
class AnonymousSurvey(object):

    def __init__(self,question):
        self.question = question
        self.responses = []

    #显示问题
    def show_question(self):
        print (self.question)

    #存储答案
    def store_response(self,new_response):
        self.responses.append(new_response)

    #显示所有答案
    def show_result(self):
        print ("Survey results:")
        for r in self.responses:
            print('-' + r)

class Employee(object):
    def __init__(self,firstname,lastname,payment):
        self.fn = firstname
        self.ln = lastname
        self.pay = payment

    def give_raise(self,inpay=5000):
        increase_pay = int(self.pay) + inpay
        return increase_pay
