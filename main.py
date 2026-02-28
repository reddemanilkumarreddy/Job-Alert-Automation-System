import requests
import json
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- Email Configuration ---
EMAIL_ADDRESS = "reddemanilkumarreddy4@gmail.com"   # Replace with your email
EMAIL_PASSWORD = "aurn rspi qmme artg"     # For Gmail, use an App Password
EMAIL_TO = "anilkumarreddyreddem@gmail.com"   # The email where you want to receive notifications
EMAIL_SUBJECT = "Amazon Job Alert"

URL = "https://www.amazon.jobs/en/search.json?country=GBR&loc_query=United%20Kingdom&radius=1000km&offset=0&result_limit=50"

# Step 1: Fetch jobs
def fetch_jobs():
    response = requests.get(URL)
    return response.json()["jobs"]

# Step 2: Filter jobs based on keywords
def filter_jobs(jobs):
    keywords = ["shift Manager", "Area Manager", "support engineer", "cloud support", "aws cloud" ]
    return [job for job in jobs if any(k in job["title"] for k in keywords)]

# Step 3: Load previously seen jobs
def load_seen():
    if not os.path.exists("seen_jobs.json"):
        return []
    with open("seen_jobs.json", "r") as f:
        return json.load(f)

# Step 4: Save seen jobs
def save_seen(ids):
    with open("seen_jobs.json", "w") as f:
        json.dump(ids, f)

# Fetch and filter
jobs = fetch_jobs()
filtered_jobs = filter_jobs(jobs)

# Track new jobs
seen = load_seen()
new_jobs = []

for job in filtered_jobs:
    if job["id_icims"] not in seen:
        new_jobs.append(job)
        seen.append(job["id_icims"])

save_seen(seen)

print("New jobs found:", len(new_jobs))

# --- Step 2.3: Build dynamic email body ---
if new_jobs:
    body = "New Amazon Jobs Found:\n\n"
    for idx, job in enumerate(new_jobs, start=1):
        location = job.get("locations", "Unknown")
        city = "Unknown"

        if isinstance(location, list) and len(location) > 0:
            first_loc = location[0]
            if isinstance(first_loc, dict):
                city = first_loc.get("city", "Unknown")
            elif isinstance(first_loc, str):
                city = first_loc
        elif isinstance(location, str):
            city = location

        body += f"{idx}. {job['title']}, {city}\n"
        body += f"   Link: https://www.amazon.jobs{job.get('job_path','')}\n\n"
else:
    body = "No new jobs found today."

print(body)  # Optional: check the output before sending email

# --- Step 3.2: Create the email message ---
msg = MIMEMultipart()
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_TO
msg['Subject'] = EMAIL_SUBJECT

# Attach the job list body as plain text
msg.attach(MIMEText(body, 'plain'))

# --- Step 3.3: Send the email ---
if new_jobs:  # Only send if there are new jobs
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Gmail SMTP server
        server.starttls()                             # Start secure connection
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)   # Login
        server.send_message(msg)                      # Send the email
        server.quit()                                 # Close connection
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)
else:
    print("No new jobs today, email not sent.")