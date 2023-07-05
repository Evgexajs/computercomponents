import re

def extract_ssds(title, details):
    manufacturer = 'неизвестно'
        
    parts = re.split(r"SSD ", title)
    if len(parts) > 1:
        string = re.sub(r"\b\d+Gb\b|\b\d+TB\b|\b\d+Tb\b|\b\d+Гб\b", "", parts[1])
        string = re.sub(r"\bNVMe\b|\bSATA\d\b|\bMVMe\b", "", string)
        string = re.sub(r"\bM.2\b", "", string)
        string = re.sub(r"\(.*?\)", "", string)
        string = " ".join(string.split())
        manufacturer = string
        

    capacity = 'неизвестно' 
    parts = title.replace(',', '').replace(';', '').replace('/', ' ').split()
    for i in range(len(parts)):
        if parts[i].endswith("Tb") or parts[i].endswith("Gb") or parts[i].endswith("TB") or parts[i].endswith("Гб"):
            capacity = parts[i]

    # print( manufacturer, capacity)

    return manufacturer, capacity