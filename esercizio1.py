 # DICHIARAZIONI VARIABILi
prezzo_drink = 5.5
sconto = 1
cliente_preferito = "Alessio"
print("Come ti chiami?")
nome_cliente = input()
print("Quanti anni hai?")
anni_cliente = int(input())
if nome_cliente == cliente_preferito and anni_cliente>25:
     prezzo_drink=sconto
print("Il prezzo del drink e' "+str(prezzo_drink))
