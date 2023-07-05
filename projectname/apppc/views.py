from django.shortcuts import render
from .models import VideoCard
from .models import Processor
from .models import Motherboard
from .models import ComputerCase
from .models import SSD
from .models import HardDrive
from .models import RAM
from .models import PowerSupply
from .components import Component, Components

def index(request):
    return render(request, 'AppPC/index.html')

def setup(request):
    if request.method == 'GET':
        amount = float(request.GET.get('amount'))
        drone = request.GET.get('drone')
        # флаг что нет ошибок
        noErrors = True
        if drone == 'AMD':
            components = Components(amount)
            video_card = Component('video_card', 0.4, VideoCard.objects, 7)
            cpu = Component('cpu', 0.22, Processor.objects.filter(title__icontains=drone), 6)
            motherboard = Component('motherboard', 0.13, Motherboard.objects, 5)
            ram = Component('ram', 0.1, RAM.objects, 4)
            ssd = Component('ssd', 0.05, SSD.objects, 3)
            psu = Component('psu', 0.05, PowerSupply.objects, 2)
            computer_case = Component('computer_case', 0.05, ComputerCase.objects, 1)
        else:
            components = Components(amount)
            video_card = Component('video_card', 0.35, VideoCard.objects, 7)
            cpu = Component('cpu', 0.24, Processor.objects.filter(title__icontains=drone), 6)
            motherboard = Component('motherboard', 0.11, Motherboard.objects, 5)
            ram = Component('ram', 0.1, RAM.objects, 4)
            ssd = Component('ssd', 0.1, SSD.objects, 3)
            psu = Component('psu', 0.05, PowerSupply.objects, 2)
            computer_case = Component('computer_case', 0.05, ComputerCase.objects, 1)

        components.video_card = video_card
        components.cpu = cpu
        components.motherboard = motherboard
        components.computer_case = computer_case
        components.ram = ram
        components.ssd = ssd
        components.psu = psu
        
        components.calculate_component(video_card)
        components.calculate_component(cpu)
        components.calculate_component(motherboard)
        components.calculate_component(computer_case)
        components.calculate_component(ram)
        components.calculate_component(ssd)
        components.calculate_component(psu)

        # вывести значения новые
        if (
            components.video_card.result is None or
            components.cpu.result is None or
            components.motherboard.result is None or
            components.ram.result is None or
            components.ssd.result is None or
            components.psu.result is None or
            components.computer_case.result is None
        ):
            noErrors = False

        print(components.video_card.value)
        print(components.cpu.value)
        print(components.motherboard.value)
        print(components.ram.value)
        print(components.ssd.value)
        print(components.psu.value)
        print(components.computer_case.value)

        if noErrors is False: # значит у нас не нашлось комплектующих под эту цену
            return render(request, 'AppPC/setup.html', {
                'message': 'aaaaaa'
            })
        else:
            return render(request, 'AppPC/setup.html', {
                'total_sum': int(components.video_card.object.min_price) + int(components.cpu.object.min_price) + int(components.motherboard.object.min_price) + int(components.computer_case.object.min_price) + int(components.ram.object.min_price) + int(components.ssd.object.min_price) + int(components.psu.object.min_price),
                'video_card': components.video_card.object,
                'cpu': components.cpu.object,
                'motherboard': components.motherboard.object,
                'computer_case': components.computer_case.object,
                'ram': components.ram.object,
                'ssd': components.ssd.object,
                'psu': components.psu.object,
            })

