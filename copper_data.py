from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)

url = "https://www.coppercolorado.com/the-mountain/conditions-weather/snow-report"
driver.get(url)

# time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

measure = ""

for tag in soup.find_all('li'):
    text = tag.get_text(strip=True)
    if '24' in text and ('snow' in text.lower() or 'Snow' in text):
        measure = text[-4:]

if measure[1] in ['0','1','2','3','4','5','6','7','8','9']:
    if measure[0] not in ['0','1','2','3','4','5','6','7','8','9']:
        measure = measure[-3:]
else:
    measure = measure[-2:]

print("Copper Mountain Last 24 Hours: " + measure)

driver.quit()