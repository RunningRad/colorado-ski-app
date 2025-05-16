from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

url = "https://www.winterparkresort.com/the-mountain/mountain-report"
driver.get(url)

time.sleep(3) 

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

measure = soup.find("div", class_="WeatherWidget_currentComponent__hXZNL")
measure = measure.get_text(strip=True)

measure = measure[measure.find("Last 24 Hour:"):]
measure = measure[measure.find(":"):]

if measure[3] in ['0','1','2','3','4','5','6','7','8','9']:
    if measure[4]  in ['0','1','2','3','4','5','6','7','8','9']:
        measure = measure[1:5]
    else:
        measure = measure[1:4]
else:
    measure = measure[1:3]


print("Winter Park Last 24 Hours: " + measure)

driver.quit()