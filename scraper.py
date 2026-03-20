from selenium import webdriver
from bs4 import BeautifulSoup
import json
import time


def scrape_job(url):
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        time.sleep(3)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        scripts = soup.find_all("script", type="application/ld+json")

        result = {
            "Link": url,
            "daysSince": None,
            "jobDescriptionLength": 0,
        }

        description = soup.get_text(" ", strip=True)
        result["jobDescriptionLength"] = len(description)

        for script in scripts:
            try:
                payload = json.loads(script.string)
            except Exception:
                continue

            postings = payload if isinstance(payload, list) else [payload]
            for item in postings:
                if isinstance(item, dict) and item.get("@type") == "JobPosting":
                    result["datePosted"] = item.get("datePosted")
                    return result

        return result
    finally:
        driver.quit()


if __name__ == "__main__":
    sample_url = "https://www.indeed.com/viewjob?jk=b1c329181eab855c&from=shareddesktop_copy"
    print(scrape_job(sample_url))
