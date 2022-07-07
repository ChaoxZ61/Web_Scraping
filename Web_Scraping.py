from bs4 import BeautifulSoup
import requests
import csv
import sys


def getHTML(url):
    response = requests.get(url)
    return response.text

books = []


try:
    html = getHTML(f"http://books.toscrape.com")

    soup = BeautifulSoup(html,'html.parser')

    table = soup.find("article", class_ = "product_pod")



    for row in table.find_all_next("article", class_ = "product_pod"):
        book = {}    
        book["title"] = row.find_all_next("h3")[0].string
        #removing the euro dollar sign
        book["price"] = row.find("p", class_ = "price_color").string[2:]
        rate = row.find(class_ = "star-rating")
        book["rating"] = rate["class"][1] + " Star"
        books.append(book)

    with open("books.csv","w") as bookCSV:
        newCSV = csv.DictWriter(bookCSV, fieldnames=books[0].keys())
        newCSV.writeheader()
        newCSV.writerows(books)

except:
    sys.exit("An error has occured.")
