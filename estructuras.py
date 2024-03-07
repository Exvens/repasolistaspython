# arreglos en paiton se llaman listas y a los objetos diccionarios

# se declaran diccionarios = objetos
clienteUno={
    "id":5,
    "nombre":"edificio1",
    "consumo":200
}

clienteDos={
    "id":10,
    "nombre":"edificio2",
    "consumo":500
}

# se declara una lista = arreglo

clienteAspciados=[
    clienteUno,
    clienteDos
]

# y ahora que hago con esa lista?
# mi objetivo sera obtener la infoormacion de la lista
# recorrer una lista o arreglo
# print(clienteAspciados)

'''for i in range(2):
    print(clienteAspciados[i]["consumo"])'''

# preogramemos un foreach que es un forespecializado en recorrer arreglos(listas)

for cliente in clienteAspciados:
    # print(cliente["consumo"])
    print(cliente["id"],'=>',cliente['consumo'],'KWH')
    print(f"{cliente["id"]}=>{cliente["consumo"]} KWH")