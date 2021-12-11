# Lezione 4 : Esercizi

#

# Esercizio n.1
# Creare due tuple che rappresentino i due elenchi di nomi e cognomi descritti sotto:
# nomi: Numa, Tullo, Anco
# cognomi: Pompilio, Ostilio, Marzio

nomi = ('Numa', 'Tullo', 'Anco')
cognomi = ('Pompilio', 'Ostilio', 'Marzio')

print('Tupla nomi:', nomi)
print('Tupla cognomi:', cognomi)

# Esercizio n.2
# Ottenere una lista in cui ogni elemento è un dizionario {'nome': nome, 'cognome': cognome},
# che accoppia nomi e cognomi in base all'ordine.

lista = []

for nome in nomi:
    lista.append({'nome': nome})
index = 0
for cognome in cognomi:
    lista[index]['cognome'] = cognome
    index += 1

print(lista)

# Esercizio n.3
# Creare un dizionario che contenga come chiavi 'nome' e 'cognome', inserendo i propri dati come valori
# Aggiungere 'matricola'
# Aggiungere 'esami', provando ad immaginare che tipi di dato usare per rappresentare sia nome che voto degli esami

anagrafica = {'nome': 'Salvatore', 'cognome': 'Laganà'}
anagrafica['matricola'] = '149357'
anagrafica['esami'] = {'Algebra Lineare e Geometria': '30L',
                       'Fisica': '30L', 'Chimica': '30L',
                       'Analisi Matematica 1': '30'}
print('Anagrafica utente:')
print(anagrafica)

# Esercizio n.4
# Scrivere un programma che, dati i due elenchi di numeri sottostanti, crei la matrice dei loro prodotti:
#
# v1: 1,2,3,4,5
# v2: 6,7,8,9,10
# mat: 16 17 18 ... 26 27 28 ... ... Completare il programma con una stampa della matrice riga per riga.

v1 = [1, 2, 3, 4, 5]
v2 = [6, 7, 8, 9, 10]
matrice = []

for i in v1:
    riga = []
    for j in v2:
        riga.append(i * j)
    matrice.append(riga)

print('Matrice:')
print(matrice)

# Esercizio n.5
# Scrivere un programma che definisca una funzione stampa_matrice(mat),
# che migliori la stampa dell'esercizio precedente, fornendo un formato tabellare.
# Per fare in modo che i numeri siano stampati allineati, usare per ogni numero:
#
# print('%3i' % num)

print('Matrice in forma tabulare')


def stampa_matrice(matrice):
    for elem in matrice:
        print(elem)
    print('')


stampa_matrice(matrice)  # se avessi fatto print(stampa_matrice(matrice)) ti avrebbe stampato un 'None'.
# quando la funzione è di sola stampa, va invocata e basta, senza fare print.

# Esercizio n.6
# Aggiungere al programma precedente una funzione square(val,n),
# che ritorni una matrice quadrata di dimensione n con il valore val in ogni cella .
# Utilizzare la funzione stampa_matrice(mat) per stampare nella console interattiva
# una matrice 6x6 con il valore 0 in ogni cella.


def square(val, n):
    matrice_quadrata = []
    for i in range(0, n):
        riga = []
        for j in range(0, n):
            riga.append(val)
        matrice_quadrata.append(riga)
    return matrice_quadrata


print('Matrice quadrata')
stampa_matrice(square(0, 6))

# Esercizio n.7
# Definire una funzione eratostene(n) che ritorni tutti i numeri primi da 2 a n inclusi,
# utilizzando il procedimento del Crivello di Eratostene:
#
# Si crea un elenco di tutti i numeri naturali da 2 a n, detto setaccio.
# Si aggiunge il primo numero del setaccio all'elenco dei numeri primi trovati,
# e si eliminano dal setaccio tutti i suoi multipli.
# Si prosegue in questo modo fino ad esaurire i numeri nel setaccio.
print()
print('CRIVELLO DI ERATOSTENE')


def crivello_di_eratostene(n):
    setaccio = crea_setaccio(n)
    print('Setaccio')
    print(setaccio)
    index = 0
    for number in setaccio:
        for elem in setaccio[index + 1:]:
            if elem % number == 0:
                setaccio.remove(elem)
        index += 1
    print('Numeri Primi')
    print(setaccio)


def crea_setaccio(n):
    setaccio = []
    for index in range(2, n + 1):
        setaccio.append(index)
    return setaccio


# n = int(input('Inserire un numero intero >=2: '))
crivello_di_eratostene(20)


# Esercizio n.8
# Scrivere una funzione conta_caratteri(s) che ritorni un dizionario contenente
# il numero di occorrenze per ciascun carattere presente nella stringa.


def conta_caratteri(parola):
    occorrenze = {}
    for lettera in parola.lower():
        if lettera in occorrenze:
            occorrenze[lettera] += 1
        else:
            occorrenze[lettera] = 1
    print(occorrenze)


