from fetcher import fetch_html
from parser import get_soup, get_content_div

from extractor.content_extractor import extract_content
from extractor.table_extractor import extract_table_content

URL = input("Insert URL: ")

def main():
    html = fetch_html(URL)
    soup = get_soup(html)
    content_div = get_content_div(soup)

    content = extract_content(content_div)
    tables = extract_table(content_div)

    print("=== TEST SCRAPE ===")
    print("Sections:", len(content))
    print("Tables:", len(tables))

    # in 1 đoạn mẫu
    print("\n--- First section ---")
    print(content[0]["title"])
    print(content[0]["content"][:2])

if __name__ == "__main__":
    main()
