# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
print("-------------ejecutando------------------------")
f=open("Pararrayos.bc3")
contenido= f.read()
#print contenido

salida=""
"""
procesar linea por linea
"""
lineas=contenido.split("\n")

for linea in lineas:
    if "~D" in linea:
        if linea.find("#")<0:
                          #cumpoo que es linea de descompuesto y no es capitulo
                          #añadir materiales varios
                          linea = linea[0:len(linea)-1]+ "MATVARIOS\\1\\30\\|"
                          
    if "~T|" in linea:
        if linea.find("#")<0:
                      linea = linea[0:len(linea)-1] + ". Incluido mano de obra de albañileria, materiales y medios auxiliares. Totalmente instalado y probado|"
                      print(linea)
                      
    salida = salida + linea + "\n"
v=open("salida2.bc3","w")
v.write(salida)
v.close()

