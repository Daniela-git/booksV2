from playwright.sync_api import Page
from .helper import convertToNumber

class MyListPage:
    bookList = ".info-div"
    myList = ".wishlist"
    title = ".title"
    regularPrice = ".precioAntes"
    currentPrice = ".precioAhora"
    todaysData = {}

    def __init__(self, page:Page):
        self.page = page
    
    def getData(self):
        self.page.locator(self.myList).click(force=True)
        self.page.wait_for_load_state("networkidle")  
        books = self.page.locator(self.bookList).all()
        for book in books[:4]:
            title = book.locator(self.title).inner_text()
            regularPrice = book.locator(self.regularPrice).inner_text()
            currentPrice = book.locator(self.currentPrice).inner_text()
            data = {
                "RegularPrice": convertToNumber(regularPrice),
                "CurrentPrice": convertToNumber(currentPrice)
            }
            self.todaysData[title] = data






        