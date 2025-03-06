import requests
from bs4 import BeautifulSoup
import csv

def search(data, url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    names = soup.find_all("span", class_="css-a76tvl")
    prices = soup.find_all("span", class_="css-dlcfcd")
    addresses = soup.find_all("span", class_="css-avmlqd")
    for name, price, address in zip(names, prices, addresses):
        data.append((name.text, price.text, address.text))

def scrape():
    data = []
    base_url = 'https://www.boligportal.dk/lejeboliger/k%C3%B8benhavn/'
    search(data, base_url)
    
    for page in range(1, 100):
        url = f"{base_url}?offset={page*18}"
        search(data, url)

    with open("listings.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter = ";")
        writer.writerow(["Name", "Price", "Address"])
        writer.writerows(data) 

if __name__ == '__main__':
    scrape()