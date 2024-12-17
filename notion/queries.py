from notion_client import Client
import os

class NotionQuery:
  def __init__(self):
    self.dbIdTable1 = os.environ["DBIDTABLE1"]
    self.notion = Client(auth=os.environ["NOTION_KEY"])

  def create_page_table1(self,title,currentPrice,lowest, pageId):  
    query = {
        "parent": {
          "database_id": self.dbIdTable1,
        },
        "properties": {
          "Book": {
            "type": "title",
            "title": [
              {
                "type": "text",
                "text": {
                  "content": title,
                },
              },
            ],
          },
          "Current price": {
            "type": "number",
            "number": currentPrice,
          },
          "dbId": {
            "rich_text": [
              {
                "text": {
                  "content": pageId
                }
              }
            ]
          },
          "Lowest": {
            "type": "number",
            "number": lowest,
          },
        }
      }
    return self.notion.pages.create(**query)
  
  def create_page_db(self,page_id,title):
    createDBquery = {
      "parent": {
          "type": "page_id",
          "page_id": page_id
      },
      "title": [
          {
              "type": "text",
              "text": {
                  "content": title+" DB"
              }
          }
      ],
      "properties": {
        "Book": {
          "title":{}
        },
        "Current price": {
          "number": {}
        },
        "Regular price": {
          "number": {}
        },
        "Price count": {
          "number": {}
        },
        "Date": {
          "date": {}
        }
      }
    }
    return self.notion.databases.create(**createDBquery)
  
  def create_page_table2(self,newDBId,title,currentPrice,regularPrice,date,priceCount):
    newPageQuery = {
      "parent": {
        "database_id": newDBId,
      },
      "properties": {
        "Book": {
          "type": "title",
          "title": [
            {
              "type": "text",
              "text": {
                "content": title,
              },
            },
          ],
        },
        "Current price": {
          "type": "number",
          "number": currentPrice,
        },
        "Regular price": {
          "type": "number",
          "number": regularPrice,
        },
        "Price count": {
          "type": "number",
          "number": priceCount,
        },
        "Date": {
          "type": "date",
          "date": {
            "start": date,
          },
        }
      },
    }
    return self.notion.pages.create(**newPageQuery)
  
  def update_page_table1(self,pageId, dataToUpdate):
    updatePageQuery = {
      "page_id": pageId,
      "properties": {
        }
      }
    keys = list(dataToUpdate.keys())
    if "dbId" in keys:
      updatePageQuery["properties"]["dbId"]={          
        "rich_text": [
          {
            "text": {
              "content": dataToUpdate["dbId"]
            }
          }
        ]
      }    
    if "CurrentPrice" in keys:
      updatePageQuery["properties"]["Current price"]={
        "number":dataToUpdate["CurrentPrice"]
      }
    if "Lowest" in keys:
      updatePageQuery["properties"]["Lowest"]={
        "number":dataToUpdate["Lowest"]
      }  
    return self.notion.pages.update(**updatePageQuery)
  
  def update_page_table2(self,pageId, dataToUpdate):
    updatePageQuery = {
      "page_id": pageId,
      "properties": {
        }
      }
    keys = list(dataToUpdate.keys())
    if "PriceCount" in keys:
      updatePageQuery["properties"]["Price count"]={
        "number":dataToUpdate["PriceCount"]
      }
    if "RegularPrice" in keys:
      updatePageQuery["properties"]["Regular price"]={
        "number":dataToUpdate["RegularPrice"]
      }
    if "Date" in keys:
      updatePageQuery["properties"]["Date"]={
        "date":{
          "start":dataToUpdate["Date"]
        }          
      }       
    return self.notion.pages.update(**updatePageQuery)
  
  def get_page_table1(self,title):
    query = {
      "database_id": self.dbIdTable1,
      "filter": {
        "and": [
          {
            "property": "Book",
            "title": {
              "equals": title,
            },
          },
        ],
      },
    }
    response = self.notion.databases.query(**query)
    results = response["results"]
    if (len(results)==0):
      return False
    return results[0]
    
  def get_page_table2(self,dbId,price):
    query = {
      "database_id": dbId,
      "filter": {
        "and": [
          {
            "property": "Current price",
            "number": {
              "equals": price,
            },
          },
        ],
      },
    }
    response = self.notion.databases.query(**query)
    results = response["results"]
    if (len(results)==0):
      return False
    return results[0]
  