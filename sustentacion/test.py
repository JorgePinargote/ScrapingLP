import os
coding = "utf-8"
# Seteo la lista de provincias del ecuador con sus indices, que me serviran para identificarlas en la visualizacion
provincias = [
      ["Guayas",0],
      ["Pichincha",1],
      ["Azuay",2],
      ["El Oro",3],
      ["ManabÃ\xad",4],
      ["Esmeraldas",5],
      ["Tungurahua",6],
      ["Imbabura",7],
      ["Chimborazo",8],
      ["Loja",9],
      ["Carchi",10],
      ["Los Rios",11],
      ["Santa Elena",12],
      ["Cotopaxi",13],
      ["Orellana",14],
      ["Bolivar",15],
      ["Cañar",16],
      ["Galapagos",17],
      ["Morona Santiago",18],
      ["Napo",19],
      ["Pastaza",20],
      ["Santo Domingo",21],
      ["Sucumbios",22],
      ["Zamora",23]
      ]

# Obtengo una lista de tuplas con todas las ofertas
def toListaTuplas(l_filenames):
    lt_ofertas = []
    for filename in l_filenames:
        file = open(filename, errors = 'ignore')
        cont = 0
        for line in file:                    
            line = line.strip().split(",")
            try:
                puesto = line[0].strip()
                nombre_empresa = line[1].strip()           
                horario = line[3].strip()
                salario = line[-1].strip()
                provincia = line[2].split(";")[1].strip()

                # Agrego las tuplas a la lista
                lt_ofertas.append((provincia, nombre_empresa, puesto, horario, salario))
                # line = provincia + ", " + nombre_empresa + ", " + puesto + ", " + horario + ", " + salario                
            except IndexError as error:
                continue
    return lt_ofertas

# Obtengo todos los horarios sin repetir
def obtenerHorarios(lt_ofertas):
    l_horarios = []
    for i in range(len(lt_ofertas)):
        horario = lt_ofertas[i][3]
        if horario not in l_horarios:
            l_horarios.append(horario)
    return l_horarios

# Obtengo todas las empresas sin repetir
def obtenerEmpresas(lt_ofertas):
    l_empresas = []
    for i in range(len(lt_ofertas)):
        empresa = lt_ofertas[i][1]
        if empresa not in l_empresas:
            l_empresas.append(empresa)
    return l_empresas

# Obtengo todas las provincias sin repetir
def obtenerProvincias(lt_ofertas):
    l_provincias = []
    for i in range(len(lt_ofertas)):
        provincia = lt_ofertas[i][0]        
        if provincia not in l_provincias:
            l_provincias.append(provincia)
    return l_provincias

# Obtengo el numero total de ofertas por provincia
def ofertasPorProvincia(lt_ofertas, l_provincias, provincias):
    file = open("ofertas_por_provincia.csv", "w+")
    lt_ofertas_provincia = []
    for provincia in l_provincias:
        nOfertas = 0

        # Para cada provincia ofertada, comparo con mi lista de provincias
        # para asignarle un indice
        for j in range(len(provincias)):            
            if(provincia.lower() == provincias[j][0].lower()):
                #print("-------------------",provincia.lower(), provincias[j][0].lower())
                indice = provincias[j][1]

        for i in range(len(lt_ofertas)):
            if(provincia.lower() == lt_ofertas[i][0].lower()):
                nOfertas += 1

        lt_ofertas_provincia.append((provincia, nOfertas))
        line = provincia + ", " + str(nOfertas) + ", " + str(indice) + "\n"
        file.write(line)
    return lt_ofertas_provincia

# Obtengo el numero total de ofertas por empresa
def ofertasPorEmpresa(lt_ofertas, l_empresas):
    file = open("ofertas_por_empresa.csv", "w+")
    lt_ofertas_empresa = []
    for empresa in l_empresas:
        nOfertas = 0
        for i in range(len(lt_ofertas)):
            if(empresa.lower() == lt_ofertas[i][1].lower()):
                nOfertas += 1
        lt_ofertas_empresa.append((empresa, nOfertas))
        line = empresa + ", " + str(nOfertas) + "\n"
        file.write(line)
    return lt_ofertas_empresa

# Obtengo el numero total de ofertas por horario
def ofertasPorHorario(lt_ofertas, l_horarios):
    file = open("ofertas_por_horario.csv", "w+")
    lt_ofertas_horario = []
    for horario in l_horarios:
        nOfertas = 0
        for i in range(len(lt_ofertas)):
            if(horario.lower() == lt_ofertas[i][3].lower()):
                nOfertas += 1
        lt_ofertas_horario.append((horario, nOfertas))
        line = horario + ", " + str(nOfertas) + "\n"
        file.write(line)    
    return lt_ofertas_horario

# Obtengo todos los archivos csvs del directorio actual
def obtenerFilenames():
    l_filenames = []
    files = [f for f in os.listdir('./') if os.path.isfile(f)]
    for f in files:
        # print(f[-4:len(f)])
        if(f[-4:len(f)] == ".csv"):
            l_filenames.append(f)
    return l_filenames

# Pruebas
# Obtengo el nombre de los archivos csvs del directorio files
l_filenames = obtenerFilenames()
print("Archivos csvs:\n", l_filenames,"\n")

# Seteo los csvs que tengo hasta ahora
#l_filenames = ["computrabajo.csv", "multitrabajo.csv"]

# Obtengo un diccionario de todas las ofertas existentes
listaTuplas = toListaTuplas(l_filenames)
print("Lista de tuplas de todas las ofertas existentes:\n", listaTuplas,"\n")

# Obtengo las provincias donde se encuentran las ofertas
l_provincias = obtenerProvincias(listaTuplas)
print('Provincias donde existen ofertas de trabajo (con filtrado):\n', l_provincias)
print('Numero de provincias:\t', len(l_provincias), "\n")

# Obtengo las empresas donde se encuentran las ofertas
l_empresas = obtenerEmpresas(listaTuplas)
print('Empresas donde existen ofertas de trabajo (con filtrado):\n', l_empresas)
print('Numero de empresas:\t', len(l_empresas), "\n")

# Obtengo los horarios de trabajo de las ofertas
l_horarios = obtenerHorarios(listaTuplas)
print('Horarios de trabajo de las ofertas de trabajo (con filtrado):\n', l_horarios)
print('Numero de horarios:\t', len(l_horarios), "\n")

# Obtengo el numero de ofertas de trabajo por provincia
lt_ofertas_provincia = ofertasPorProvincia(listaTuplas, l_provincias, provincias)
print('Numero de ofertas de trabajo por provincia:\n',lt_ofertas_provincia, "\n")

# Obtengo el numero de ofertas de trabajo por empresa
lt_ofertas_empresa = ofertasPorEmpresa(listaTuplas, l_empresas)
print('Numero de ofertas de trabajo por empresa:\n', lt_ofertas_empresa, "\n")

# Obtengo el numero de ofertas de trabajo por horario
lt_ofertas_horario = ofertasPorHorario(listaTuplas, l_horarios)
print('Numero de ofertas de trabajo por horario:\n', lt_ofertas_horario, "\n")