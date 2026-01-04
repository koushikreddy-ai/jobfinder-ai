Features

🔎 Scrapes multiple job sites including Indeed and SimplyHired

🤖 Summarizes each job posting using OpenAI GPT

📧 Sends a professional HTML email with job links and summaries

⚡ Fully text-based, lightweight, and CPU-friendly

💼 Customizable for any job title, location, or email address

Demo

Run the script:

python jobfinder.py


Output in terminal:

Fetching jobs from Indeed...
Fetching jobs from SimplyHired...
Found 10 jobs. Summarizing and sending email...
Email sent successfully!


Check your inbox to see a beautifully formatted list of AI job opportunities.

Installation

Clone the repository:

git clone https://github.com/koushikreddy-ai/ai_job_finder_pro.git
cd ai_job_finder_pro


Install dependencies:

pip install requests beautifulsoup4 openai pandas lxml

Configuration

Open job_finder_pro.py

Set the following variables at the top:

JOB_KEYWORD = "AI Engineer"       # Job title to search
LOCATION = "Delaware"             # Job location
YOUR_EMAIL = "your_email@gmail.com"  # Email to send results
EMAIL_PASSWORD = "your_app_password" # Gmail App Password
OPENAI_API_KEY = "your_openai_api_key" # OpenAI API Key


💡 Tip: For Gmail, enable 2FA and create an App Password for secure email sending.

How It Works

Scraping: The script fetches job postings from Indeed and SimplyHired.

Summarization: Each job description is summarized in 2 lines using GPT.

Email Formatting: A professional HTML email is generated.

Notification: The email is sent to the configured Gmail address.

Technologies Used

Python 3.10+

Requests & BeautifulSoup4 (web scraping)

OpenAI GPT-3.5-turbo (AI summarization)

Pandas (data handling)

SMTP (email automation)

Potential Enhancements

Include LinkedIn, Glassdoor, or other job platforms

Add daily automation via cron or Task Scheduler

Add Slack/WhatsApp notifications for instant job alerts

Include filters for remote jobs, full-time/part-time, or salary range

License

This project is MIT licensed — feel free to use, modify, and contribute!

Contact

Koushik Reddy
GitHub: https://github.com/koushikreddy-ai

Email: koushikreddyofc@gmail.com
