from selenium import  webdriver
from selenium.webdriver.common.by import By


class Login():

	_login_locator = (By.CSS_SELECTOR, 'a.link.s-fc3')
	_other_login_mode_locator =(By.CSS_SELECTOR ,'a.u-btn2.other')
	_phone_number_login_locator = (By.CSS_SELECTOR ,'a.u-btn2.u-btn2-2')
	_privacy_policy_checkout_loactor = (By.CSS_SELECTOR ,'input#j-official-terms')
	_input_phone_number_locator = (By.CSS_SELECTOR , 'input.j-phone.txt.u-txt')
	_input_password_locator = (By.CSS_SELECTOR , 'input#pw.j-pwd.u-txt')
	_login_button_locator = (By.CSS_SELECTOR, 'a.j-primary.u-btn2.u-btn2-2')

	def __init__(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(4)
		self.driver.maximize_window()
		self.driver.get('https://music.163.com/')

	def click_login(self):
		self.driver.find_element(*self._login_locator).click()

	def select_other_login_mode(self):
		self.driver.find_element(*self._other_login_mode_locator).click()

	def check_privacy_policy_checkout(self):
		if not self.driver.find_element(*self._privacy_policy_checkout_loactor).is_selected():
			self.driver.find_element(*self._privacy_policy_checkout_loactor).click()

	def phone_number_login(self):	
		self.driver.find_element(*self._phone_number_login_locator).click()

	def input_phone_number_account(self):
		self.driver.find_element(*self._input_phone_number_locator).send_keys('165564464654')
	
	def input_password(self):
		self.driver.find_element(*self._input_password_locator).send_keys('253156454121')
	
	def click_login_button(self):
		self.driver.find_element(*self._login_button_locator).click()

	def close_window(self):
		self.driver.quit()

if __name__ == '__main__':
	login = Login()
	login.click_login()
	login.select_other_login_mode()
	login.check_privacy_policy_checkout()
	login.phone_number_login()
	login.input_phone_number_account()
	login.input_password()
	login.click_login_button()
	login.close_window()

