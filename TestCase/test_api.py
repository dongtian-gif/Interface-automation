import requests

import unittest
 #4.编写测试用例和断言
class Testapi(unittest.TestCase):
    '''测试接口'''
    def test_school(self):
        '''测试接口是否正常返回'''
        url = "http://127.0.0.1:8888/query"

        par = {
                 "school": "北京一中",  # 输入参数params
         }
        r = requests.post(url, params=par)
        print(r.text)     # 获取返回的结果
        print(r.status_code)  #相应状态码
        names = r.json()['student_names'] #获取返回值
        age= r.json()['age']
         # print(result)
         # print(result2)
         # 断言
         # assert r.status_code == 200
        self.assertEqual(r.status_code,200)
        self.assertEqual('张静', names)  #值是否相等，直接的比较
        self.assertEqual('25', age)

    def test_student_names(self):
        '''测试接口是否正常返回'''
        url = "http://127.0.0.1:8888/query"

        par = {
            "student_names": "李丽",  # 输入参数params
        }
        r = requests.post(url, params=par)
        print(r.text)  # 获取返回的结果
        print(r.status_code)  # 相应状态码
        school = r.json()['school']  # 获取返回值

        classname = r.json()['class']
        # print(result)
        # print(result2)
        # 断言
        # assert r.status_code == 200

        self.assertEqual(r.status_code, 200)
        self.assertEqual('清华附中', school)  # 值是否相等，直接的比较
        self.assertEqual('一班', classname )

if __name__ == "__main__":
     unittest.main()