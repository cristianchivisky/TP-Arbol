from heap import HeapMax

cp = HeapMax()
cp.agregar('PrimerDocEmpleado', 1)
cp.agregar('SegundoDocEmpleado', 1)
cp.agregar('TercerDocEmpleado', 1)
##print(cp.vector)
print()
aux = cp.quitar()
print(aux[0])
cp.agregar(aux[0], aux[1])
#print(cp.vector)
print()
cp.agregar('PrimerDocStaffTI', 2)
cp.agregar('SegundoDocStaffTI', 2)
cp.agregar('PrimerDocumentoGerente', 3)
#print(cp.vector)
print()
cp.quitar()
cp.quitar()
#print(cp.vector)
print()
cp.agregar('CuartoDocEmpleado', 1)
cp.agregar('QuintoDocEmpleado', 1)
cp.agregar('SegundoDocumentoGerente', 3)
#print(cp.vector)
print()
while cp.tamanio > 0:
    print(cp.quitar())
