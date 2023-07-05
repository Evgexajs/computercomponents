import re

def extract_rams(title, details):
    manufacturer = 'неизвестно'
    parts = re.split(r"память", title)
    if len(parts) > 1:
        string = re.sub(r"\(.*?\)", "", parts[1])
        string = re.sub(r"\b\d+Tb\b", "", string)
        string = re.sub(r"\b\d+Gb\b", "", string)
        string = re.sub(r"\b\d+MHz\b", "", string)
        string = re.sub(r"\b\d+GB\b", "", string)
        string = re.sub(r"DDR4", "", string)
        string = re.sub(r"DDR5", "", string)
        string = re.sub(r"2x16Gb", "", string)
        string = re.sub(r"4x16Gb", "", string)
        string = re.sub(r"2x8Gb", "", string)
        string = re.sub(r"4x8Gb", "", string)
        string = re.sub(r"2x4Gb", "", string)
        string = re.sub(r"2x32Gb", "", string)
        string = re.sub(r"2x16GB", "", string)
        string = re.sub(r"4x16GB", "", string)
        string = re.sub(r"4x8GB", "", string)
        string = re.sub(r"2x8GB", "", string)
        string = re.sub(r"2x4GB", "", string)
        string = re.sub(r"2x32GB", "", string)
        string = re.sub(r"KIT", "", string)
        string = re.sub(r"\bCL+\d\d\b", "", string)
        string = re.sub(r"\bSATA-III\b", "", string)
        string = " ".join(string.split())
        manufacturer = string
        
    capacity = 'неизвестно' 
    parts = title.replace(',', '').replace(';', '').replace('/', ' ').split()
    for i in range(len(parts)):
        if parts[i].endswith("Gb"):
            capacity = parts[i].replace('(', '').replace(')', '').replace('/', '').replace(';', '')

    return manufacturer, capacity