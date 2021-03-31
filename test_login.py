import unittest
from app import Login
from ddt import ddt,data,unpack

@ddt
class TestLogin(unittest.TestCase):
    
    @data(('https://music.163.com/','165564464654','huudff'))
    @unpack
    def test_login_wangyiyun(self,url,phone_number,password):
        login = Login(url)
        login.click_login()
        login.select_other_login_mode()
        login.check_privacy_policy_checkout()
        login.phone_number_login()
        login.input_phone_number_account(phone_number)
        login.input_password(password)
        login.click_login_button()
        login.close_window()

if __name__ =='__main__':
    unittest.main()


# class TestLogin(unittest.TestCase):

#     def test_login_wangyiyun(self):
#         login = Login('https://music.163.com/')
#         login.click_login()
#         login.select_other_login_mode()
#         login.check_privacy_policy_checkout()
#         login.phone_number_login()
#         login.input_phone_number_account('165564464654')
#         login.input_password('hfied')
#         login.click_login_button()
#         login.close_window()
