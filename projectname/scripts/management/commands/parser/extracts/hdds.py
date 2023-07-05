import re

def extract_hdds(title, details):
    manufacturer = 'неизвестно'
        
    parts = re.split(r"диск|HDD", title)
    if len(parts) > 1:
        string = re.sub(r"\(.*?\)", "", parts[1])
        string = re.sub(r"\b\d+Tb\b", "", string)
        string = re.sub(r"\b\d+Gb\b", "", string)
        string = re.sub(r"\bSATA-III\b", "", string)
        string = " ".join(string.split())
        manufacturer = string
        

    capacity = 'неизвестно' 
    parts = title.replace(',', '').replace(';', '').replace('/', ' ').split()
    for i in range(len(parts)):
        if parts[i].endswith("Tb") or parts[i].endswith("Gb"):
            capacity = parts[i]

    # print( manufacturer, capacity)

    return manufacturer, capacity