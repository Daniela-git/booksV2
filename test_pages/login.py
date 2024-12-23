from playwright.sync_api import Page, expect

class LoginPage():
    username = "#signin_username"
    continueBtn = "#submit_login"
    password = "#signin_password"
    closePopUp= ".cerrar"

    def __init__(self,page:Page):
      self.page = page
    
    def login(self,user, password):
      popUp = self.page.locator(self.closePopUp)
      if(popUp.is_visible()):
        popUp.click()
      self.page.locator(self.username).fill(user)
      self.page.locator(self.continueBtn).first.click()
      self.page.locator(self.password).fill(password)
      self.page.get_by_role("button", name="Ingresar").click()
      expect(self.page.locator(self.username)).not_to_be_visible()
      