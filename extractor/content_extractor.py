import re

def extract_content(content_div):
    data = []

    # CONTENT TEXT

    current_section = None

    for div in content_div.find_all(['h2', 'p', 'ul']):

        # for div in content_div.find_all(recursive=False):
        #     print(div.name)
            
        if div.name == 'h2':
            span = div.find("span", class_="mw-headline")
            title = span.get_text(strip=True) if span else ""
            current_section = {
                "Title": title,
                "Content": []
            }
            data.append(current_section)

        elif div.name == 'p' and current_section:

            for sup in div.find_all("sup"):
                    sup.decompose()

            text1 = div.get_text(" ",strip=True)
            text1 = re.sub(r'\s+([,.;:!?])', r'\1', text1)
            text1 = re.sub(r'([,.;:!?])(?=\S)', r'\1 ', text1)

            if text1:
                current_section["Content"].append(text1)
                

        elif div.name == 'ul' and current_section:
            for li in div.find_all('li'):

                for a in li.find_all("a"):
                    a.replace_with(a.get_text(strip=True))
                    
                text2 = li.get_text(strip=True)
                text2 = re.sub(r'\s+([,.;:!?])', r'\1', text2)
                current_section["Content"].append(text2)

    # clear_data = []

    # for cleared_data in data:
    #     if cleared_data["Title"]:
    #         clear_data.append(cleared_data["Title"])

    #     clear_data.extend(cleared_data["Content"])

    # clear_data = "\n".join(clear_data)
    
    return data