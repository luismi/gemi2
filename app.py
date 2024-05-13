# Import the required libraries
import google.generativeai as genai
import streamlit as st
from scrapegraphai.graphs import SmartScraperGraph

# Get OpenAI API key from user
openai_access_token = st.text_input("OpenAI API Key", type="password")

if openai_access_token:
    model = "gemini-1.0-pro-002"
    
    graph_config = {
        "llm": {
            "api_key": openai_access_token,
            "model": model,
        },
    }
    # Get the URL of the website to scrape
    url = st.text_input("Enter the URL of the website you want to scrape")
    # Get the user prompt
    user_prompt = st.text_input("What you want the AI agent to scrae from the website?")
    
    # Create a SmartScraperGraph object
    smart_scraper_graph = SmartScraperGraph(
        prompt=user_prompt,
        source=url,
        config=graph_config
    )
    # Scrape the website
    if st.button("Scrape"):
        result = smart_scraper_graph.run()
        st.write(result)