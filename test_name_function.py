#--coding:utf-8--

"""
测试函数
"""
# import unittest
# from name_function import get_full_name
#
# class NameTestCase(unittest.TestCase):
#
#     def test_first_last_name(self):
#         formatted_name = get_full_name('janis','joplin')
#         self.assertEqual('Janis Joplin',formatted_name)
#
#     def test_first_last_middle_name(self):
#         formatted_name = get_full_name('wolfgang','mozart','amadeus')
#         self.assertEqual('Wolfgang Amadeus Mozart',formatted_name)
#
# if __name__=='main':
#     unittest.main()

"""
测试类
"""
import unittest
from name_function import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        """
        创建一个调查对象和一组答案，供使用的测试方法使用
        """
        question = "What language did you first learn?"
        self.my_survey = AnonymousSurvey(question)
        self.response_list = ['English','Spanish','Mandarin']

    def test_store_single_response(self):
        """测试单个答案会被正确存储"""
        self.my_survey.store_response(self.response_list[0])   #调用 存储回答 方法，使responses属性，即该列表新增一个English数据项
        self.assertIn('English',self.my_survey.responses)  #检查值是否存在于列表中

    def test_store_three_response(self):
        """测试三个答案会被正确存储"""
        for response in self.response_list:
            self.my_survey.store_response(response)  #将答案逐一存入responses属性列表
        for response in self.response_list:
            self.assertIn(response,self.my_survey.responses)


if __name__ == 'main':
    unittest.main
