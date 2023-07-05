from bs4 import BeautifulSoup
from .extracts.videocards import extract_videocards
from .extracts.cpus import extract_cpus
from .extracts.motherboards import extract_motherboards
from .extracts.psus import extract_psus
from .extracts.hdds import extract_hdds
from .extracts.ssds import extract_ssds
from .extracts.cases import extract_cases
from .extracts.rams import extract_rams

def get_content(html, name):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='products-list-v2__item')
    content = []

    for item in items:
        price = item.find('div', class_='products-list-v2__item-prices')
        prices = {}

        # Получаем цены из магазинов "Регард", "Ситилинк" и "ДНС"
        for column in price.find_all('column'):
            store = column.find('span', class_='text-warning date').text
            if store in ['Регард', 'Ситилинк', 'ДНС']:
                price = column.find('b', class_='price').text.strip()
                prices[store] = price
                
        if prices.get('Регард') != 'ожидается' and prices.get('Ситилинк') != 'ожидается' and prices.get('ДНС') != 'ожидается':
            details = item.find('div', class_='products-list-v2__item-title').find('p', class_='products-list-v2__item-description').get_text()
            title = item.find('div', class_='products-list-v2__item-title').find('a', class_='title').get_text()
            if name == 'videocards':
                manufacturer, memory_type, memory_capacity, memory_clock = extract_videocards(title, details)
                content.append(
                    {
                        'title': item.find('div', class_='products-list-v2__item-title').find('a', class_='title').get_text(),
                        'link': item.find('div', class_='products-list-v2__item-title').find('a').get('href'),
                        'details': details,
                        'manufacturer': manufacturer,
                        'memory_type': memory_type,
                        'memory_capacity': memory_capacity,
                        'memory_clock': memory_clock,
                        'price_dns': prices.get('ДНС'),
                        'price_citylink': prices.get('Ситилинк'),
                        'price_regard': prices.get('Регард'),
                    }
                )
            elif name == 'cpu':
                manufacturer, socket, cores = extract_cpus(title, details)
                content.append(
                    {
                        'title': item.find('div', class_='products-list-v2__item-title').find('a', class_='title').get_text(),
                        'link': item.find('div', class_='products-list-v2__item-title').find('a').get('href'),
                        'details': details,
                        'manufacturer': manufacturer,
                        'socket': socket,
                        'cores': cores,
                        'price_dns': prices.get('ДНС'),
                        'price_citylink': prices.get('Ситилинк'),
                        'price_regard': prices.get('Регард'),
                    }
                )
            elif name == 'motherboards':
                manufacturer, socket, size = extract_motherboards(title, details)
                content.append(
                    {
                        'title': item.find('div', class_='products-list-v2__item-title').find('a', class_='title').get_text(),
                        'link': item.find('div', class_='products-list-v2__item-title').find('a').get('href'),
                        'details': details,
                        'manufacturer': manufacturer,
                        'socket': socket,
                        'size': size,
                        'price_dns': prices.get('ДНС'),
                        'price_citylink': prices.get('Ситилинк'),
                        'price_regard': prices.get('Регард'),
                    }
                )
            elif name == 'psu':
                manufacturer, wattage = extract_psus(title, details)
                content.append(
                    {
                        'title': item.find('div', class_='products-list-v2__item-title').find('a', class_='title').get_text(),
                        'link': item.find('div', class_='products-list-v2__item-title').find('a').get('href'),
                        'details': details,
                        'manufacturer': manufacturer,
                        'wattage': wattage,
                        'price_dns': prices.get('ДНС'),
                        'price_citylink': prices.get('Ситилинк'),
                        'price_regard': prices.get('Регард'),
                    }
                )
            elif name == 'hdd':
                manufacturer, capacity = extract_hdds(title, details)
                content.append(
                    {
                        'title': item.find('div', class_='products-list-v2__item-title').find('a', class_='title').get_text(),
                        'link': item.find('div', class_='products-list-v2__item-title').find('a').get('href'),
                        'details': details,
                        'manufacturer': manufacturer,
                        'capacity': capacity,
                        'price_dns': prices.get('ДНС'),
                        'price_citylink': prices.get('Ситилинк'),
                        'price_regard': prices.get('Регард'),
                    }
                )
            elif name == 'ssd':
                manufacturer, capacity = extract_ssds(title, details)
                content.append(
                    {
                        'title': item.find('div', class_='products-list-v2__item-title').find('a', class_='title').get_text(),
                        'link': item.find('div', class_='products-list-v2__item-title').find('a').get('href'),
                        'details': details,
                        'manufacturer': manufacturer,
                        'capacity': capacity,
                        'price_dns': prices.get('ДНС'),
                        'price_citylink': prices.get('Ситилинк'),
                        'price_regard': prices.get('Регард'),
                    }
                )
            elif name == 'case':
                manufacturer, form_factor = extract_cases(title, details)
                content.append(
                    {
                        'title': item.find('div', class_='products-list-v2__item-title').find('a', class_='title').get_text(),
                        'link': item.find('div', class_='products-list-v2__item-title').find('a').get('href'),
                        'details': details,
                        'manufacturer': manufacturer,
                        'form_factor': form_factor,
                        'price_dns': prices.get('ДНС'),
                        'price_citylink': prices.get('Ситилинк'),
                        'price_regard': prices.get('Регард'),
                    }
                )
            elif name == 'ram':
                manufacturer, capacity = extract_rams(title, details)
                content.append(
                    {
                        'title': item.find('div', class_='products-list-v2__item-title').find('a', class_='title').get_text(),
                        'link': item.find('div', class_='products-list-v2__item-title').find('a').get('href'),
                        'details': details,
                        'manufacturer': manufacturer,
                        'capacity': capacity,
                        'price_dns': prices.get('ДНС'),
                        'price_citylink': prices.get('Ситилинк'),
                        'price_regard': prices.get('Регард'),
                    }
                )
            else:
                content.append(
                    {
                        'title': item.find('div', class_='products-list-v2__item-title').find('a', class_='title').get_text(),
                        'link': item.find('div', class_='products-list-v2__item-title').find('a').get('href'),
                        'details': details,
                        'price_dns': prices.get('ДНС'),
                        'price_citylink': prices.get('Ситилинк'),
                        'price_regard': prices.get('Регард'),
                    }
                )
    return content