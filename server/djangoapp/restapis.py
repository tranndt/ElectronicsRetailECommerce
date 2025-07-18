# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5002/")

def get_request(endpoint, **kwargs):
    """Add code for get requests to back end"""
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params += f"{key}={value}&"
    
    request_url = backend_url + endpoint + "?" + params
    
    print(f"GET from {request_url}")
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        # If any error occurs
        print(f"Network exception occurred: {e}")
        return None

def analyze_review_sentiments(text):
    """Add code for retrieving sentiments"""
    import urllib.parse
    encoded_text = urllib.parse.quote(text, safe='')
    # Use the environment variable or fallback to localhost
    base_url = sentiment_analyzer_url if sentiment_analyzer_url else "http://localhost:5002/"
    if not base_url.endswith('/'):
        base_url += '/'
    request_url = base_url + "analyze/" + encoded_text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        result = response.json()
        return result
    except Exception as e:
        print(f"Sentiment analysis error: {e}")
        return None

def post_review(data_dict):
    """Add code for posting review"""
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as e:
        print(f"Network exception occurred {e}")
        return None
