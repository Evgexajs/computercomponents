from django.db import models

class Price(models.Model):
    dns_price = models.DecimalField(max_digits=20, decimal_places=2)
    citilink_price = models.DecimalField(max_digits=20, decimal_places=2)
    regard_price = models.DecimalField(max_digits=20, decimal_places=2)

class Component(models.Model):
    title = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    details = models.CharField(max_length=300)
    prices = models.ForeignKey(Price, on_delete=models.CASCADE)

class VideoCard(Component):
    memory_capacity = models.CharField(max_length=50)
    memory_type = models.CharField(max_length=50)
    memory_clock = models.CharField(max_length=50)
    core_clock = models.CharField(max_length=50, blank=True, null=True)# частота ядра
    boost_clock = models.CharField(max_length=50, blank=True, null=True)# частота буста
    power_consumption = models.CharField(max_length=50, blank=True, null=True)# потребление
    size = models.CharField(max_length=50, blank=True, null=True)# размер видеокарты

class Processor(Component):
    socket = models.CharField(max_length=50)
    cores = models.IntegerField()
    integrated_graphics = models.CharField(max_length=50, blank=True, null=True)# встроеная графика если есть
    core_clock = models.CharField(max_length=50, blank=True, null=True)# частота ядер
    boost_clock = models.CharField(max_length=50, blank=True, null=True)# частота буста ядер
    memory_type = models.CharField(max_length=50, blank=True, null=True)# тип оперативной памяти
    max_memory_speed = models.CharField(max_length=50, blank=True, null=True)# предельная частота оперативной памяти
    cache_3 = models.CharField(max_length=50, blank=True, null=True)# объем кеша 3-го уровня
    power_consumption = models.CharField(max_length=50, blank=True, null=True)# потребление

class Motherboard(Component):
    socket = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    memory_slots = models.IntegerField(blank=True, null=True)# количество слотов оперативной памяти
    memory_type = models.CharField(max_length=50, blank=True, null=True)# типо оперативной памяти
    max_memory_speed = models.CharField(max_length=50, blank=True, null=True)# предельная частота оперативной памяти
    chipset = models.CharField(max_length=50, blank=True, null=True)# чипсет

class SSD(Component):
    capacity = models.CharField(max_length=50)
    read_speed = models.CharField(max_length=50, blank=True, null=True)# скорость чтения
    write_speed = models.CharField(max_length=50, blank=True, null=True)# скорость записи
    
class HardDrive(Component):
    capacity = models.CharField(max_length=50)
    speed = models.CharField(max_length=50, blank=True, null=True)# скорость, хотя не так важно

class ComputerCase(Component):
    form_factor = models.CharField(max_length=50)
    max_gpu_size = models.CharField(max_length=50, blank=True, null=True)# размер видеокарты
    fans = models.BooleanField(default=False, blank=True, null=True)# вентиляторы если есть
    weight = models.CharField(max_length=50, blank=True, null=True)# вес

class RAM(Component):
    capacity = models.CharField(max_length=50)
    speed = models.CharField(max_length=50, blank=True, null=True)# скорость
    timings = models.CharField(max_length=50, blank=True, null=True)# тайминги
    modules = models.IntegerField(blank=True, null=True)# количество плашек

class PowerSupply(Component):
    wattage = models.CharField(max_length=10)
    certificate = models.CharField(max_length=50, blank=True, null=True)# сертификат если есть