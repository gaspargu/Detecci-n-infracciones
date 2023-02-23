import numpy as np

def reader(file_name):
    lista = []

    with open(file_name, encoding='utf-8') as f:
        for line in f:
            lista += [line.split(',')]
    
    return lista

logs_28 = reader('LOGS-28-07-2021.txt')
logs_29 = reader('LOGS-29-07-2021.txt')
logs_30 = reader('LOGS-30-08-2020.txt')

pcr_28 = reader('PCR-28-07-2021.txt')
pcr_29 = reader('PCR-29-07-2021.txt')
pcr_30 = reader('PCR-30-08-2020.txt')


def telefonos_sospechosos(logs):
    cerciorados = np.zeros(len(logs), dtype=int)
    telefonos = []
    for i in range(len(logs)):
        j = i+1
        while(j < len(logs)):
            repite = logs[i][2]==logs[j][2] and logs[i][0]!=logs[j][0]
            if (cerciorados[j]==0 and cerciorados[i]==0 and repite):
                cerciorados[j] = 1
                cerciorados[i] = 1
                telefonos += [[logs[i][2],logs[i][0], logs[j][0]]]
                j+=1
            elif (cerciorados[j]==0 and cerciorados[i]==1 and repite):
                telefonos[-1] += [logs[j][0]]
                j+=1
            else:
                j+=1
    return telefonos


telefonos_28 = telefonos_sospechosos(logs_28)
telefonos_29 = telefonos_sospechosos(logs_29)
telefonos_30 = telefonos_sospechosos(logs_30)

#agrega los datos de la persona asociada al telefono sospechoso
def agrega_info(telefonos,datos):
    resultado = []
    for i in range(len(telefonos)):
        for j in range(len(datos)):
            if (datos[j][2]==telefonos[i][0]):
                resultado += [[datos[j][0], datos[j][3].rstrip('\n')] + telefonos[i]]
    return resultado

resultados_28 = agrega_info(telefonos_28,pcr_28)
resultados_29 = agrega_info(telefonos_29,pcr_29)
resultados_30 = agrega_info(telefonos_30,pcr_30)

print(resultados_28[0:10])
print(resultados_29[0:10])
print(resultados_30[0:10])

def writer(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(len(data)):
            line = ''
            for j in range(len(data[i])):
                line += data[i][j]+','
            line = line[:-1]
            line += '\n'
            f.write(line)

writer('RESULTADOS-28-07-21.txt', resultados_28)
writer('RESULTADOS-29-07-21.txt', resultados_29)
writer('RESULTADOS-30-08-20.txt', resultados_30)








 

