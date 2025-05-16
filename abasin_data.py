from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

url = "https://www.arapahoebasin.com/snow-report/"
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

measure = soup.find("div", class_="sr-box-1")
measure = measure.get_text(strip=True)

measure = measure[measure.find("24HR"):]

if measure[5] in ['0','1','2','3','4','5','6','7','8','9']:
    if measure[6]  in ['0','1','2','3','4','5','6','7','8','9']:
        measure = measure[4:8]
    else:
        measure = measure[4:7]
else:
    measure = measure[4:6]

print("A-Basin Last 24 Hours:" + measure)


driver.quit()