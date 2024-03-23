# Diccionario

informacion_personal = {
    'nombre':'Neila',
    'edad':21,
    'ciudad':'Nueva loja',
    'provincia':'sucumbios',
}
print('----------------------')
print('Diccionario Original')
print('----------------------')
for clave, valor in informacion_personal.items():
    print(f'{clave} : {valor}')

# Clave "ciudad" y modifícalo con una ciudad diferente.
informacion_personal['ciudad'] = 'lago agrio'
informacion_personal['provincia'] = 'sucumbios'

# Nueva clave-valor al diccionario "profesion"
informacion_personal['profesion'] = 'estudiante'

# Verifica si la clave "telefono" existe
if 'telefono' not in informacion_personal:
    informacion_personal['telefono'] = '0985733365'

# Elimina la clave "edad" del diccionario
# del informacion_personal['edad']
informacion_personal.pop('edad')

print('----------------------')
print('Diccionario Modificado')
print('----------------------')
for clave, valor in informacion_personal.items():
    print(f'{clave} : {valor}')