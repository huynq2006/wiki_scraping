from bs4 import BeautifulSoup

def get_soup(html):
    soup = BeautifulSoup(html.text, "html.parser")
    return soup

def get_content_div(soup):
    content_div = soup.find("div", class_="mw-content-ltr mw-parser-output")
    return content_div
    
def get_table_cont(soup):
    # Try a few ways to find a navbox/collapsible table. Fall back to the first table if necessary.
    # 1) Very specific class used previously
    table = soup.find("table", class_ = "nowraplinks hlist mw-collapsible expanded navbox-inner mw-made-collapsible")
    if table:
        return table

    # 2) Any table that contains 'navbox' in its class list
    table = soup.find(lambda tag: tag.name == 'table' and tag.get('class') and any('navbox' in c for c in tag.get('class')))
    if table:
        return table

    # 3) Last resort: return the first table on the page
    table = soup.find('table')
    return table
    