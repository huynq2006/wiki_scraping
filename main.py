from fetcher import fetch_html
from parser import get_soup, get_content_div, get_table_cont

from extractor.content_extractor import extract_content
from extractor.table_extractor import extract_table_content

URL = input("Insert URL: ")

def main():
    html = fetch_html(URL)
    soup = get_soup(html)
    content_div = get_content_div(soup)
    table_cont = get_table_cont(soup)

    content = extract_content(content_div)
    tables = extract_table_content(table_cont)

    print("=== TEST SCRAPE ===")
    print("Sections:", len(content))
    print("Tables:", len(tables))

    # sample output (guard against missing content)
    if content:
        print("\n--- First section ---")
        print(content[0]["Title"])
        print(content[0]["Content"][:2])
    else:
        print("No content sections found.")

if __name__ == "__main__":
    main()
