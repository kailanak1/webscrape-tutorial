from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic%20card'

#opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.findAll("div", {"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"

f.write(headers)

for container in containers:
    brand = container.img["title"]
    new_brand = brand.replace(",", " ")
    title_container = container.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text
    new_product_name = product_name.replace(","," ")
    shipping_container = container.findAll("li",{"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand: " + brand)
    print("product name: " + new_product_name)
    print("shipping: " + shipping)

    f.write(new_brand + "," + new_product_name + "," + shipping + "\n")

f.close()