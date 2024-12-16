from playwright.sync_api import Page

class LoginPage():
    username = "#signin_username"
    continueBtn = "#submit_login"
    password = "#signin_password"

    def __init__(self,page:Page):
      self.page = page
    
    def login(self,user, password):
      self.page.locator(self.username).fill(user)
      self.page.locator(self.continueBtn).first.click()
      self.page.locator(self.password).fill(password)
      self.page.get_by_role("button", name="Ingresar").click()