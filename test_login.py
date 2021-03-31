import unittest
from app import Login


class TestLogin(unittest.TestCase):

    def test_login_wangyiyun(self):
        login = Login()
        login.click_login()
        login.select_other_login_mode()
        login.check_privacy_policy_checkout()
        login.phone_number_login()
        login.input_phone_number_account()
        login.input_password()
        login.click_login_button()
        login.close_window()

if __name__ =='__main__':
    unittest.main()