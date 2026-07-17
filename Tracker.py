import requests
from bs4 import BeautifulSoup
import google.generativeai as genai  # Or openai, depending on your preferred API

# 1. Configure your AI API Key
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel('gemini-pro')

# 2. Target a messy university event page (e.g., JNU CSRD / School of Social Sciences)
target_url = "https://www.jnu.ac.in/sss/csrd-events" 

def run_ai_curator(url):
    try:
        # Fetch the webpage text
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        page_text = soup.get_text() # This grabs all the messy, unformatted text
        
        # Craft the prompt for the AI
        prompt = f"""
        You are an elite academic research assistant. 
        Analyze the following raw text scraped from a university event directory.
        
        Identify all UPCOMING academic events (workshops, seminars, conferences, calls for papers) 
        related to Geography, Sociology, Management, Anthropology, History, or GIS.
        
        Today's date is {datetime.date.today().strftime('%B %d, %Y')}. 
        Disregard any events that have already happened.
        
        Format the output as a clean markdown table with these columns:
        | Institution | Department | Event Title | Event Date/Deadline | Status (Upcoming/Active) | Source Link |
        
        Raw webpage text:
        {page_text[:8000]}  # Feeding the first 8000 characters to prevent token overflow
        """
        
        # Let the AI do the heavy lifting
        ai_response = model.generate_content(prompt)
        return ai_response.text

    except Exception as e:
        return f"Error gathering data: {str(e)}"

# Run the curation
print(run_ai_curator(target_url))
