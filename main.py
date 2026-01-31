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
    for i in range(0, len(content)):
        if content:
            print("\n--- Section {} ---".format(i+1))
            print(content[i]["Title"])
            print(content[i]["Content"])
        else:
            print("No content sections found.")
            
    for j in range(0, min(1, len(tables))):
        if not tables.empty:
            print("\n--- Table {} ---".format(j+1))
            print("Heading:", tables.iloc[j]["Heading"])
            print("Table data:", tables.iloc[j]["Table"])
        else:
            print("No tables found.")

if __name__ == "__main__":
    main()
