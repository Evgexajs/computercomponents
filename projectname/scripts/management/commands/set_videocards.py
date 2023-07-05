from django.core.management.base import BaseCommand
from apppc.models import Component, Price, VideoCard, Processor, Motherboard, SSD, HardDrive, ComputerCase, RAM, PowerSupply
from .parser.main import init

# Удаляем все объекты из каждой модели
class Command(BaseCommand):

    def handle(self, *args, **options):
        videocards = VideoCard.objects.all()

        # Создание экземпляров моделей и сохранение данных
        for videocard in videocards:
            title = videocard.title
            details = videocard.details
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

                if any(char.isdigit() for char in memory_capacity) != True and memory_capacity != 'неизвестно':
                    memory_capacity = parts[i - 1] + parts[i]

                if any(char.isdigit() for char in memory_clock) != True and memory_clock != 'неизвестно':
                    memory_clock = parts[i - 1] + parts[i]

            
            # частота ядра
            core_clock = 'неизвестно'
            if 'ядро' in details:
                temp = details.split('ядро')[1].split(',')[0].strip().split(' ')
                core_clock = temp[-2] + temp[-1]
            if 'ядра' in details:
                temp = details.split('ядра')[1].split(',')[0].strip().split(' ')
                core_clock = temp[-2] + temp[-1]
            elif 'частота процессора' in details:
                temp = details.split('частота процессора')[1].split(';')[0].strip().split(' ')
                core_clock = temp[-2] + temp[-1]
            elif 'Ядро' in details:
                core_clock = details.split('Ядро')[1].split(' ')[1].strip()
            elif 'дро' in details:
                temp = details.split('дро')[1].split(',')[0].strip().split(' ')
                core_clock = temp[-2] + temp[-1]
            
            # частота буста
            # потребление
            # размер видеокарты

            if memory_type == 'неизвестно':
                memory_type = 'GDDR5'

            # if core_clock == 'неизвестно':
            #     print({
            #         'details': details,
            #         'manufacturer': manufacturer,
            #         'memory_type': memory_type,
            #         'memory_capacity': memory_capacity,
            #         'memory_clock': memory_clock,
            #         'core_clock': core_clock
            #     })
                