import requests
import json

class DataFetcher:
    def __init__(self):
        self.valid_url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        self.broken_url = "https://this-website-does-not-exist.com/api"

    def fetch_live_data(self, url):
        print(f"\n\t\t Attempting to fetch data from: {url}")
        
        try:
            response = requests.get(url, timeout=5)
            
            assert response.status_code == 200, f"Critical Failure: Server returned status {response.status_code}"
            
            # converting the raw web text into a python dictionary
            data = response.json()
            
            print("\t\t Data retrieved and parsed!")

            print(f"Bitcoin Price (USD): ${data['bpi']['USD']['rate']}")
            
        except requests.exceptions.RequestException as network_error:
            print(f"NETWORK ERROR: Failed to reach the server. Details: {network_error}")
            
        except AssertionError as assert_error:
            # Catches our custom tripwire if the server is online but returning bad codes
            print(f"VALIDATION ERROR: {assert_error}")
            
        except json.JSONDecodeError:
            # Catches scenarios where the server returns corrupted HTML instead of clean JSON
            print("DATA ERROR: The response was not valid JSON.")

if __name__ == "__main__":
    fetcher = DataFetcher()
    #pass
    fetcher.fetch_live_data(fetcher.valid_url)
    #fail
    fetcher.fetch_live_data(fetcher.broken_url)