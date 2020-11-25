#Esercizio 24 e 25 (insieme)


from random import randint
print("le percentuali dei voti dei due candidati  x e y sono:")
x = randint(1, 100)
y = (100-x)
print(x, y)

print(" lista dei candidati in ordine alfabetico: x, y")
if x > y :
    print(" lista dei candidati in ordine decrescente: x, y")
else:
    print(" lista dei candidati in ordine decrescente: y, x")




#Esercizio 26

lista_stipendi = []
conteggio = True
dipendente = 0
ripetizioni = 0
somma = 0
while conteggio == True:
    dipendente += 1
    ripetizione_input += 1
    print("Stipendio dipendente", dipendente,"? ")
    stipendi_dipendente = int(input())
    lista_stipendi.append(stipendi_dipendente)

    if ripetizione_input == 5:
        tasto_premuto = int(input("se vuoi fermare qui il conteggio e osservare la media degli stipendi, premi -1, in caso contrario premi 0 "))
        ripetizione_input = 0
        if tasto_premuto == -1:
            conteggio = False
        else:
            pass
for x in lista_stipendi:
    somma += x
lista1 = len(lista_stipendi)
print(lista_stipendi)
mediastipendi = somma/lista1
print(mediastipendi)



#Es 27


lista_veicoli = []
conteggio = True
numerogg = 0
ripetizioni = 0
somma = 0
while conteggio == True:
    numerogg += 1
    ripetizioni += 1
    print("Quanti veicoli sono entrati il giorno", numerogg,"? ")
    veicoli = int(input())
    lista_veicoli.append(veicoli)

    if ripetizioni == 5:
        risp = int(input("se vuoi uscire e vedere quanti veicoli sono passati in questi giorni, premi 0, se vuoi continuare premi -1 : "))
        ripetizioni = 0
        if risp == 0:
            conteggio = False
        else:
            pass
for x in lista_veicoli:
    somma += x
print("In un totale di", numerogg,"giorni, sono transitati", somma, "veicoli")