def leer_archivo(nombre_archivo):
    lista_grande = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            lista = list(map(int, linea.strip().split()))
            lista_grande.append(lista)
    return lista_grande

nombre_archivo = "./P1.in"
resultado = leer_archivo(nombre_archivo)

def separar(resultado):
    casos = []
    ncaso = -1
    for x in resultado:
        if len(x) == 3:
            caso = []
            ncaso += 1
            caso.append(x)
            casos.append(caso)
        elif len(x) == 2:
            casos[ncaso].append(x)
    return casos
casos = separar(resultado)
#print(casos)

def misma_carga(w1, m1, m2):
    return (1 + abs(m1 - m2)) % w1

def diferente_carga(w2, m1, m2):
    return (w2 - abs(m1 - m2)) % w2

def formar_elementos_fundamentales(casos):
    elementos_fundamentales_por_caso = []  # Almacenará todos los elementos fundamentales de cada caso

    for caso in casos:
        elementos = caso[1:]  # Ignorar la primera línea que contiene los parámetros w1, w2
        elementos_fundamentales = []

        # Revisar cada par de átomos en el caso para formar elementos fundamentales
        for i in range(len(elementos)):
            for j in range(i + 1, len(elementos)):
                m1, c1 = elementos[i]
                m2, c2 = elementos[j]
                
                # Formar un elemento si las masas son diferentes
                if m1 != m2:
                    elementos_fundamentales.append((elementos[i], elementos[j]))

        # Agregar la lista de elementos fundamentales para este caso a la lista global
        elementos_fundamentales_por_caso.append(elementos_fundamentales)

    return elementos_fundamentales_por_caso
print(formar_elementos_fundamentales(casos))


