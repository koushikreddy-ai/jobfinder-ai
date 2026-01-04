import requests
from bs4 import BeautifulSoup
import openai
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

# ========== CONFIG ==========
JOB_KEYWORD = "AI Engineer"
LOCATION = "Delaware"
YOUR_EMAIL = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
OPENAI_API_KEY = "your_openai_api_key"
# ============================

openai.api_key = OPENAI_API_KEY

# --- Step 1: Scrape Indeed ---
def fetch_indeed_jobs(keyword, location, max_jobs=5):
    url = f"https://www.indeed.com/jobs?q={keyword.replace(' ','+')}&l={location.replace(' ','+')}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    jobs = []

    for job_card in soup.find_all('a', attrs={'class':'jcs-JobTitle'})[:max_jobs]:
        title = job_card.text.strip()
        link = "https://www.indeed.com" + job_card['href']
        jobs.append({'title': title, 'link': link})
    return jobs

# --- Step 2: Scrape SimplyHired ---
def fetch_simplyhired_jobs(keyword, location, max_jobs=5):
    url = f"https://www.simplyhired.com/search?q={keyword.replace(' ','+')}&l={location.replace(' ','+')}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    jobs = []

    for job_card in soup.find_all('a', attrs={'class':'SerpJob-link'})[:max_jobs]:
        title = job_card.text.strip()
        link = "https://www.simplyhired.com" + job_card['href']
        jobs.append({'title': title, 'link': link})
    return jobs

# --- Step 3: Summarize jobs using OpenAI ---
def summarize_job(title, link):
    prompt = f"Summarize this job posting in 2 lines: {title} {link}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content":prompt}],
            max_tokens=60
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return "Summary unavailable"

# --- Step 4: Build HTML email ---
def build_email(jobs):
    html = "<h2>AI Job Finder Pro: Today's Job Links</h2><ul>"
    for job in jobs:
        summary = summarize_job(job['title'], job['link'])
        html += f"<li><a href='{job['link']}'>{job['title']}</a><br>{summary}</li><br>"
    html += "</ul>"
    return html

# --- Step 5: Send email ---
def send_email(html_body):
    msg = MIMEMultipart('alternative')
    msg['From'] = YOUR_EMAIL
    msg['To'] = YOUR_EMAIL
    msg['Subject'] = "Daily AI Job Links"

    msg.attach(MIMEText(html_body, 'html'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(YOUR_EMAIL, EMAIL_PASSWORD)
    server.send_message(msg)
    server.quit()
    print("Email sent successfully!")

# --- Step 6: Main program ---
if __name__ == "__main__":
    print("Fetching jobs from Indeed...")
    jobs = fetch_indeed_jobs(JOB_KEYWORD, LOCATION)
    print("Fetching jobs from SimplyHired...")
    jobs += fetch_simplyhired_jobs(JOB_KEYWORD, LOCATION)

    print(f"Found {len(jobs)} jobs. Summarizing and sending email...")
    html_email = build_email(jobs)
    send_email(html_email)
