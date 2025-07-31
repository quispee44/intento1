import time
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "GG": "Dimitunivo de God Game, usado tambien cuando algo acaba y/o ya no tiene solucion",
            "CHAMBA": "Trabajo, ocupacion o tarea",
            "SPAWNEAR": "Probeniente de la palabra [spanw], re refiere a la aparecion repentina de algo o alguien"
            }

while True:
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    time.sleep(1)    
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("ESO NO FORMA PARTE DE NUESTRO DICCIONARIO")
    time.sleep(2)
