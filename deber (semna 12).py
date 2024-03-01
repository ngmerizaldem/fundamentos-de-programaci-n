# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 68},
            {"day": "Martes", "temp": 70},
            {"day": "Miércoles", "temp": 72},
            {"day": "Jueves", "temp": 69},
            {"day": "Viernes", "temp": 75},
            {"day": "Sábado", "temp": 78},
            {"day": "Domingo", "temp": 82}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 66},
            {"day": "Martes", "temp": 69},
            {"day": "Miércoles", "temp": 73},
            {"day": "Jueves", "temp": 71},
            {"day": "Viernes", "temp": 77},
            {"day": "Sábado", "temp": 79},
            {"day": "Domingo", "temp": 83}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 67},
            {"day": "Martes", "temp": 71},
            {"day": "Miércoles", "temp": 75},
            {"day": "Jueves", "temp": 72},
            {"day": "Viernes", "temp": 78},
            {"day": "Sábado", "temp": 81},
            {"day": "Domingo", "temp": 85}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 65},
            {"day": "Martes", "temp": 68},
            {"day": "Miércoles", "temp": 70},
            {"day": "Jueves", "temp": 69},
            {"day": "Viernes", "temp": 74},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 81}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 52},
            {"day": "Martes", "temp": 54},
            {"day": "Miércoles", "temp": 58},
            {"day": "Jueves", "temp": 60},
            {"day": "Viernes", "temp": 63},
            {"day": "Sábado", "temp": 65},
            {"day": "Domingo", "temp": 69}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 53},
            {"day": "Martes", "temp": 56},
            {"day": "Miércoles", "temp": 60},
            {"day": "Jueves", "temp": 62},
            {"day": "Viernes", "temp": 55},
            {"day": "Sábado", "temp": 57},
            {"day": "Domingo", "temp": 71}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 51},
            {"day": "Martes", "temp": 55},
            {"day": "Miércoles", "temp": 58},
            {"day": "Jueves", "temp": 60},
            {"day": "Viernes", "temp": 62},
            {"day": "Sábado", "temp": 66},
            {"day": "Domingo", "temp": 70}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 54},
            {"day": "Martes", "temp": 57},
            {"day": "Miércoles", "temp": 59},
            {"day": "Jueves", "temp": 61},
            {"day": "Viernes", "temp": 64},
            {"day": "Sábado", "temp": 67},
            {"day": "Domingo", "temp": 70}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 80},
            {"day": "Martes", "temp": 82},
            {"day": "Miércoles", "temp": 84},
            {"day": "Jueves", "temp": 81},
            {"day": "Viernes", "temp": 78},
            {"day": "Sábado", "temp": 75},
            {"day": "Domingo", "temp": 72}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 79},
            {"day": "Martes", "temp": 81},
            {"day": "Miércoles", "temp": 83},
            {"day": "Jueves", "temp": 80},
            {"day": "Viernes", "temp": 77},
            {"day": "Sábado", "temp": 74},
            {"day": "Domingo", "temp": 71}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 81},
            {"day": "Martes", "temp": 83},
            {"day": "Miércoles", "temp": 85},
            {"day": "Jueves", "temp": 82},
            {"day": "Viernes", "temp": 79},
            {"day": "Sábado", "temp": 76},
            {"day": "Domingo", "temp": 73}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 78},
            {"day": "Martes", "temp": 80},
            {"day": "Miércoles", "temp": 92},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 86},
            {"day": "Sábado", "temp": 73},
            {"day": "Domingo", "temp": 70}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad in temperaturas:
    for semana in ciudad:
        suma = 0
        for dia in semana:
            suma += dia['temp']
        print(suma)