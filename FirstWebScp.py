from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48'

# establishes connection and grabs the web page

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html page parser
page_soup = soup(page_html, "html.parser")

# grabs each product  

containers = page_soup.findAll("div",{"class":"item-container"})

filename = "neweggProducts.csv"
f = open(filename, "w")

headers = "product_name, shipping\n"

f.write(headers)

for container in containers:

	# grabs product name

	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text 

	# grabs shipping price

	shipping_container = container.findAll("li", {"class":"price-ship"})
	shipping = shipping_container[0].text

	print("product_name: " + product_name)
	print("shipping: " + shipping)

	f.write(product_name.replace(",", "|") + "," + shipping + "\n")

f.close()