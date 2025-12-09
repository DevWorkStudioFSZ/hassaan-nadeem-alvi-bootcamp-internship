import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template


app = Flask(__name__)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
for i in range(1,10):
    web= requests.get("https://www.olx.com.pk/mobile-phones_c1453?page="+str(i), headers=headers)
    # print(web)
    soup = BeautifulSoup(web.text,"html.parser")
    # print(soup)


    h2 = []
    a = soup.find_all("h2", class_ = "_1093b649")

    for i in a:
        h2.append(i.text)
        # print(i.text)


    images =[]

    a= soup.find_all("img")
    for i in a :
        images.append(i.get("src"))



    price = []

    p = soup.find_all("span",class_='f83175ac')
    for i in p:
        price.append(i.text)
        # print(i.text)


    location = []

    p = soup.find_all("span",class_="f047db22")
    for i in p:
        location.append(i.text)
        # print(i.text)
    print("__________________________________________")

@app.route("/")
def home():
    return render_template("index.html",h2=h2,images = images,price = price, locations = location)


if __name__ == "__main__":
    app.run(debug=True)
