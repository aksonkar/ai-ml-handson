import google.generativeai as genai
from tavily import TavilyClient
import json
from datetime import datetime


genai.configure(api_key="AIzaSyAVCWPVVsF5vBOJZlIpnjtLX-Qnu1Fwwp8")
tavily_client = TavilyClient(api_key="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")
model = genai.GenerativeModel("gemini-2.0-flash-001")


def check_the_claim(prompt: str) -> str:
    """
    Check the claim using the Gemini model and Tavily search.
    
    Args:
        claim (str): The claim to be checked.
        
    Returns:
        str: The result of the fact-checking process.
    """
    # Generate a response from the model
    response = generate_response(prompt)
    
    
    
    # Combine the results
   
    
    return response


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

def search_web(query: str) -> str:
    """
    Search the web using Tavily and return the first result.
    
    Args:
        query (str): The search query.
        
    Returns:
        str: The search results as string.
    """
    search_result = tavily_client.search(query, max_results=2)
    returned_results = search_result['results'] if 'results' in search_result else []
    if not returned_results:
        return "No results found."
    # Print the search results
    print("Search Results:")
    print("----------------")
    print(f"Total Results: {len(returned_results)}")
    print(f"Timestamp: {datetime.now().isoformat()}")
    # convert the results into a readable string format
    results_string = "\n".join([f"Title1: {result['title']} - \n URL: {result['url']}\n{result['content']}..." for result in returned_results])
    
    # Print each result
    print("\nDetailed Results:")
    print("----------------")
    print(f"Total Results: {len(search_result['results'])}")
    print(f"Timestamp: {datetime.now().isoformat()}")
    # Print each result with title, URL, and content snippet
    print("Results:")
    for result in search_result['results']:
        print(f"Title: {result['title']}")
        print(f"URL : {result['url']}")
        print(f"Content : {result['content'][:100]}...")
        print()
    return results_string if results_string else "No results found."

def main():
    """Main function to check the claim."""
    claim = "Is RAG still relevant as of today?."
    print("Gathering evidence for the claim...")

    evidence = search_web(claim); 

    prompt = f"""
    You are a professional fact-checker. Analayze this claim against the evidence:

    CLAIM:{claim}

    EVIDENCE:{evidence}

    Provide a fact-check analysis with:

    1. VERDICT: Choose ONE of these:
        -TRUE: Claim is factually accuract
        -FALSE: Claim is factually incorrect
        -PARTIALLY TRUE: Claim has some triuth but is misleading
        -UNVERIFIED: Insufficient evidence to determine accuracy
        -OUTDATED: Claim was trye but circumstances have changed

    2. CONFIDENCE: High/Medium/Low

    3. EXPLANATION: Clear 2-3 lines sentence explanation of your verdict

    4. KEY EVIDENCE: Brief summary of the most important evidence

    keep it concise and factual
    """
    result = check_the_claim(prompt)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
    # Uncomment the line below to run the main function