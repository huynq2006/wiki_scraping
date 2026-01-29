import requests

def fetch_html(url):
    headers = {
        "User-Agent": "StudentProject/1.0 (contact: huynq1411@gmail.com)"
    }
    html = requests.get(url, headers=headers)
    return html
