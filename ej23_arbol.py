from mi_arbol import(
    nodoArbol,
    insertar_nodo,
    inorden_criaturas,
    busqueda,
    derrotadas_por_heracles,
    no_derrotadas,
    inorden_empieza_con,
    eliminar_nodo,
    por_nivel,
    capturadas_por_heracles,
    cant_derrotas
)
tabla = [
    ['Ceto', None],
    ['Tifon', 'Zeus'],
    ['Equidna', 'Argos Panoptes'],
    ['Dino', None],
    ['Pefredo', None],
    ['Enio', None],
    ['Escila', None],
    ['Caribdis', None],
    ['Euriale', None],
    ['Esteno', None],
    ['Medusa', 'Perseo'],
    ['Ladon', 'Heracles'],
    ['Aguila del caucaso', None],
    ['Quimera', 'Belerofonte'],
    ['Hidra de Lerna', 'Heracles'],
    ['Leon de Nemea', 'Heracles'],
    ['Esfinge', 'Edipo'],
    ['Dragon de la Colquida', None],
    ['Cerbero', None],
    ['Cerda de Cromion', 'Teseo'],
    ['Ortro', 'Heracles'],
    ['Toro de Creta', 'Teseo'],
    ['Jabali de Calidon', 'Atalanta'],
    ['Carcinos', None],
    ['Gerion', 'Heracles'],
    ['Cloto', None],
    ['Laquesis', None],
    ['Atropos', None],
    ['Minotauro de Creta', 'Teseo'],
    ['Harpias', None],
    ['Argos Panoptes', 'Hermes'],
    ['Aves del Estinfalo', None],
    ['Talos', 'Medea'],
    ['Sirenas', None],
    ['Piton', 'Apolo'],
    ['Cierva de Cerinea', None],
    ['Basilisco', None],
    ['Jabali de Erimanto', None]
]
arbol_1=nodoArbol()

for criatura, derrotado_por in tabla:
    datos = {'derrotado_por': derrotado_por,
            'capturada': None,
            'descripcion': None}
    insertar_nodo(arbol_1, criatura, datos)

print('listado inorden de las criaturas y quienes la derrotaron')
inorden_criaturas(arbol_1)

print()
aux='0'
while aux=='0':
    clave=input('Ingrese el nombre de la criatura para cargar la descripcion:  ')
    pos=busqueda(arbol_1, clave)
    if pos:
        pos['datos']['descripcion']=input('Ingrese la decripcion:  ')
        #print(pos['info'], pos['datos'])
    else:
        print('No se encontro la criatura')
    aux=input('Si desea cargar otra descripcion presione cero:  ')
# Talos
buscado=input('Ingrese el nombre de la criatura que desea buscar: ') 
pos=busqueda(arbol_1, buscado)
if pos:
    print(pos['info'], pos['datos'])
else:
    print('No se encontro la criatura')

print()
print('Los tres que mas derrotaron')
lista=[]
aux_1=['', 0]
aux_2=['', 0]
aux_3=['', 0]
for h in cant_derrotas(arbol_1, lista):
    if h[1]>aux_1[1]:
        aux_3=aux_2        
        aux_2=aux_1
        aux_1=h
    elif h[1]>aux_2[1]:
        aux_3=aux_2
        aux_2=h
    elif h[1]>aux_3[1]:
        aux3=h
print(aux_1, aux_2, aux_3)

print('Criaturas derrotadas por Heracles: ')
derrotadas_por_heracles(arbol_1)
print()
print('Criaturas no derrotadas: ')
no_derrotadas(arbol_1)
print()
criaturas = ['Cerbero', 'Toro de Creta', 'Cierva de Cerinea', 'Jabali de Erimanto']
for criatura in criaturas:
    pos=busqueda(arbol_1, criatura)
    pos['datos']['capturada']='Heracles'
    print(pos['info'], pos['datos'])

print()
buscado=input('ingrese parte de lo que desea buscar: ')
inorden_empieza_con(arbol_1, buscado)
print()
eliminar_nodo(arbol_1, 'Basilisco')
eliminar_nodo(arbol_1, 'Sirenas')
print()
pos=busqueda(arbol_1, 'Aves del Estinfalo')
if pos:
    pos['datos']['derrotado_por']= 'Heracles derroto a varias'
    #print(pos['info'], pos['datos'])

print()
aux = eliminar_nodo(arbol_1, 'Ladon')
#print(aux)
insertar_nodo(arbol_1, 'Dragon Ladon', aux[1])
print()
print('Listado por nivel')
por_nivel(arbol_1)
print()
print('Capturadas por Heracles')
capturadas_por_heracles(arbol_1)
print()
