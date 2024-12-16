import re
from playwright.sync_api import Page, expect

def booksV2(page: Page):
    page.goto("https://www.buscalibre.com.co/v2/u")
    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("buscalibre"))