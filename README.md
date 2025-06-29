# LeadSight AI - Smart Lead Enrichment & Prioritization Tool

LeadSight AI is a high-impact, 5-hour project built to enhance the basic scraping functionality of existing lead generation tools like SaaSquatchLeads. It offers enriched and prioritized lead data to help B2B sales teams find and focus on high-value contacts faster.

 Features

Domain Scraping: Start with a list of company websites.

 Lead Enrichment: Uses WHOIS and LinkedIn search to enrich leads.

 Lead Scoring: Prioritizes leads based on email presence, organization data, and role.

 CSV Export: Filter and export leads based on score, title, location.

 Simple UI: Streamlit-based interface for ease of use.

 Quick Start



1. Install Dependencies

pip install -r requirements.txt

2. Run the App

streamlit run app.py

 Example Usage

Input or upload a list of domains/company names.

Click "Enrich Leads" to get:

Emails from WHOIS

Organization info

LinkedIn profiles

Leads are scored & displayed in a table.

Use filters to export only high-quality leads.

 Tech Stack

Tool

Purpose

Python

Core programming

Streamlit

Frontend UI

WHOIS

Get domain registration info

Google Search

Get LinkedIn profile URL

Pandas

Data filtering/export

 Files Overview

leadsight-ai/
│
├── app.py            # Streamlit frontend
├── enrich.py         # WHOIS and LinkedIn scraping
├── utils.py          # Scoring, deduplication, helpers
├── requirements.txt  # Python dependencies


 Sample Input Format

domain
example.com
github.com
openai.com

 To Do (Post-MVP)

CRM Integration (HubSpot, Salesforce)

Automated Lead Validation

Scheduled Data Sync

Company Revenue/Funding Enrichment

 Contributing

PRs welcome! If you have suggestions, feel free to fork the repo and submit a pull request.

 Disclaimer

This tool is for educational use. Ensure ethical use and compliance with data privacy laws (e.g., GDPR, CCPA).

 Author

Made with ❤️ by [Mantasha]
