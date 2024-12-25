from notion.queries import NotionQuery
from datetime import datetime, timezone

def writeData(todaysData):
  queries = NotionQuery()
  keys = list(todaysData.keys())
  date = datetime.now().astimezone(timezone.utc).isoformat()
  newLowests = []
  goodPrices = []
  for title in keys:
    print("title "+ title)
    data = todaysData[title]
    pageTable1 = queries.get_page_table1(title)
    if(not pageTable1):
      #new book
      print("new book "+title)
      newPage=queries.create_page_table1(title, data["CurrentPrice"],data["CurrentPrice"],"none")
      newDB = queries.create_page_db(newPage["id"],title)
      dataToUpdate = {
        "dbId": newDB["id"]
      }
      queries.update_page_table1(newPage["id"],dataToUpdate)
      queries.create_page_table2(newDB["id"],title,data["CurrentPrice"],data["RegularPrice"],date,1)
    else:
      #old book
      print("old book")
      lastPrice = pageTable1["properties"]["Current price"]["number"]
      todaysPrice = data["CurrentPrice"]
      #storing the price only if it changes
      if (lastPrice != todaysPrice):
        print(f"price change: old {lastPrice} - new {todaysPrice}")
        lowest = pageTable1["properties"]["Lowest"]["number"]
        dataToUpdate = {
          "CurrentPrice":todaysPrice
        }
        #new lowest
        if(todaysPrice < lowest):
          print("new lowest")
          newLowests.append({"title":title, "price":todaysPrice})
          dataToUpdate["Lowest"] = todaysPrice 
        #good price
        elif(todaysPrice <= lowest + 5000):
          print("good price")
          goodPrices.append({"title":title, "price":todaysPrice})         
        #update table 1
        queries.update_page_table1(pageTable1["id"],dataToUpdate)
        #search price in table 2
        pageDBId = pageTable1["properties"]["dbId"]["rich_text"][0]["text"]["content"]
        priceRecord = queries.get_page_table2(pageDBId,todaysPrice)
        if(priceRecord):
          print("update price")
          updateTable2 = {
            "PriceCount":priceRecord["properties"]["Price count"]["number"]+1,
            "RegularPrice":data["RegularPrice"],
            "Date":date
          }
          queries.update_page_table2(priceRecord["id"],updateTable2)
        else:
          print("new price")
          queries.create_page_table2(pageDBId,title,data["CurrentPrice"],data["RegularPrice"],date,1)  
          
  return {
    "goodPrices": goodPrices,
    "lowest": newLowests
  }          
