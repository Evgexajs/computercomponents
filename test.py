import re
words = [
    [
      'Видеокарта Gigabyte GeForce RTX 4090 GAMING OC 24GB (GV-N4090GAMING OC-24GD)',
      'ядро 2235 МГц, Boost 2535 МГц, память 24 ГБ GDDR6X 21 ГГц, 384 бит, HDMI, 3xDisplayPort, TDP 450 Вт, 16 pin, длина 340 мм, PCIe 4.0'  
    ],
    [
      'Видеокарта Palit GeForce RTX 4060 Ti Dual 8Gb (NE6406T019P1-1060D)',
      'ядро 2310 МГц, Boost 2535 МГц, память 8 ГБ GDDR6 18 ГГц, 128 бит, HDMI, 3xDisplayPort, TDP 160 Вт, 8 pin, длина 250 мм, RGB подсветка, DLSS 3, PCIe 4.0'  
    ],
    [
      'Видеокарта Gigabyte GeForce RTX 4060 Ti GAMING OC 8Gb (GV-N406TGAMING OC-8GD)',
      'ядро 2310 МГц, Boost 2580 МГц, память 8 ГБ GDDR6 18 ГГц, 128 бит, 2xHDMI, 2xDisplayPort, TDP 160 Вт, 8 pin, длина 281 мм, RGB подсветка, DLSS 3, PCIe 4.0'  
    ],
    [
      'Видеокарта Gigabyte GeForce RTX 3060 EAGLE OC 12GB (GV-N3060EAGLE OC-12GD 2.0 LHR)',
      'ядро 1320 МГц, Boost 1807 МГц, память 12ГБ GDDR6 15 ГГц, 192 бит, 2xHDMI, 2xDisplayPort, TDP 170 Вт, 8 pin, длина 242 мм, PCIe 4.0, REV2.0/LHR'  
    ],
    [
      '',
      ''  
    ],
    [
      '',
      ''  
    ],
    [
      '',
      ''  
    ],
    [
      '',
      ''  
    ],
    [
      '',
      ''  
    ],
    [
      '',
      ''  
    ],
    [
      '',
      ''  
    ],
    [
      '',
      ''  
    ],
    [
      '',
      ''  
    ],
    [
      '',
      ''  
    ],
    [
      '',
      ''  
    ],
    [
      '',
      ''  
    ],
    [
      '',
      ''  
    ],
    [
      '',
      ''  
    ],
    [
      '',
      ''  
    ],
    [
      '',
      ''  
    ],
]

for title in words: