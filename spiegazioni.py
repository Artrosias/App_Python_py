

# SETTARE LE VARIABILI
from pprint import pprint


drink_speciale = "Moscow Mule" #ricorda le stringe vanno sempre negli apici
print(drink_speciale) #la variabile va scritta senza apici
drink_speciale = "White Russian"
print(drink_speciale)

#INPUT
#stringa_inserita = input()
#print(stringa_inserita)


#LISTA
alcolici = ["White Russian", "Gin Tonic", "Whiskey Sour"]
analcolici = ["Cedrata", "Limonata", "Sprite",]
if "Gin Tonic" in alcolici:
    print("La bevanda e' disponibile")#congiunzione con dichiarazione if
menù_drink = analcolici+alcolici #con questo operatore possiamo concatenare più liste
alcolici.append ("Margarita") #aggiunge un elemento alla lista
alcolici.insert (0,"Martini") #aggiunge un elemento all'inizio della lista
alcolici.remove("Martini") #rimuove un elemento alla lista
alcolici.pop[1] #elimina un elemento specificando la sua posizione
alcolici.sort() #ordina gli elementi in ordine alfabetico
print(alcolici)                                            # KEEP IT SIMPLE, STUPID!
for alcolico in alcolici:
    print(alcolico)