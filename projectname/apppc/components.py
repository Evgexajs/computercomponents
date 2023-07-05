from django.db.models.functions import Least
from .models import Motherboard, ComputerCase

class Component:
    def __init__(self, name, value, queryset, priority = 1):
        self.queryset = queryset
        self.name = name
        self.value = value
        self.priority = priority

    def set_object(self, obj):
        self.object = obj

    def find_closest_component(self, amount):
        closest_component = self.queryset.annotate(
            min_price=Least('prices__dns_price', 'prices__citilink_price', 'prices__regard_price')
        ).filter(
            min_price__lte=int(self.value * amount)
        ).order_by('-min_price').first()
        self.result = closest_component

class Components:
    """
    Класс для вычисления комплектующих по сумме покупки
    """
    def __init__(self, amount):
        """
        Конструктор класса с установкой суммы,
        и шага сдвига доли
        """
        self.amount = amount
        self.step = 0.005
        self.drone = None
        self.video_card = None
        self.cpu = None
        self.motherboard = None
        self.computer_case = None
        self.ram = None
        self.ssd = None
        self.psu = None

    def _find_max(self, limit = 1):
        """
        Метод поиска компонента с максимальной долей от суммы
        """
        print('gavno')
        min_priority = 7
        max_value = 0
        component_name = None

        components = [
            self.video_card,
            self.cpu,
            self.motherboard,
            self.computer_case,
            self.ram,
            self.ssd,
            self.psu
        ]

        for component in components:
            if component is not None and component.value > max_value and component.value < limit and component.priority < min_priority:
                max_value = component.value
                component_name = component.name
                min_priority = component.priority
        # print('max', max_value)
        if max_value == 0:
            # Обработка ошибки, если все значения равны 0
            return None

        return component_name

    def _set_socket(self, component):
        """
        Метод устанавливает фильтрый материнской платы
        """
        if component.name == 'motherboard' and self.cpu and self.cpu.result and self.cpu.result.socket:
            component.queryset = Motherboard.objects.filter(socket=self.cpu.result.socket)

    def _set_size(self, component):
        """
        Метод устанавливает фильтрый для корпуса
        """
        if component.name == 'computer_case' and self.motherboard and self.motherboard.result and self.motherboard.result.size:
            component.queryset = ComputerCase.objects.filter(form_factor=self.motherboard.result.size)

    def set_filter(self, component):
        """
        Метод устанавливает фильтры в зависимости от типа комплектующего
        """
        self._set_socket(component)
        self._set_size(component)

    def calculate_component(self, component):
        """
        Метод поиска компонента в базе
        """
        self.set_filter(component)
        component.find_closest_component(self.amount)

        if component.result is None:
            max_component_name = self._find_max()
            # обработка для выхода из рекурсии когда ничего не нашли
            if max_component_name is None:
                return False
            
            item = getattr(self, max_component_name)
            res = self.reset_component(item, component)
            # обработка для выхода из рекурсии когда ничего не нашли
            if res is False:
                return False
        
        item = getattr(self, component.name)
        item = component
        item.set_object(component.result)
        setattr(self, component.name, item)
        return True

    def reset_component(self, item, component):
        """
        Метод переопределения комплектующего по измененной доле
        """
        
        item.value = round(item.value - self.step, 3)
        item.result = None
        setattr(self, item.name, item)
        res = self.calculate_component(item)
        # обработка для выхода из рекурсии когда ничего не нашли
        if res is False:
            return False
            
        self.set_filter(component)

        component.value = round(component.value + self.step, 3)
        component.find_closest_component(self.amount)
        if component.result is None:
            self.reset_component(item, component)