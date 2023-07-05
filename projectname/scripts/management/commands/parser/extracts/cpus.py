def extract_cpus(title, details):
    manufacturer = 'неизвестно'
    if 'Процессор' in title:
        manufacturer = title.split('Процессор')[1].split(' ')[1].strip()
    elif 'процессор' in title:
        manufacturer = title.split('процессор')[1].split(' ')[1].strip()

    socket = 'неизвестно'
    cores = 'неизвестно'

    socket = details.split(',')[0].replace('Socket', '').replace('socket', '').replace('сокет', '').replace('Сокет', '').replace(' ', '')
    
    parts = details.replace(',', '').replace(';', '').replace('/', ' ').split()
    for i in range(len(parts)):
        if parts[i].endswith("поточный"):
            cores = parts[i].replace('-поточный', '')
        elif parts[i].endswith("ядерный"):
            cores = parts[i].replace('-ядерный', '')
        elif parts[i].endswith("потоков"):
            if any(char.isdigit() for char in parts[i + 1]):
                cores = parts[i + 1]
            else:
                cores = parts[i - 1]
        elif parts[i].endswith("потока"):
            cores = parts[i - 1]

    return manufacturer, socket, cores