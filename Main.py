from selenium import  webdriver
import unittest
import  time
import HtmlTestRunner
from  selenium.webdriver.common.keys import Keys
import sys
sys.path.append("C:\\Users\\NIRAJ RANA\\PycharmProjects\\POM_Python")
from Pages.Createtest import Login

class main(unittest.TestCase):
    driver = webdriver.Chrome(executable_path=r"C:\Users\NIRAJ RANA\PycharmProjects\Demo_Project\Drivers\chromedriver.exe")
    username = "admin@yourstore.com"
    password = "admin"

    @classmethod
    def setUpClass(cls):
        driver = cls.driver
        driver.implicitly_wait(10)
        driver.get("https://admin-demo.nopcommerce.com/")
        driver.implicitly_wait(20)
        time.sleep(5)
        driver.maximize_window()

    def test_case_login(self):
        ct = Login(self.driver)
        ct.username(self.username)
        print('Test Step 1: Username entered\n')
        ct.password(self.password)
        print('Test Step 2: Password entered')
        ct.login_btn()
        print("Test Step 3: Clicked on the Login button")
        time.sleep(7)
        self.assertEqual("Dashboard / nopCommerce administration",self.driver.title,"Webpage is not matching")

    def test_case_logout(self):
        ct = Login(self.driver)
        ct.logout()
        print("Test Step 1: Click oed on the Logout button")

    @classmethod
    def tearDownClass(cls):
        driver=cls.driver
        driver.close()
        driver.quit()

if __name__ =='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\NIRAJ RANA\\PycharmProjects\\POM_Python\\Reports"))
