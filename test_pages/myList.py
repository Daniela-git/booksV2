import re
from playwright.sync_api import Page
from helper import convertToNumber

class MyListPage:
    bookList = ".info-div"
    myList = ".wishList"
    title = ".title"
    regularPrice = ".precioAntes"
    currentPrice = ".precioAhora"
    percentaje = ".etiquetawish > .numero"
    todaysData = {}

    def __init__(self, page:Page):
        self.page = page
        pass
    
    def getData(self):
        c = "dsdf"
        self.page.locator(self.myList).click()
        books = self.page.locator(self.bookList).all()
        for book in books:
            title = book.locator(title).inner_text()
            regularPrice = book.locator(regularPrice).inner_text()
            currentPrice = book.locator(currentPrice).inner_text()
            data = {
                "regularPrice": convertToNumber(regularPrice),
                "currentPrice": convertToNumber(currentPrice)
            }
            self.todaysData[title] = data






        