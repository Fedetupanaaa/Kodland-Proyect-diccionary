meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "ROFT": "Una respuesta a una broma",
    "SHEESH": "Ligera desaprobación",
    "CREEPY": "Aterrador, siniestro",
    "AGGRO": "Ponerse agresivo/enojado"
}

for a, memazo in meme_dict.items():
    print(a)        
    print(memazo)      
    print()  

bucle=int(input("Cuantas palabras no entienes?"))
for i in range(bucle) :
    
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!):")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Esa palabra no esta en el diccionario")
