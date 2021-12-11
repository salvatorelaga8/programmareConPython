"""
stringa = "i topi non avevano nipoti"
risultato = ""

for number in range(-1, -(len(stringa) + 1), -1):
    risultato = risultato + stringa[number]
print(risultato)
print(stringa[::-1]) # è come se fosse: [inizio:fine:step] con [inizio,fine). Non specificando inizio e fine tu stai dicendo
# prendimi tutto, cioè dall'inizio alla fine. Questa si chiama slicing notation. :)
# stringa[1:] -> stampa dalla posizione 1 fino alla fine
# stringa[1:3] -> stampa dalla posizione 1 alla posizione 3 (esclusa)
# stringa[:4] -> stampa dall'inizio alla posizione 4.
"""

# Esercizio n.1
# Calcolare la somma dei primi 500 numeri naturali (da 0 a 500 escluso)

somma = 0

for number in range(0, 500):
    somma = somma + number

print(somma)

# Esercizio n.2
# Data la stringa 'abcdefghi', scrivere un programma che analizzi la stringa e stampi a video:
# Lettera 1: a Lettera 2: b ... E così via. Modificare poi il programma in modo da leggere la stringa da tastiera.

# parola = input('Inserire una parola ')
parola = 'sal'

for index in range(0, len(parola)):
    print('Lettera ', index, " :", parola[index])

# Esercizio n.3
# Scrivere una funzione area_cerchio che, dato un raggio, calcola la sua area.
# Scrivere anche una funzione circonferenza, che calcola in maniera analoga il suo perimetro.

raggio = 5
PI_GRECO = 3.14


def perimetro_circonferenza(raggio):
    return 2 * PI_GRECO * raggio


def area_cerchio(raggio):
    return PI_GRECO * raggio * raggio


print("Perimetro cerchio: ", perimetro_circonferenza(raggio))
print("Area cerchio: ", area_cerchio(raggio))

# Esercizio n.4
# Modificare il codice del gioco della palla magica presente nella cartella dei file per gli esercizi, usando le condizioni elif per quelle in eccesso: usare risposte del tipo
#
# Meglio non dirlo ora.
# Ne sei sicuro?
# Direi proprio di sì.
# La mia risposta è no.
# Chiedimelo più tardi.
# Dovresti rifletterci di più.
# Ci puoi contare.
# Le mie fonti dicono di sì.
# Far sì che il gioco non finisca finché l'utente non digita una stringa uguale a "exit".

# Gioco PALLA MAGICA
import random

# domanda = input('Fai una domanda alla palla magica: ')
domanda = 'exit'

while (domanda != 'exit'):
    # estrae un numero intero casuale tra 1 e 8
    risposta = random.randint(1, 8)
    if risposta == 1:
        print('Meglio non dirlo ora.')
    elif risposta == 2:
        print('Ne sei sicuro?')
    elif risposta == 3:
        print('Direi proprio di sì.')
    elif risposta == 4:
        print('La mia risposta è no.')
    elif risposta == 5:
        print('Chiedimelo più tardi.')
    elif risposta == 6:
        print('Dovresti rifletterci di più.')
    elif risposta == 7:
        print('Ci puoi contare.')
    else:
        print('Le mie fonti dicono di sì.')
    domanda = input('Fai una domanda alla palla magica: ')

# Esercizio n.5
# Scrivi un programma Python che stampi tutti i numeri da 0 a 6 tranne 3 e 6.

for number in range(0, 6):
    if number != 3:
        print(number)

# Esercizio n.6
# Scrivi un programma Python per stampare il modello alfabetico 'P'.

result_str = ""
for row in range(0, 7):
    for column in range(0, 7):
        if (column == 1 or ((row == 0 or row == 3) and column > 0 and column < 5) or (
                (column == 5 or column == 1) and (row == 1 or row == 2))):
            result_str = result_str + "*"
        else:
            result_str = result_str + " "
    result_str = result_str + "\n"
print(result_str)

# Esercizio n.7
# Scrivi un programma che stampi il countdown, che dato come parametro di ingresso un numero,
# restituisce il countdown a partire da quel numero, fino a zero. Usare il ciclo for.

