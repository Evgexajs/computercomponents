import re

def extract_cases(title, details):
    manufacturer = 'неизвестно'
    if 'Корпус' in title:
        manufacturer = title.split('Корпус')[1].split(' ')[1].strip()
        
        

    form_factor = 'неизвестно' 
    form_factor = details.split(',')[0].split(' ')[0]

    return manufacturer, form_factor