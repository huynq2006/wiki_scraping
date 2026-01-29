import re
import pandas as pd

def extract_table_content(table_cont):
    ## TABLE EXTRACTION
    tables = table_cont.find_all("table")

    table_data = []

    heading_tags = ['h1', 'h2', 'h3', 'h4', 'h5']

    current_heading = None
    # for table in tables:
    #     table_row = []
        
    #     body = table.find("tbody")
    #     rows = body.find_all('tr') if body else table.find_all('tr')
    #     for row in rows:
    #         cells = row.find_all(["th", "td"])
    #         row_data = [cell.get_text(" ", strip=True) for cell in cells]

    #         if row_data:
    #             table_row.append(row_data)

    #     if table_row:
    #         table_data.append(table_row)

    for element in table_cont.find_all(heading_tags + ["table"], recursive=True):
        if element.name in heading_tags:
            current_heading = element.get_text(strip=True)
        
        elif element.name == 'table':
            rows_data = []

            body = element.find("tbody")
            rows = body.find_all("tr") if body else element.find_all("tr")

            for row in rows:  
                cells = row.find_all(['th', 'td'])
                row_data = [cell.get_text(strip=True) for cell in cells]
                if row_data:
                    rows_data.append(row_data)

            if row_data:
                table_data.append({
                    "Heading" : current_heading,
                    "Table" : rows_data
                })


    data_fr = pd.DataFrame(table_data)

    return data_fr

