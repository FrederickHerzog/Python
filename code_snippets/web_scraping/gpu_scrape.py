#Frederick Herzog
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

values = ['0','1','2','3','4','5','6','7','8','9','0','.','$']
count = 1
my_url = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709&Order=RATING'

#opening up the connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class":"item-container"})


# file operations
F = open("/home/fs/Desktop/data.csv", "w")
headers = "brand, product_name, price\n"
F.write(headers)

for container in containers:
	brand = container.div.div.a.img["title"]
	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text
	price_container = container.findAll("li", {"class":"price-current"})
	price1 = price_container[0].text
	price = ''
	for ch in price1:
		if len(price) <= 6:
			if ch in values:
				price += ch

	print(count)
	print("Brand:", brand)
	print("Product Name:", product_name)
	print("Price:",price)
	print()
	F.write(brand + "," +product_name.replace(",", "|") + "," +price +"\n")

	count += 1

F.close()
