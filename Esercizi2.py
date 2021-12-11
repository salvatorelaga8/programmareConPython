# Esercizio 1: Definire un programma che valuta i seguenti casi:
# *Se il parametro passato è uguale a “piove”, allora viene restituita una stringa che dice “rimanda appuntamento”;
# *Se il parametro invece è “sole”, allora viene restituita “puoi partecipare all'evento”;
# *Se non avviene nessuno di questi casi, allora stampa “non ho capito”.

# previsione = input('Digitare PIOVE se piove oppure SOLE se c\'è il sole? ')
previsione = 'PIOVE'
previsione = previsione.lower()
if previsione == 'piove':
    print('Rimanda appuntamento')
elif previsione == 'sole':
    print('Puoi partecipare all\'evento')
else:
    print('Non ho capito!')

# Esercizio 2: Cosa stampa?
a = 33
b = 200
if b > a:
    print("b is greater than a")
# b is greater than a

# Esercizio 3: Scrivi un programma che trovi tutti i numeri che sono divisibili per 7 ma non sono multipli di 5.
# number = int(input('Digitare un numero: '))
number = 35
if (number % 7 == 0 and number % 5 != 0):
    print('Il numero è divisibile per 7 e non è multiplo di 5')
else:
    print('Il numero non è divisibile per 7 o è multiplo di 5')

# Esercizio 4 : Scrivere un programma in grado di calcolare il fattoriale di un dato numero.
# number = int(input('Digitare il numero di cui si vuole calcolare il fattoriale: '))
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

# Esercizio 5: Scrivi un programma per cui, se il voto inserito è maggiore del 65, allora l'esame è passato.
# voto_esame = int(input('Digitare risultato votazione: '))
voto_esame = 80

if voto_esame >= 65:
    print('L\'esame è stato SUPERATO')
else:
    print('l\'esame NON è stato SUPERATO')

# Esercizio 6: Scrivi un programma che stampi se un numero è pari, dispari o negativo.
# number = int(input('Digitare un numero: '))
number = 20

if number >= 0 and number % 2 == 0:
    print('Il numero è POSITIVO e PARI')
elif number >= 0 and number % 2 != 0:
    print('Il numero è POSITIVO e DISPARI')
else:
    print('Il numero è NEGATIVO')

# Esercizio 7: Scrivi un programma che accetti un intero (n) e calcoli il valore di n+nn+nnn.
# number = int(input('Digitare un numero intero n: '))
number = 3
result = number + (number * number) + (number * number * number)
print('Risultato: ', result)

# Esercizio 8: Scrivi un programma per verificare se un numero è compreso tra 100 o 1000 o 2000.
# number = int(input('Digitare un numero intero n: '))
number = 300

if 100 <= number <= 1000:
    print('Il numero appartiene al range [100,1000]')
elif 1000 < number <= 2000:
    print('Il numero appartiene al range (1000,2000]')
else:
    print('Il numero è inferiore a 100 o superiore a 2000')

# Esercizio 9: Scrivi un programma per calcolare la somma di tre numeri dati, se i valori sono uguali restituisci tre volte la loro somma.
number_1 = 5
number_2 = 5
number_3 = 5

if number_1 == number_2 and number_2 == number_3:
    print('Numeri uguali. Risultato: ', 3 * (number_1 + number_2 + number_3))
else:
    print('Numeri diversi. Risultato: ', number_1 + number_2 + number_3)

# Esercizio 10: Scrivi un programma per sommare tre numeri interi dati. Tuttavia, se due valori sono uguali, la somma sarà zero.
number_1 = 6
number_2 = 5
number_3 = 5

if number_1 == number_2 and number_2 == number_3:
    print('Numeri uguali. Risultato: ', 0)
else:
    print('Numeri diversi. Risultato: ', number_1 + number_2 + number_3)

# Esercizio 11: Scrivi un programma che restituirà vero se i due valori interi dati sono uguali o la loro somma o differenza è 5.

number_1 = 8
number_2 = 3

if (number_1 == number_2) or (number_1 + number_2 == 5) or (number_2 - number_1 == 5) or (number_1 - number_2 == 5):
    print(True)
else:
    print(False)

