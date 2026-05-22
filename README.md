# AI-Powered Cold Email Generator

## Streamlit + LangChain + Groq | Python
A generative AI application built using Streamlit, LangChain, Groq API, and a modular Python pipeline for job-based cold email generation.

This project generates personalized cold outreach emails from public job posting URLs:<br>

-Job Posting URL<br>
-Extracted Role Details<br>
-Required Skills<br>
-Relevant Portfolio Links<br>
-Generated Cold Email<br>

The system analyzes a job description, extracts structured requirements, matches relevant portfolio examples, and produces a professional business development email.

## Key Features:

🔥 Generative AI Email Creation:<br>
->Uses Groq LLM through LangChain<br>
->Extracts job role, experience, skills, and description<br>
->Generates personalized cold outreach emails<br>
->Adds relevant portfolio links based on required skills<br>

All combined into a simple Streamlit web application for fast cold email generation.<br>

🧠 Job Posting Intelligence<br>
The app analyzes public job posting pages:<br>
->Fetches job page content<br>
->Cleans scraped text<br>
->Extracts structured job information<br>
->Prepares role-specific input for the email generation chain<br>
"Cold emails are generated using extracted job requirements and matched software service capabilities."<br>

## 📊 Application Workflow
*User enters a public job posting URL<br>
*App fetches and cleans the webpage content<br>
*LangChain extracts structured job details<br>
*Portfolio matcher selects relevant project links<br>
*Groq generates a personalized cold email<br>
*Final email is displayed in Streamlit<br>

## ⚙️ Configurable App Pipeline
*Groq API key through `.env` file<br>
*Streamlit web interface<br>
*Prompt-based job extraction<br>
*Prompt-based email generation<br>
*Local CSV-based portfolio matching<br>
*Fast URL fetching with browser-like request headers<br>

## 📁 Project Structure:
project/<br>
├── app/<br>
│   ├── chains.py<br>
│   ├── main.py<br>
│   ├── portfolio.py<br>
│   ├── utils.py<br>
│   ├── .env<br>
│   └── resource/<br>
│       └── my_portfolio.csv<br>
├── imgs/<br>
├── requirements.txt<br>
├── README.md<br>
├── email_generator.ipynb<br>
├── tutorial_chromadb.ipynb<br>
└── tutorial_groq.ipynb<br>

## 📈 Project Output:
From the generated result:<br>
"The app creates a personalized cold email for a software services company based on the target company's hiring needs."<br>
->Extracted job role and requirements<br>
->Matched technical skills<br>
->Relevant portfolio links<br>
->Professional outreach message<br>

## Summary:
| Area | Details |
| --- | --- |
| **Project Type** | Generative AI Web App |
| **Frontend** | Streamlit |
| **LLM Provider** | Groq |
| **Framework** | LangChain |
| **Language** | Python |
| **Input** | Public Job Posting URL |
| **Output** | Personalized Cold Email |

## 🏗️ Installation:
git clone &lt;your-repo-url&gt;<br>
cd "Coldemail generator"<br>
py -3.11 -m venv .venv<br>
.\.venv\Scripts\python.exe -m pip install -r requirements.txt<br>

## ⚙️ Configuration:
Create an `.env` file inside the `app` folder:<br>

app/.env<br>

Add your Groq API key:<br>

GROQ_API_KEY=your_groq_api_key_here<br>

Do not use quotes, spaces, or angle brackets around the API key.<br>
Keep your API key private and do not upload it to GitHub.<br>

## ▶️ Running the App:
.\.venv\Scripts\python.exe -m streamlit run app/main.py<br>

### Outputs:
*Streamlit local web app<br>
*Extracted job details<br>
*Matched portfolio links<br>
*Generated cold email<br>

## 🧪 Test URL:
Use this sample job posting URL:<br>

https://job-boards.greenhouse.io/greenhouse/jobs/7296545<br>

## 🔍 Usage:
1. Open the Streamlit app<br>
2. Paste a public job posting URL<br>
3. Click Submit<br>
4. Wait for job extraction and email generation<br>
5. Review the generated cold email<br>
6. Customize before sending<br>

## 🧠 Model Pipeline (Summary)
"The core pipeline uses LangChain with Groq to extract structured job details from scraped webpage text. The extracted skills are matched with portfolio links from a local CSV file, and the final prompt generates a personalized cold outreach email."<br>

## 📌 Future Improvements
->Add email tone selection<br>
->Add subject line generation<br>
->Add copy-to-clipboard button<br>
->Support manual job description input<br>
->Deploy on Streamlit Community Cloud<br>
->Add CRM export support<br>

## License
This project is based on the Codebasics cold email generator tutorial repository. Check the original repository license and terms before commercial use.
