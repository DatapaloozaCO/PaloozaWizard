from bs4 import BeautifulSoup
with open("test.html", "r") as f:
    data = f.read()
    data = BeautifulSoup(data, "html.parser")

#print(data)
section = data.find_all("section", recursive=False)[0]
divs = section.find_all("div", recursive=False)
print(divs)