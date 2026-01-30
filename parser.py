from bs4 import BeautifulSoup

def get_soup(html):
    soup = BeautifulSoup(html.text, "html.parser")
    return soup

def get_content_div(soup):
    content_div = soup.find("div", class_="mw-content-ltr mw-parser-output")
    return content_div
    
def get_table_cont(soup):
    table_cont = soup.find("table", class_ = "nowraplinks hlist mw-collapsible expanded navbox-inner mw-made-collapsible")
    return table_cont
    