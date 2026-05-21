# Cold Mail Generator

A Streamlit app that generates personalized cold outreach emails from a job posting URL. The app scrapes the job page, extracts role requirements with Groq + LangChain, matches relevant portfolio links from a local CSV, and writes a tailored cold email for a software services company.

## GitHub Description

AI-powered cold email generator using Streamlit, LangChain, Groq, and Python.

## GitHub Topics

`streamlit` `langchain` `groq` `generative-ai` `cold-email` `python` `job-scraper` `llm-app` `sales-automation` `ai-tools`

## Resume / LinkedIn Project Topic

AI-Powered Cold Email Generator for Job-Based Sales Outreach

## Resume / LinkedIn Description

Built a generative AI web app that analyzes public job posting URLs, extracts role requirements, matches relevant portfolio links, and generates personalized cold outreach emails using Python, Streamlit, LangChain, and Groq.

## Features

- Accepts a public job posting URL.
- Extracts role, experience, skills, and job description from the page.
- Matches job skills with portfolio links from `app/resource/my_portfolio.csv`.
- Generates a personalized cold email using Groq.
- Uses a lightweight local portfolio matcher for faster runtime.

## Tech Stack

- Python
- Streamlit
- LangChain
- Groq API
- Pandas
- Requests

## Project Structure

```text
app/
  chains.py          # Groq + LangChain prompts
  main.py            # Streamlit app
  portfolio.py       # Portfolio link matching
  utils.py           # URL fetching and text cleaning
  resource/
    my_portfolio.csv # Portfolio examples
requirements.txt
```

## Setup

Clone or download the project, then open a terminal in the project folder.

```powershell
cd "C:\Projects\Coldemail generator"
```

Create and activate a virtual environment.

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Create an `app/.env` file and add your Groq API key.

```env
GROQ_API_KEY=your_groq_api_key_here
```

Do not wrap the key in quotes or angle brackets.

## Run

```powershell
.\.venv\Scripts\python.exe -m streamlit run app/main.py
```

Open the local Streamlit URL shown in the terminal, usually:

```text
http://localhost:8501
```

## Usage

1. Paste a public job posting URL.
2. Click `Submit`.
3. Review the generated cold email.
4. Copy and customize the email before sending.

## Notes

- Some job sites block automated scraping. If one URL fails, try another public job posting page.
- Keep your Groq API key private. If you accidentally share it, revoke it and create a new one.
- The app uses `llama-3.3-70b-versatile` because older Groq tutorial models may be decommissioned.

## License

This project is based on the Codebasics cold email generator tutorial repository. Check the original repository license and terms before commercial use.
