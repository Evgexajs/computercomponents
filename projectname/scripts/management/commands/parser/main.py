from .selenium_config import get_html
from .beautifulsoup import get_content
import csv

def write_csv(video_cards_info, name_file):
    csv_file = f'{name_file}.csv'

    with open(csv_file, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter=';')
        if name_file == 'videocards':
            writer.writerow(['Title', 'Link', 'Details', 'manufacturer', 'memory_type', 'memory_capacity', 'memory_clock', 'price_dns', 'price_citylink', 'price_regard'])
            for video_card_info in video_cards_info:
                title = video_card_info['title'].strip()
                link = video_card_info['link'].strip()
                details = video_card_info['details'].strip()
                manufacturer = video_card_info['manufacturer'].strip()
                memory_type = video_card_info['memory_type'].strip()
                memory_capacity = video_card_info['memory_capacity'].strip()
                memory_clock = video_card_info['memory_clock'].strip()
                price_dns = video_card_info['price_dns'].strip()
                price_citylink = video_card_info['price_citylink'].strip()
                price_regard = video_card_info['price_regard'].strip()
                writer.writerow([title, link, details, manufacturer, memory_type, memory_capacity, memory_clock, price_dns, price_citylink, price_regard])
        elif name_file == 'cpu':
            writer.writerow(['Title', 'Link', 'Details', 'manufacturer', 'socket', 'cores', 'price_dns', 'price_citylink', 'price_regard'])
            for video_card_info in video_cards_info:
                title = video_card_info['title'].strip()
                link = video_card_info['link'].strip()
                details = video_card_info['details'].strip()
                manufacturer = video_card_info['manufacturer'].strip()
                socket = video_card_info['socket'].strip()
                cores = video_card_info['cores'].strip()
                price_dns = video_card_info['price_dns'].strip()
                price_citylink = video_card_info['price_citylink'].strip()
                price_regard = video_card_info['price_regard'].strip()
                writer.writerow([title, link, details, manufacturer, socket, cores, price_dns, price_citylink, price_regard])
        elif name_file == 'motherboards':
            writer.writerow(['Title', 'Link', 'Details', 'manufacturer', 'socket', 'size', 'price_dns', 'price_citylink', 'price_regard'])
            for video_card_info in video_cards_info:
                title = video_card_info['title'].strip()
                link = video_card_info['link'].strip()
                details = video_card_info['details'].strip()
                manufacturer = video_card_info['manufacturer'].strip()
                socket = video_card_info['socket'].strip()
                size = video_card_info['size'].strip()
                price_dns = video_card_info['price_dns'].strip()
                price_citylink = video_card_info['price_citylink'].strip()
                price_regard = video_card_info['price_regard'].strip()
                writer.writerow([title, link, details, manufacturer, socket, size, price_dns, price_citylink, price_regard])
        elif name_file == 'psu':
            writer.writerow(['Title', 'Link', 'Details', 'manufacturer', 'wattage', 'price_dns', 'price_citylink', 'price_regard'])
            for video_card_info in video_cards_info:
                title = video_card_info['title'].strip()
                link = video_card_info['link'].strip()
                details = video_card_info['details'].strip()
                manufacturer = video_card_info['manufacturer'].strip()
                wattage = video_card_info['wattage'].strip()
                price_dns = video_card_info['price_dns'].strip()
                price_citylink = video_card_info['price_citylink'].strip()
                price_regard = video_card_info['price_regard'].strip()
                writer.writerow([title, link, details, manufacturer, wattage, price_dns, price_citylink, price_regard])
        elif name_file == 'hdd' or name_file == 'ssd':
            writer.writerow(['Title', 'Link', 'Details', 'manufacturer', 'capacity', 'price_dns', 'price_citylink', 'price_regard'])
            for video_card_info in video_cards_info:
                title = video_card_info['title'].strip()
                link = video_card_info['link'].strip()
                details = video_card_info['details'].strip()
                manufacturer = video_card_info['manufacturer'].strip()
                capacity = video_card_info['capacity'].strip()
                price_dns = video_card_info['price_dns'].strip()
                price_citylink = video_card_info['price_citylink'].strip()
                price_regard = video_card_info['price_regard'].strip()
                writer.writerow([title, link, details, manufacturer, capacity, price_dns, price_citylink, price_regard])
        elif name_file == 'case':
            writer.writerow(['Title', 'Link', 'Details', 'manufacturer', 'form_factor', 'price_dns', 'price_citylink', 'price_regard'])
            for video_card_info in video_cards_info:
                title = video_card_info['title'].strip()
                link = video_card_info['link'].strip()
                details = video_card_info['details'].strip()
                manufacturer = video_card_info['manufacturer'].strip()
                form_factor = video_card_info['form_factor'].strip()
                price_dns = video_card_info['price_dns'].strip()
                price_citylink = video_card_info['price_citylink'].strip()
                price_regard = video_card_info['price_regard'].strip()
                writer.writerow([title, link, details, manufacturer, form_factor, price_dns, price_citylink, price_regard])
        elif name_file == 'ram':
            writer.writerow(['Title', 'Link', 'Details', 'manufacturer', 'capacity', 'price_dns', 'price_citylink', 'price_regard'])
            for video_card_info in video_cards_info:
                title = video_card_info['title'].strip()
                link = video_card_info['link'].strip()
                details = video_card_info['details'].strip()
                manufacturer = video_card_info['manufacturer'].strip()
                capacity = video_card_info['capacity'].strip()
                price_dns = video_card_info['price_dns'].strip()
                price_citylink = video_card_info['price_citylink'].strip()
                price_regard = video_card_info['price_regard'].strip()
                writer.writerow([title, link, details, manufacturer, capacity, price_dns, price_citylink, price_regard])
        else:
            writer.writerow(['Title', 'Link', 'Details', 'price_dns', 'price_citylink', 'price_regard'])
            for video_card_info in video_cards_info:
                title = video_card_info['title'].strip()
                link = video_card_info['link'].strip()
                details = video_card_info['details'].strip()
                price_dns = video_card_info['price_dns'].strip()
                price_citylink = video_card_info['price_citylink'].strip()
                price_regard = video_card_info['price_regard'].strip()
                writer.writerow([title, link, details, price_dns, price_citylink, price_regard])

    print("Данные успешно записаны в файл CSV.")

def init():
    paths = [
        {
            'url': 'https://hardprice.ru/category/videocard',
            'name': 'videocards',
            'data': []
        },
        {
            'url': 'https://hardprice.ru/category/cpu',
            'name': 'cpu',
            'data': []
        },
        {
            'url': 'https://hardprice.ru/category/mobo',
            'name': 'motherboards',
            'data': []
        },
        {
            'url': 'https://hardprice.ru/category/psu',
            'name': 'psu',
            'data': []
        },
        {
            'url': 'https://hardprice.ru/category/hdd',
            'name': 'hdd',
            'data': []
        },
        {
            'url': 'https://hardprice.ru/category/ssd',
            'name': 'ssd',
            'data': []
        },
        {
            'url': 'https://hardprice.ru/category/case',
            'name': 'case',
            'data': []
        },
        {
            'url': 'https://hardprice.ru/category/ram',
            'name': 'ram',
            'data': []
        },
    ]
    for path in paths:
        html = get_html(path['url'])
        content = get_content(html, path['name'])        
        path['data'] = content
        # write_csv(path['data'], path['name'])
    return paths

# init()