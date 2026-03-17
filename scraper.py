from selenium import webdriver
from bs4 import BeautifulSoup
import json
import time

driver = webdriver.Chrome()

url = "https://www.indeed.com/viewjob?jk=b1c329181eab855c&from=shareddesktop_copy"
driver.get(url)

time.sleep(3)

soup = BeautifulSoup(driver.page_source, "html.parser")

scripts = soup.find_all("script", type="application/ld+json")

for script in scripts:
    try:
        data = json.loads(script.string)

        if isinstance(data, dict) and data.get("@type") == "JobPosting":
            print("Date Posted:", data["datePosted"])

        elif isinstance(data, list):
            for item in data:
                if item.get("@type") == "JobPosting":
                    print("Date Posted:", item["datePosted"])

    except:
        pass

driver.quit()