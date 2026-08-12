import requests
import urllib.parse

def shorten_url(long_url: str) -> str:
    try:
        encoded_url = urllib.parse.quote(long_url)
        api_url = f"http://tinyurl.com/api-create.php?url={encoded_url}"

        response = requests.get(api_url, timeout=5)

        if response.status_code == 200:
            return response.text
        else:
            return "Could not shorten the link.Please check the URL."
    except Exception as e:
        return f"Error: {str(e)}"