# Import the required libraries
import google.generativeai as genai
import streamlit as st
from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.utils import prettify_exec_info

# Get OpenAI API key from user
openai_access_token = st.text_input("OpenAI API Key", type="password")

if openai_access_token:
    model = "gemini-pro"
    
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
        
        # Get graph execution info
        graph_exec_info = smart_scraper_graph.get_execution_info()
        st.write(prettify_exec_info(graph_exec_info))