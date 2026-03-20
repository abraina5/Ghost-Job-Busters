import pandas as pd
from scraper import scrape_job
import os
print("RUNNING FILE:", os.path.abspath(__file__))

df = pd.DataFrame(columns=['Link', 'daysSince', 'jobDescriptionLength', 'Score'])
print("RUNNING NEW DATA.PY FILE")
url = "https://www.indeed.com/viewjob?jk=b1c329181eab855c"

data = scrape_job(url)

print("SCRAPED DATA:", data)

# Placeholder score
data["Score"] = 0

df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)

print(df)