print('Conta Occorrenze parola')
conta_caratteri('salvatore')

# Esercizio n.9
# Scrivere un programma che stampi tutti i numeri perfetti inferiori ad un numero n dato in ingresso.
#
# Un numero naturale è perfetto se è uguale alla somma dei suoi divisori propri e dell'unità.
# Per esempio 6: i divisori propri di 6 sono 2 e 3, e la somma di 2, 3 e dell'unita' ha come risultato 6.
# 0 non è un numero perfetto.

print('NUMERI PERFETTI')


def numeri_perfetti(n):
    lista = crea_lista(n)
    print('Lista numeri')
    print(lista)
    lista_numeri_perfetti = []
    for number in lista:
        lista_divisori = []
        for elem in range(1, number):
            if number % elem == 0:
                lista_divisori.append(elem)
        if somma_divisori(lista_divisori) == number:
            lista_numeri_perfetti.append(number)
    print('Lista Numeri perfetti')
    print(lista_numeri_perfetti)


def somma_divisori(lista_divisori):
    somma = 0
    for divisore in lista_divisori:
        somma += divisore
    return somma


def crea_lista(n):
    lista = []
    for index in range(1, n + 1):
        lista.append(index)
    return lista


numeri_perfetti(40)

# Esercizio n.10
# Stampa i caratteri tra la terza e la sesta posizione della stringa "Hello world!".

parola = 'Hello world!'
print(parola[3:7])

# Esercizio n.11
# Stampa i caratteri dalla terza posizione in poi della stringa "Hello wolrd!".

print(parola[3:])

# Esercizio n.12
# Stampa i caratteri tra la quinta e la seconda posizione della stringa "Hello world!".

print(parola[5:1:-1])


# Esercizio n.13
# Scrivere una funzione reverse(s) che ritorni la stringa passata come parametro al contrario.

def reverse(s):
    print(s[::-1])


reverse('salvatore')

# Esercizio n.14
# Scrivere un programma in grado di calcolare il fattoriale di un dato numero.
# I risultati dovrebbero essere stampati in una sequenza separata da virgole su una singola riga.
# Supponiamo che al programma venga fornito il seguente input: 8 Quindi, l'output dovrebbe essere: 40320

print('')
print('Fattoriale')
number = 8


def fattoriale(x):
    if x == 0 or x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        return x * fattoriale(x - 1)


fatt = fattoriale(number)
print('Il fattoriale è', fatt)


# Esercizio n.15
# Scrivi un programma che, passata come parametro una lista di interi,
# fornisce in output il maggiore tra i numeri contenuti nella lista.

def max_number_list(list):
    max = list[0]
    for number in list:
        if number > max:
            max = number
    print('Il massimo della lista è:', max)


max_number_list([2, 4, 29, 32, 1])


# Esercizio n.16
# Scrivi una funzione che data in ingresso una lista A contenente n parole,
# restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.


def length_word_list(list_a):
    list_b = []
    for word in list_a:
        list_b.append(len(word))
    print('List A:')
    print(list_a)
    print('List B:')
    print(list_b)


length_word_list(['salvatore', 'auto', 'moto', 'cavallo'])

# Esercizio n.17
# Scrivi una funzione a cui passare una stringa come parametro,
# e che restituisca un dizionario rappresentante la "frequenza di comparsa" di ciscun carattere componente la stringa.

# Guarda Esercizio n.8 per la soluzione

# GIOCO
# Gioco!
# In Svezia, i bambini giocano spesso utilizzando un linguaggio un po' particolare detto "rövarspråket",
# che significa "linguaggio dei furfanti": consiste nel raddoppiare ogni consonante di una parola
# e inserire una "o" nel mezzo. Ad esempio la parola "mangiare" diventa "momanongogiarore".
#
# Scrivi una funzione in grado di tradurre una parola o frase passata tramite input in "rövarspråket".
#
# Dopo aver tradotto una frase, il programma dovrà chiedere all'utente se intende tradurne un'altra,
# e in caso di risposta positiva, dovrà attendere l'inserimento di una nuova parola da parte dell'utente.
print('GIOCO')

def rovarspraket():
    parola = input('Inserire parola da tradurre: ')
    vocali_list = ['a', 'e', 'i', 'o', 'u']
    flag = True
    while flag == True:
        parola_tradotta = ""
        for lettera in parola.lower():
            if lettera not in vocali_list:
                parola_tradotta = parola_tradotta + lettera + 'o' + lettera
            else:
                parola_tradotta += lettera
        print('La traduzione della parola è:', parola_tradotta)
        risposta_utente = input('Vuoi continuare a giocare? Digitare S se si o N se no ')
        if risposta_utente.upper() == 'N':
            flag = False
            print('Gioco Terminato')
        elif risposta_utente.upper() == 'S':
            parola = input('Inserire un\'altra parola da tradurre: ')
        else:
            flag = False
            print('Hai inserito una risposta non valida')
            print('Gioco Terminato')


rovarspraket()