# Esercizio 12: Scrivere un programma che converta il numero del mese nella stringa corrispondente.
# numero_mese = int(input('Inserire numero compreso tra 1 e 12: '))
numero_mese = 1

if numero_mese == 1:
    print('Gennaio')
elif numero_mese == 2:
    print('Febbraio')
elif numero_mese == 3:
    print('Marzo')
elif numero_mese == 4:
    print('Aprile')
elif numero_mese == 5:
    print('Maggio')
elif numero_mese == 6:
    print('Giugno')
elif numero_mese == 7:
    print('Luglio')
elif numero_mese == 8:
    print('Agosto')
elif numero_mese == 9:
    print('Settembre')
elif numero_mese == 10:
    print('Ottobre')
elif numero_mese == 11:
    print('Novembre')
elif numero_mese == 12:
    print('Dicembre')
else:
    print('Conversione non possibile. Inserire numero compreso tra 1 e 12')

# Esercizio 13: Scrivi un programma Python per verificare se un alfabeto è una vocale o una consonante.
lettera = '/'

if lettera in ['a', 'e', 'i', 'o', 'u']:
    print('VOCALE')
elif lettera in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                 'z']:
    print('CONSONANTE')
else:
    print('CARATTERE SPECIALE')

# Esercizio 14: Scrivi un programma Python per verificare che un triangolo sia equilatero, isoscele o scaleno.
lato_1 = 3
lato_2 = 3
lato_3 = 3

if lato_1 == lato_2 and lato_2 == lato_3:
    print('Il triangolo è EQUILATERO')
elif lato_1 != lato_2 and lato_1 != lato_3 and lato_2 != lato_3:
    print('Il triangolo è SCALENO')
else:
    print('Il triangolo è ISOSCELE')

# Esercizio 15: Cosa stampa
x = 'a' if 4 == 2 + 2 else 'b'
print(x)  # x = 'a'
x = 'a' if 4 == 3 + 2 else 'b'
print(x)  # x = 'b'

# Esercizio 16: Crea un programma per soli maggiorenni:
# se la variabile è maggiore di 18, stampa "Puoi entrare", "Non puoi entrare" altrimenti.
# eta = input("Inserisci la tua età: ")
eta = 25
if eta >= 18:
    print('Puoi entrare')
else:
    print('Non puoi entrare')

# Esercizio 17: Scrivi un programma Python per verificare che la password inserita dall'utente
# (salvata precedentemente in una variabile) sia corretta.
# Sia se è corretta, sia se non lo è, stampare un messaggio.

password = 'ReplyAdmin'
# pwd = input('Inserire password utente: ')
pwd = 'ReplyAdmin'

if password == pwd:
    print('La password inserita è corretta. Login in corso')
else:
    print('La password inserita NON è corretta. Login negato')

# Esercizio 18: Scrivi un programma Python per trovare il più grande tra due numeri inseriti in input.
# number_1 = input('Inserire il primo numero: ')
# number_2 = input('Inserire il secondo numero: ')
number_1 = 4
number_2 = 5

if number_1 > number_2:
    print('Il primo numero', number_1, 'è maggiore del secondo ', number_2)
elif number_2 > number_1:
    print('Il secondo numero', number_2, 'è maggiore del primo', number_1)
else:
    print('Il primo numero', number_1, 'è uguale al secondo', number_2)

# Esercizio 19: Scrivi un programma Python per verificare se il numero inserito contiene due, tre o quattro cifre.
# number = int(input('Inserire numero intero positivo: '))
number = 10

if 0 <= number <= 9:
    print('Il numero inserito è ad una cifra')
elif 10 <= number <= 99:
    print('Il numero inserito è a due cifre')
elif 100 <= number <= 999:
    print('Il numero inserito è a tre cifre')
else:
    print('Il numero inserito ha più di quattro cifre')

# Esercizio 20: Scrivi un programma Python per verificare se la stringa è scritta tutta in maiuscolo oppure in minuscolo.
# word = input('Inserire una parola: ')
word = 'Pippo'

if word.islower():
    print('La parola inserita è tutta in minuscolo')
elif word.isupper():
    print('La parola inserita è tutta in maiuscolo')
else:
    print('La stringa contiene caratteri sia minuscoli che maiuscoli')

# Gioco PALLA MAGICA
import random

domanda = input('Fai una domanda alla palla magica: ')
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