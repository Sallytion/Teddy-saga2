import csv
from jobspy import scrape_jobs

jobs = scrape_jobs(
    site_name=["linkedin"], # "glassdoor", "bayt", "naukri", "bdjobs"
    search_term="software engineer",
    google_search_term="software engineer jobs near San Francisco, CA since yesterday",
    location="India",
    results_wanted=100,
    hours_old=1,
    linkedin_fetch_description=True 
)
print(f"Found {len(jobs)} jobs")
print(jobs.head())
jobs.to_csv("jobs.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False) # to_excel
