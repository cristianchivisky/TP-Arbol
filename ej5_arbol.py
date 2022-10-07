from mi_arbol import (
    nodoArbol,
    insertar_nodo,
    inorden_villano,
    inorden_empieza_con,
    contar_heroes,
    eliminar_nodo,
    inorden,
    postorden_heroes,
    crear_bosque,
    contar_heroes_villanos
)

arbol = nodoArbol()

lista = [
    ['Iron Man', False, 1960],
    ['Capitana Marvel', False, 1890],
    ['Thor', False, 1962],
    ['Dotor Strange', False, 1961],
    ['Thanos', True, 1962],
    ['Red Skull', True, 1963],
    ['Capitan America', False, 2000],
]

for nombre, villano, anio in lista:
    datos = {'villano': villano,
             'anio_aparicion': anio}
    
    insertar_nodo(arbol, nombre, datos)


print('Villanos')
inorden_villano(arbol)
print()
print('Superheroes que empiezan con C ')
inorden_empieza_con(arbol, 'C')
print()
print('Cantidad de superheroes:  ')
print(contar_heroes(arbol))
print()
clave = input('Ingrese parte del nombre que desea modificar ')
inorden_empieza_con(arbol, clave)
clave = input('Ahora que conoce la clave ingresela ')
pos = eliminar_nodo(arbol, clave)
if pos:
    name = input('Ingrese nuevo nombre ')
    insertar_nodo(arbol, name, pos[1])
else:
     print('valor no encontrado en el arbol')
print()
print('Superhéroes ordenados de manera descendente')
postorden_heroes(arbol)
print()
heroes = nodoArbol()
villanos = nodoArbol()
crear_bosque(arbol, heroes, villanos)
cantidad = {'villanos': 0, 'heroes': 0}
contar_heroes_villanos(arbol, cantidad)
print('Cantidad de heroes y villanos', cantidad)
print()
print('Heroes')
inorden(heroes)
print()
print('Villanos')
inorden(villanos)