countdown = 12


def countdown_with_for(countdown):
    for number in range(countdown, -1, -1):
        print(number)


countdown_with_for(countdown)
print('\n')
print('\n')


# Esercizio n.8
# Ripetere l'esercizio precedente e usare il ciclo while.

def countdown_with_while(countdown):
    while countdown >= 0:
        print(countdown)
        countdown = countdown - 1


countdown_with_while(countdown)

# Esercizio n.9
# Scrivi una funzione che prende due numeri come parametro e manda in print il più grande tra i due.
# Per quanto Python disponga di una funzione max(),
# sei invitato a utilizzare le istruzioni If, Elif ed Else per la scrittura dell'algoritmo.

number_1 = 5
number_2 = 6


def max_number(number_1, number_2):
    if (number_1 > number_2):
        print(number_1)
    elif (number_2 > number_1):
        print(number_2)
    else:
        print('i due numeri coincidono')


max_number(number_1, number_2)

# Esercizio n.10
# Scrivi una funzione che prende stavolta tre numeri come parametro e restituisce il più grande tra loro!

number_1 = 10
number_2 = 10
number_3 = 7


def max_between_three_number(number_1, number_2, number_3):
    if number_1 >= number_2 and number_1 >= number_3:
        print(number_1)
    elif number_2 >= number_1 and number_2 >= number_3:
        print(number_2)
    elif number_3 >= number_1 and number_3 >= number_2:
        print(number_3)
    else:
        print('i due numeri coincidono')


max_between_three_number(number_1, number_2, number_3)

# Esercizio n.11
# Scrivi una funzione "sommatrice" che somma tra loro tutti gli elementi di una lista di numeri.

lista = [1, 3, 5, 4]


def sommatrice(lista):
    somma = 0
    for elem in lista:
        somma = somma + elem
    print("Risultato ", somma)


sommatrice(lista)

# Esercizio n.12
# Scrivi una funzione che, dato in ingresso un valore espresso in metri,
# mandi in print l'equivalente in miglia terrestri, iarde, piedi e pollici.
metri = 20


def americana(metri):
    conversions = dict()
    conversions["miglia"] = metri / 1609.344
    conversions["piedi"] = metri * 3.280840
    conversions["pollici"] = metri * 39.37008
    conversions["iarde"] = metri * 1.093613

    print(f"{metri} metri corrispondono a:")
    for key, value in conversions.items():
        print(f"{key}: {value}")


# Esercizio n.13
# Correggi il seguente codice

paragrafo = "Viviamo in un mondo che ci disorienta con la sua complessità. Vogliamo comprendere ciò che vediamo attorno a noi e chiederci: Qual è la natura dell'universo? Qual è il nostro posto in esso? Da che cosa ha avuto origine l'universo e da dove veniamo noi? "


def stampaParagrafo(testo):
    print(testo)  # print testo -> print è una funzione e quindi bisogna scrivere print(testo)


stampaParagrafo(paragrafo)  # stampaPararrafo() -> nome della funziona sbagliato.


# la funzione inoltre accetta un valore come parametro, cioè paragrafo.


# Esercizio n.14
# Scrivere una funzione “equalTo” che, dato un array di numeri qualsiasi e un numero scelto,
# conti quante volte il numero scelto compare nell'array.
# Esempio: [1,2,4,8,12,4,3] NumeroScelto = 4
# Suggerimento: usare una variabile contatore, dove “contare” quante volte viene trovato il numero scelto...

def equalTo(number_list, number):
    counter = 0
    for elem in number_list:
        if elem == number:
            counter += 1
    return counter


number_list = [1, 2, 4, 8, 12, 4, 3]
number = 4
print(number, " compare nella lista ", number_list, " ", equalTo(number_list, number), " volte")


# Esercizio n.15
# Scrivere un programma che conti le occorrenze della “a” nelle seguenti parole:
# Banana;
# Aiuola;
# Abracadrabra;
# Elfo.

def counter_letter_in_words(letter, *args):
    counter = 0
    for word in args:
        for elem in word:
            # non distinguiamo tra maiuscole e minuscole
            if elem.lower() == letter:
                counter += 1
    print(letter, "è presente nelle parole ", args, " ", counter, " volte")


