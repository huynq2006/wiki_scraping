from bs4 import BeautifulSoup

def get_content_div(html):
    soup = BeautifulSoup(html.text, "html.parser")
    content_div = soup.find("div", class_="mw-content-ltr mw-parser-output")
    
def get_table_cont(html):
    soup = BeautifulSoup(html.text, "html.parser")
    table_cont = soup.find("table", class_ = "nowraplinks hlist mw-collapsible expanded navbox-inner mw-made-collapsible")
    