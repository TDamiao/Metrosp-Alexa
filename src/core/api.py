import requests
import os

API_URL = os.environ.get("API_URL", "https://ale-jr-metro-sp-api.herokuapp.com/")

def get_status():
    """
    Fetches the status of the São Paulo metro and CPTM lines from the API.
    """
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None
