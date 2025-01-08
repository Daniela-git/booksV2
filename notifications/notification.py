import os
import requests
import locale

class Notification:  
        
    def __init__(self):
        self.TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
        self.TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
        self.headers = {
            'content-type': 'application/json',
            }
        self.url =  f"https://api.telegram.org/bot{self.TELEGRAM_BOT_TOKEN}/sendMessage"
        self.data = {
                "chat_id": self.TELEGRAM_CHAT_ID,
            }
        
    def sendNotification(self,text):
        self.data["text"]=text
        response = requests.post(self.url, json=self.data, headers=self.headers)
        print(response)
        
    def notificationBody(self,notificationTitle, goodPrices):
        locale.setlocale(locale.LC_ALL, '')
        text = notificationTitle
        for book in goodPrices:
            price = locale.format_string("%.0f",book["price"], grouping=True)
            title = book["title"]
            text = f"{text}\n**{title}**: ${price}"
        return text
    
                