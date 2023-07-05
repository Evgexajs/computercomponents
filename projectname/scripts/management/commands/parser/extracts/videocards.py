def extract_videocards(title, details):
    manufacturer = 'неизвестно'
    if 'Видеокарта' in title:
        manufacturer = title.split('Видеокарта')[1].split(' ')[1].strip()

    memory_type = 'неизвестно'
    memory_capacity = 'неизвестно'
    memory_clock = 'неизвестно'

    parts = details.replace(',', '').replace(';', '').replace('/', ' ').split()
    memory_words = parts
    for word in memory_words:
        if word.startswith("GDD") or  word.startswith("HBM"):
            memory_type = word
            break
    
    for i in range(len(parts)):
        if parts[i].endswith("Mb"):
            memory_capacity = parts[i]
        elif parts[i].endswith("Мб"):
            memory_capacity = parts[i]
        elif parts[i].endswith("GB") and parts[i].endswith("RGB") != True:
            memory_capacity = parts[i]
        elif parts[i].endswith("Гб"):
            memory_capacity = parts[i]
        elif parts[i].endswith("ГБ"):
            memory_capacity = parts[i]

        if parts[i].endswith("Mhz"):
            memory_clock = parts[i]
        elif parts[i].endswith("MHz"):
            memory_clock = parts[i]
        elif parts[i].endswith("ГГц"):
            memory_clock = parts[i]
        elif parts[i].endswith("Мгц"):
            memory_clock = parts[i]
        elif parts[i].endswith("МГц"):
            memory_clock = parts[i]
        elif parts[i].endswith("Мбит/с"):
            memory_clock = parts[i]

        if any(char.isdigit() for char in memory_capacity) != True and memory_capacity != 'неизвестно':
            memory_capacity = parts[i - 1] + parts[i]

        if any(char.isdigit() for char in memory_clock) != True and memory_clock != 'неизвестно':
            memory_clock = parts[i - 1] + parts[i]

    if memory_type == 'неизвестно':
        memory_type = 'GDDR5'
        
    return manufacturer, memory_type, memory_capacity, memory_clock