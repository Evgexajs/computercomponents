from django.core.management.base import BaseCommand
from apppc.models import Component, Price, VideoCard, Processor, Motherboard, SSD, HardDrive, ComputerCase, RAM, PowerSupply
from .parser.main import init

# Удаляем все объекты из каждой модели
class Command(BaseCommand):

    def handle(self, *args, **options):
        Component.objects.all().delete()
        Price.objects.all().delete()
        VideoCard.objects.all().delete()
        Processor.objects.all().delete()
        Motherboard.objects.all().delete()
        SSD.objects.all().delete()
        HardDrive.objects.all().delete()
        ComputerCase.objects.all().delete()
        RAM.objects.all().delete()
        PowerSupply.objects.all().delete()
        # Вызов функции парсера и получение данных
        datas = init()

        # Создание экземпляров моделей и сохранение данных
        for data in datas:
            items = data['data']
            for item in items:
                dns_price=item['price_dns']
                citilink_price=item['price_citylink']
                regard_price=item['price_regard']
                dns_price=dns_price.replace('\xa0', '').replace('p.', '').replace(' ', '')
                citilink_price=citilink_price.replace('\xa0', '').replace('p.', '').replace(' ', '')
                regard_price=regard_price.replace('\xa0', '').replace('p.', '').replace(' ', '')
                
                price = Price.objects.create(
                    dns_price=int(dns_price),
                    citilink_price=int(citilink_price),
                    regard_price=int(regard_price)
                )

                if data['name'] == 'videocards':
                    VideoCard.objects.create(
                        title=item['title'],
                        manufacturer=item['manufacturer'],
                        link=item['link'],
                        details=item['details'],
                        prices=price,
                        memory_type=item['memory_type'],
                        memory_capacity=item['memory_capacity'],
                        memory_clock=item['memory_clock']
                    )
                elif data['name'] == 'cpu':
                    Processor.objects.create(
                        title=item['title'],
                        manufacturer=item['manufacturer'],
                        link=item['link'],
                        details=item['details'],
                        prices=price,
                        socket=item['socket'],
                        cores=item['cores']
                    )
                elif data['name'] == 'motherboards':
                    Motherboard.objects.create(
                        title=item['title'],
                        manufacturer=item['manufacturer'],
                        link=item['link'],
                        details=item['details'],
                        prices=price,
                        socket=item['socket'],
                        size=item['size']
                    )
                elif data['name'] == 'psu':
                    PowerSupply.objects.create(
                        title=item['title'],
                        manufacturer=item['manufacturer'],
                        link=item['link'],
                        details=item['details'],
                        prices=price,
                        wattage=item['wattage']
                    )
                elif data['name'] == 'hdd':
                    HardDrive.objects.create(
                        title=item['title'],
                        manufacturer=item['manufacturer'],
                        link=item['link'],
                        details=item['details'],
                        prices=price,
                        capacity=item['capacity']
                    )
                elif data['name'] == 'ssd':
                    SSD.objects.create(
                        title=item['title'],
                        manufacturer=item['manufacturer'],
                        link=item['link'],
                        details=item['details'],
                        prices=price,
                        capacity=item['capacity']
                    )
                elif data['name'] == 'case':
                    ComputerCase.objects.create(
                        title=item['title'],
                        manufacturer=item['manufacturer'],
                        link=item['link'],
                        details=item['details'],
                        prices=price,
                        form_factor=item['form_factor']
                    )
                elif data['name'] == 'ram':
                    RAM.objects.create(
                        title=item['title'],
                        manufacturer=item['manufacturer'],
                        link=item['link'],
                        details=item['details'],
                        prices=price,
                        capacity=item['capacity']
                    )
                # Другие связанные модели и поля