letter = 'a'
counter_letter_in_words(letter, "Banana", "Aiuola", "Abracadabra", "Elfo")


# Esercizio n.16
# Scrivere un programma che conti i numeri pari presenti in un array.

def counter_num_pari(number_list):
    counter = 0
    for elem in number_list:
        if elem % 2 == 0:
            counter += 1
    print(number_list, " contiene ", counter, " elementi pari")


number_list = [1, 2, 4, 8, 12, 4, 3]
counter_num_pari(number_list)


# Esercizio n.17
# Scrivere una funzione “reverse” che, data una stringa, la stampi carattere per carattere al contrario.

def reverse(word):
    result = ""
    for elem in range(len(word) - 1, -1, -1):
        result += word[elem]
    print("Word: ", word)
    print("Reverse Word With For: ", result)
    print("Reverse Word With Slicing Notation : ", word[::-1])


word = "cavallo"
reverse(word)


# Esercizio n.18
# Scrivere una funzione divisibiliPerCinque che, dato il seguente array:
# [10, 23, 45, 92, 70, 1020, 71] stampi solo gli elementi divisibili per cinque.

def divisibili_per_cinque(*args):
    result = []
    for elem in args:
        if elem % 5 == 0:
            result.append(elem)
    return result


print(divisibili_per_cinque(10, 23, 45, 92, 70, 1020, 71))


# Esercizio n.19
# Per calcolare il volume di alcune figure solide, è utile prima calcolare l'area di base
# e poi utilizzarla nel calcolo seguente: prendiamo in esempio una piramide a base quadrata.
# Scrivere una funzione che calcola prima l'area di base e poi un'altra che usa il calcolo
# per calcolare il volume. Area base = lato x lato Volume piramide = (Abase x altezza) / 3


def area_di_base(lato):
    return lato * lato


def volume_piramide(lato, altezza):
    return (area_di_base(lato) * altezza) / 3


lato = 5
altezza = 12

print("Volume piramide quadrata con lato", lato, "e altezza ", altezza, ":", volume_piramide(lato, altezza))


# Esercizio n.20
# Per calcolare la media di alcune misurazioni, è utile prima calcolare la somma e poi fare la divisione in base agli input.
# Per semplicità, si definisca una funzione che calcola la somma di 3 input (con ritorno)
# e un'altra che ne calcola la media (con ritorno).


def somma(*args):
    result = 0
    for elem in args:
        result = result + elem
    return result


def media(*args):
    return somma(*args) / len(args)


print(media(1, 2, 3, 4))


# Gioco!
# Scrivere un programma per un gioco che permetta di indovinare un numero pescato casualmente
# dal computer tramite delle indicazioni basso-alto.
# Il gioco ha le seguenti regole: il sistema estrae un numero compreso tra due valori a scelta (ad esempio, 0-100);
# all'utente viene richiesto di inserire un numero qualsiasi per cercare di indovinare il numero pensato dal sistema;
# questo restituirà un messaggio che dice "Il numero è troppo alto" se il numero inserito è maggiore del numero estratto,
# oppure "Il numero è troppo basso". Se il numero inserito è corretto, si stampa un messaggio e il gioco termina.

# Esempio di flusso:

# Il sistema pesca 97.
# L'utente inserisce in input 3.
# Il sistema verifica che 3 è inferiore a 97, per cui stampa un messaggio adeguato.
# Suggerimento: sfruttare il gioco della palla magica.

import random

print('Gioco')
user_number = int(input('Inserire un numero compreso tra 0 e 100 o -1 per terminare il programma: '))
# estrae un numero intero casuale tra 0 e 100
computer_number = random.randint(0, 100)

while user_number != computer_number and user_number != -1:
    if user_number < computer_number:
        print('Ho pensato ad un numero più grande')
    else:
        print('Ho pensato ad un numero più piccolo')
    user_number = int(input('Riprova o scrivi -1 per terminare il programma: '))

if user_number == computer_number:
    print('Complimenti! Hai vinto!')
else:
    print('Gioco terminato')