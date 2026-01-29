import requests

url = "https://vi.wikipedia.org/wiki/Trí_tuệ_nhân_tạo"
headers = {
    "User-Agent": "StudentProject/1.0 (contact: huynq1411@gmail.com)"
}

html = requests.get(url, headers=headers)
