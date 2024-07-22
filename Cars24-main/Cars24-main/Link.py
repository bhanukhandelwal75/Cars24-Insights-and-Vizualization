#Import the required libraries or modules.
from selenium import webdriver
from bs4 import BeautifulSoup
import time

#Step 1: Driver ready to scrape the URL.
driver = webdriver.Firefox()
url = 'https://www.cars24.com/buy-used-cars-delhi-ncr/'
driver.get(url)

#Step 2: Set Driver to scroll N number of time.
for i in range(20):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

page_source = driver.page_source
driver.quit()

soup = BeautifulSoup(page_source, 'html.parser')

#Step 3: Create an empty List to store the Output.
final_list = []

#Step 4: Use BeautifulSoup to scrape the data using tag and class name and append them to the list.
for div in soup.find_all('a', class_='IIJDn'):
    link_tag = div
    if link_tag:
        final_list.append(link_tag['href'])
    else:
        final_list.append(None)

#Step 5: Just print to see the list and the Number of elements inside it.
print(final_list)
print(len(final_list))
