def extract_motherboards(title, details):
    manufacturer = 'неизвестно'
    if 'Материнская плата' in title:
        manufacturer = title.split('Материнская плата')[1].split(' ')[1].strip()
    elif 'материнская плата' in title:
        manufacturer = title.split('материнская плата')[1].split(' ')[1].strip()

    socket = 'неизвестно'
    size = 'неизвестно'
    
    parts = details.replace(',', '').replace(';', '').replace('/', ' ').split()
    for i in range(len(parts)):
        if parts[i].startswith("Socket") or parts[i].startswith("Sockel") or parts[i].startswith("socket") or parts[i].startswith("сокет") or parts[i].startswith("Сокет"):
            if not details.startswith("Socket"):
                socket = parts[i].replace('Socket', '').replace('socket', '').replace('сокет', '').replace('Сокет', '').replace(' ', '').replace('-', '')
            else:
                socket = details.split(',')[0].replace('Socket', '').replace('socket', '').replace('сокет', '').replace('Сокет', '').replace(' ', '').replace('-', '')
        elif parts[i].endswith("LGA"):
            socket = parts[i + 1]
        elif parts[i].startswith("AM4") or parts[i].startswith("AM5"):
            socket = parts[i]

        if parts[i].endswith("ATX"):
            size = parts[i]

    if size == 'неизвестно':
        size = 'ATX'

    return manufacturer, socket, size