from bs4 import BeautifulSoup
import requests
import csv
import sys


def getHTML(url):
    response = requests.get(url)
    return response.text

books = []


try:
    for i in range(51):
        html = getHTML(f"https://books.toscrape.com/catalogue/page-{i}.html")
        soup = BeautifulSoup(html,'html.parser')
        table = soup.find_all("article", class_ = "product_pod")

        for row in table:
            book = {}    
            book["title"] = row.find_all_next("h3")[0].string
            #removing the euro dollar sign
            book["price"] = row.find("p", class_ = "price_color").string[1:]
            rate = row.find(class_ = "star-rating")
            book["rating"] = rate["class"][1] + " Star"
            books.append(book)
        
    with open("books.csv","w", encoding="utf-8") as bookCSV:
        newCSV = csv.DictWriter(bookCSV, fieldnames=books[0].keys())
        newCSV.writeheader()
        newCSV.writerows(books)

except:
    sys.exit("An error has occured.")
