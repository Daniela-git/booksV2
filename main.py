from playwright.sync_api import Page
import os
from test_pages import LoginPage, MyListPage
from notion.updateData import writeData
from notifications import notification


def test_booksV2(page: Page):    
    loginPage = LoginPage(page)
    myListPage = MyListPage(page)
    page.goto(os.environ("URL"))
    loginPage.login(os.environ("USERNAME"),os.environ("PASSWORD"))  
    page.wait_for_load_state("networkidle")  
    myListPage.getData()
    #updating notion tables
    data = writeData(myListPage.todaysData)
    notificationObj = notification.Notification()
    if(len(data["goodPrices"]) > 0):
      notificationObj.sendNotification(notificationObj.notificationBody("GOOD PRICE(S)",data["goodPrices"]))
    if(len(data["lowest"]) > 0):
      notificationObj.sendNotification(notificationObj.notificationBody("NEW LOWEST(S)",data["lowest"]))
    
