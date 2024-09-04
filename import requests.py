import requests

def fetch_google_homepage():
    url = "https://www.google.com"
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Return the HTML content of the page
        return response.text
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"An error occurred: {err}"

if __name__ == "__main__":
    # Fetch the content of the Google homepage
    html_content = fetch_google_homepage()
    
    # Print the HTML content
    print(html_content)
