
import re
from playwright.sync_api import Page, expect
from dotenv import load_dotenv
import os
from test_pages import LoginPage, MyListPage


def test_booksV2(page: Page):
    load_dotenv()
    loginPage = LoginPage(page)
    myListPage = MyListPage(page)
    page.goto("https://www.buscalibre.com.co/v2/u")
    print(os.getenv("USERNAME"))
    loginPage.login(page,os.getenv("USERNAME"),os.getenv("PASSWORD"))
    myListPage.getData()
    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("buscalibre"))

if __name__ == "__main__":
  test_booksV2()