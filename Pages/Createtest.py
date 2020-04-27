class Login():

    textbox_username_id = "Email"
    textbox_password_id = "Password"
    login_button_xpath = "//input[@value='Log in']"
    logout_linktext = "Logout"


    def __init__(self, driver):
        self.driver = driver

    def username(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def password(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def login_btn(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def logout(self):
        self.driver.find_element_by_link_text(self.logout_linktext).click()