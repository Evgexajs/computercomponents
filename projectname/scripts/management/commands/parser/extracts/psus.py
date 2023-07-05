def extract_psus(title, details):
    temp = title.replace('  ', ' ')
    manufacturer = 'неизвестно'
    if 'Блок питания' in temp:
        manufacturer = temp.split('Блок питания')[1].split(' ')[2].strip()
    elif 'блок питания' in title:
        manufacturer = temp.split('блок питания')[1].split(' ')[2].strip()

    wattage = 'неизвестно'
    if 'Блок питания' in temp:
        wattage = temp.split('Блок питания')[1].split(' ')[1].strip()
    elif 'блок питания' in title:
        wattage = temp.split('блок питания')[1].split(' ')[1].strip()

    return manufacturer, wattage