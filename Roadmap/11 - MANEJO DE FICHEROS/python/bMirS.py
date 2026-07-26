datos = ["Nombre: Barbara\n", "Edad: 20\n", "Lenguaje: Java y BD\n"]
with open("alumno.txt", "w") as archivito:
    archivito.writelines(datos)
with open("alumno.txt", "r") as archivito:
    
    linealis = archivito.readlines()  
    for i in linealis:
        print(i.strip())
with open("alumno.txt", "r+") as archivito:
    texto_completo=archivito.read()
    posicionjava=texto_completo.find("Java")
    archivito.seek(posicionjava)
    archivito.write("Python y ML")
    print(archivito.tell())