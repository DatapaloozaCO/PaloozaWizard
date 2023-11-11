from bs4 import BeautifulSoup
import palooza_wizard.constants as ct
import sys  

print(f"Using file: {ct.SOUPS_OUTPUT_FOLDER}/base_soup.html")

with open(f'{ct.SOUPS_OUTPUT_FOLDER }/base_soup.html') as f:
    soup = BeautifulSoup(f, 'html.parser')

values = [0, 0, 0, 1, 0, 0, 5, 0, 0, 0]
for value in values:
    soup = soup.findChildren(recursive=False)[value]
print(soup)

sys.exit()

print(soup.name)

res = soup.findChildren(recursive=False)[0]
print(0, res.name)

res = res.findChildren(recursive=False)[0]
print(0, res.name)

res = res.findChildren(recursive=False)[0]
print(0, res.name)

res = res.findChildren(recursive=False)[1]
print(1, res.name)

res = res.findChildren(recursive=False)[0]
print(0, res.name)

res = res.findChildren(recursive=False)[0]
print(0, res.name)

res = res.findChildren(recursive=False)[5]
print(5, res.name)

res = res.findChildren(recursive=False)[0]
print(0, res.name)

res = res.findChildren(recursive=False)[0]
print(0, res.name)

res = res.findChildren(recursive=False)[0]
print(0, res.name)

#print(res)

