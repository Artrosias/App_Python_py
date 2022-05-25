#Dichiarazioni variabili
nome_barman = "HAL 9000"
drink_speciale = "Moscow Mule"
prezzo_drink = 6
alcolici = ["White Russian", "Gin Tonic", "Whiskey Sour"]
analcolici = ["Cedrata", "Limonata", "Sprite",]

#Inizio del programma
print("Benvenuti al Drink&Python")
print("Mi chiamo " +nome_barman+ "...e sono pronto a servirti!")

print("Il drink piu' richiesto nel nostro pub e': "+str(drink_speciale))
print("Provalo subito, al modico prezzo di: "+str(prezzo_drink))
print("\nI drink alcolici sono "+str(len(alcolici)))
print("\nI drink analcolici sono "+str(len(alcolici)))
print("\nInserisci il tuo anno di nascita")
anno_nascita = int(input())
anni_cliente = 2022 - anno_nascita
print("Hai "+str(anni_cliente)+" anni")
drink_disponibili =[]

if anni_cliente < 18:
    print("\nSei minorenne: puoi ordinare solo analcolici")
    drink_disponibili += analcolici
else:
    print("\nSei maggiorenne : puoi ordinare alcolici e analcolici")
    drink_disponibili = analcolici+alcolici
print("\nEcco i drink consigliati per te:")
 
#KEEP IT SIMPLE, STUPID!
for drink_disponibile in drink_disponibili:
    print(drink_disponibile)
drink_scelto = input()
if drink_scelto in drink_disponibili:
    print("Hai scelto "+drink_scelto+". Buon aperitivo!")    
else:
    print("Mi spiace, il drink "+drink_scelto+" non e' disponibile :( ")  

