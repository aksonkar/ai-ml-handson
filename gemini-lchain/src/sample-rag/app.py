import google.generativeai as genai
from tavily import TavilyClient
import json
from datetime import datetime


genai.configure(api_key="AIzaSyAVCWPVVsF5vBOJZlIpnjtLX-Qnu1Fwwp8")
tavily_client = TavilyClient(api_key="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")
model = genai.GenerativeModel("gemini-2.0-flash-001")
def generate_response(prompt: str) -> str:
    """
    Generate a response using the Gemini model.
    
    Args:
        prompt (str): The input prompt for the model.
        
    Returns:
        str: The generated response from the model.
    """
    response = model.generate_content(prompt)
    return response.text

def generate_summary(prompt: str) -> str:
    """
    Generate a summary using the Gemini model.
    
    Args:
        prompt (str): The input prompt for the model.
        
    Returns:
        str: The generated summary from the model.
    """
    response = model.generate_content(prompt)
    return response.text

def search_web(query: str) -> str:
    """
    Search the web using Tavily and return the first result.
    
    Args:
        query (str): The search query.
        
    Returns:
        str: The first search result.
    """
    search_result = tavily_client.search(query, max_results=2)
    for result in search_result['results']:
        print(f"Title: {result['title']}")
        print(f"URL : {result['url']}")
        print(f"Content : {result['content'][:100]}...")
        print()
    return search_result['results'][0]['content'] if search_result['results'] else "No results found."

def main():
    """Main function to demonstrate the usage of the above functions."""
    prompt = "What is the capital of France?"
    print("Generating response...")
    response = generate_response(prompt)
    print(f"Response: {response}")
    print("Generating summary...")
    summary = generate_summary(prompt)    
    print(f"Summary: {summary}")    
    print("Searching the web...")    
    search_result = search_web(prompt)
    print(f"Search Result: {search_result}")    
if __name__ == "__main__":
    main()


# This code is a simple application that uses the Gemini model from Google Generative AI and Tavily to generate responses, summaries, and search the web. 
# It demonstrates how to configure the model, generate text, and perform web searches using the Tavily client. 
# The main function showcases the usage of these functions by generating a response, summary, and performing a web search based on a given prompt.
# Make sure to replace the API keys with your own before running the code.
# The code is structured to be easily extendable for more complex applications, such as integrating with web frameworks or adding more functionalities like handling user inputs, storing results, etc.
# It is also
