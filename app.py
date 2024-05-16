# Import the required libraries
import os
import json
import pandas as pd
import google.generativeai as genai
import streamlit as st
from scrapegraphai.graphs import SmartScraperGraph


# Get OpenAI API key from user
openai_access_token = st.text_input("OpenAI API Key", type="password")


if openai_access_token:
    model = "gemini-pro"
    
    graph_config = {
        "llm": {
            "api_key": openai_access_token,
            "model": model
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

    # Added downloads buttons
    def add_download_options(result: str):
        """
        Adds download buttons for graph result.
        """
        st.download_button(
            label="Download JSON",
            data=json.dumps(result, indent=4),
            file_name="scraped_data.json",
            mime="application/json"
        )

        df = pd.DataFrame(result)
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="scraped_data.csv",
            mime="text/csv"
        )
        
    # Scrape the website
    if st.button("Scrape"):
        result = smart_scraper_graph.run()
        st.write("# Respuesta")
        st.write(result)
        add_download_options(result)
        