import os
def obtenerOfertas(l_filenames):
    l_ofertas = []
    for filename in l_filenames:
        l_provincias = obtenerProvincias(l_filenames)
        file = open(filename, "r+")
        # Agrego el nombre del csv para saber las ofertas que pertenecen a cada csv
        l_ofertas.append(filename.upper())
        for line in file:
            line = line.strip().split(",")
            try:
                provincia = line[2].split(";")[1].strip()
                l_ofertas.append(provincia)
            except IndexError as error:
                continue
    return l_ofertas

def obtenerProvincias(l_filenames):
    l_provincias = []
    for filename in l_filenames:
        file = open(filename, "r+")
        for line in file:
            line = line.strip().split(",")
            try:
                provincia = line[2].split(";")[1].strip()
                if provincia not in l_provincias:
                    l_provincias.append(provincia)
            except IndexError as error:
                continue
    return l_provincias

def ofertasPorProvincia(l_ofertas, l_provincias):
    file = open("pre-processing.csv", "w+")
    l_ofertas_provincia = []
    for provincia in l_provincias:
        nOfertas = l_ofertas.count(provincia)
        l_ofertas_provincia.append((provincia, nOfertas))
        # print(provincia, nOfertas)
        line = provincia + ", " + str(nOfertas) + "\n"
        file.write(line)
    return l_ofertas_provincia

def obtenerFilenames():
    l_filenames = []
    files = [f for f in os.listdir('./files') if os.path.isfile(f)]
    for f in files:
        # print(f[-4:len(f)])
        if(f[-4:len(f)] == ".csv"):
            l_filenames.append(f)
    return l_filenames

# Pruebas
# Obtengo el nombre de los archivos csvs del directorio files
l_filenames = obtenerFilenames()
print("Archivos csvs:\n", l_filenames)
print()

# Seteo los csvs que tengo hasta ahora
#l_filenames = ["computrabajo.csv", "multitrabajo.csv"]

# Obtengo las ofertas disponibles
l_ofertas = obtenerOfertas(l_filenames)
print('Provincias donde existen ofertas de trabajo (sin filtrado):\n',l_ofertas)
# Cuento el numero de ofertas que existen en la provincia del Guayas
print('Numero de ofertas que esiten en la provincia del Guayas:',l_ofertas.count("Guayas"))
print()

# Obtengo las provincias donde se encuentran las ofertas
l_provincias = obtenerProvincias(l_filenames)
print('Provincias donde existen ofertas de trabajo (con filtrado):\n', l_provincias)
# Verifico que exista una sola aparicion por provincia
print('¿Cuantas provincias del Guayas hay en el Ecuador? ',l_provincias.count("Guayas"))
print()

l_ofertas_provincia = ofertasPorProvincia(l_ofertas, l_provincias)
print('Numero de ofertas de trabajo por provincia:\n',l_ofertas_provincia)
