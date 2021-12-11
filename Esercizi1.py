# Esercizio 1: Stampa il tuo nome
print("Hello Salvatore!")

# Esercizio 2: Crea una variabile che contenga un nome e una con un numero di telefono, e stampane il contenuto
nome = 'Salvatore'
num_telefonico = 3499341066
print(nome)
print(num_telefonico)

# Esercizio 3: Crea una variabile che contenga una barzelletta e poi stampane il risultato.
barzelletta = "Qual è il colmo per un’agenzia funebre? Essere chiusa per lutto."
print(barzelletta)

# Esercizio 4: Scrivere un programma che restituisca il risultato di tutte le possibile combinazioni dei valori booleani con l'operatore AND.
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Esercizio 5: Scrivere un programma che restituisca il risultato di tutte le possibile combinazioni dei valori booleani con l'operatore NOT AND
print(not (True and True))
print(not (True and False))
print(not (False and True))
print(not (False and False))

# Esercizio 6: Scrivere un programma che, date due variabili a e b rispettivamente uguali a 58 e 43, ne stampi il risultato.
a = 58
b = 43
print(a + b)

# Esercizio 7: Scrivere un programma che, date tre variabili x, y, z, rispettivamente uguali a 3, 4 e 5, ne calcoli prima la somma, e poi la moltiplicazione.
x = 3
y = 4
z = 5
print(x + y + z)
print(x * y * z)

# Esercizio 8: Stampa il risultato della somma tra 328 e 7789.
print(328 + 7789)

# Esercizio 9: Qual è il risultato?
# a. True and not False
# b. True and not false (Notice the capitalization.)
# c. True or True and False
# d. not True or not False
# e. True and not 0 Chapter 5. Making Choices • 94 report erratum • discuss
# f. 52 < 52.3
# g. 1 + 52 < 52.3
# h. 4 != 4.0
print(True and not False)  # true
# print(True and not false) #errore bisogna scrivere False
print(True or True and False)  # true
print(not True or not False)  # true
print(True and not 0)  # true perchè 0 = false 1= true
print(52 < 52.3)  # true
print(1 + 52 < 52.3)  # false
print(4 != 4.0)  # false

# Esercizio 10: Scrivi un'espressione che restituisce True solo se tutte e tre le variabili sono vere.
x = True
y = True
z = True
print(x and y and z)

# Esercizio 11: Scrivi un'espressione per cui viene stampato True solo se la variabile è uguale a False.
x = False
print(not x)

# Esercizio 12: Scrivi un'espressione che stampa True se almeno due delle variabili sono uguali a True.
x = True
y = False
z = True
print((x and y) or (y and z) or (x and z))

# Esercizio 13: Scrivi un commento multiriga.
"""
Questo è un commento
multiriga."""

# Esercizio 14: Cosa stampa
x = 5
y = "Pluto"
print(x)
print(y)
# 5
# Pluto

# Esercizio 15: Cosa stampa
x = 4  # x is of type int
x = "Sally"  # x is now of type str
print(x)
# Sally

# Esercizio 16: Cosa stampa
x = str(3.75)
y = int(3.75)
z = float(3.75)
print(x)
print(y)
print(z)
# 3.75
# 3 -> va sempre per difetto
# 3.75

# Esercizio 17: Sono la stessa cosa? x = "Pippo" x = 'Pippo'
print("Pippo")
print('Pippo')
# Risposta: si

# Esercizio 18: Cosa stampa
a = 4
A = "Pluto"
print(a)
print(A)
# 4
# Pluto

# Esercizio 19: Crea tre variabili e assegna loro i nomi di 3 personaggi di Topolino in una sola riga.
x = 'Tooling'
y = 'Pluto'
z = 'Papering'
# non so

# Esercizio 20: Cosa stampa
# print(5 + 'a')
# unsupported operand type(s) for +: 'int' and 'str'

# Esercizio 21: Qual è il tipo delle seguenti variabili
x = "Paperino"  # string
y = 20.5  # float
z = 1j  # complex
a = True  # bool
b = b"Hello"  # bytes
c = ("a", "b", "c")  # tuple
print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))

# Esercizio 22: Rendi tutta in maiuscolo la seguente stringa: "Index".
x = 'Index'
# isupper() ti dice se la stringa è tutta in maiuscolo
# upper() te la converte in maiuscolo
print(x.upper())

# Esercizio 23: Rendi tutto in minuscolo la seguente stringa: "Index".
x = 'Index'
# islower() ti dice se la stringa è tutta in minuscolo
# lower() te la converte in minuscolo
print(x.lower())

# Esercizio 24: Rimuovi tutti gli spazi dalla seguente stringa.
x = 'Lorem ipsum dolor sit amet.'
print(x.replace(' ', ''))

# Esercizio 25: Sostituisci il placeholder XYZ con un nome.
x = "Ciao XYZ, benvenuto al corso di Python."
print(x.replace('XYZ', 'Salvo'))

# Esercizio 26: Cosa stampa?
a = "Hello"
b = "World"
c = a + b
# HelloWorld
print(c)

# Esercizio 27: Cosa stampa?
a = "Hello"
b = "World"
c = a + " " + b
# Hello World
print(c)

# Esercizio 28: Stampa una stringa che sia esattamente uguale a questa: Un tempo l'Iran si chiamava "Persia".
stringa = 'Un tempo l\'Iran si chiamava "Persia"'
print(stringa)

# Esercizio 29: Input:
# C’è un’ape che se posa su un bottone de rosa: lo succhia e se ne va… Tutto sommato, la felicità è una piccola cosa.
#
# Output:
# C’è un’ape che se posa
# su un bottone de rosa:
# lo succhia e se ne va…
# Tutto sommato, la felicità
# è una piccola cosa.
print('C’è un’ape che se posa' + '\n' + 'su un bottone de rosa:' + '\n'
      + 'lo succhia e se ne va…' + '\n' + 'Tutto sommato, la felicità' + '\n' + ' è una piccola cosa.')
#oppure
print('C’è un’ape che se posa\nsu un bottone de rosa:\nlo succhia e se ne va…\nTutto sommato, la felicità\nè una piccola cosa.')

# Esercizio 30: Rendi l'intera stringa in Camel Case: "prova a mettere ogni lettera iniziale in maiuscolo"
z = 'prova a mettere ogni lettera iniziale in maiuscolo'
print(z.title())

# Esercizio 31: Cosa stampa?
a = "Roma"
print(a.islower())  # false
print(a.isdecimal())  # false
print(a.isnumeric())  # false
print(a.isspace())  # false (true se la stringa ha solo spazi)
print(a.isalnum())  # true (true se contiene solo caratteri alfa numerici)

# Esercizio 32: Stampa la lunghezza della seguente stringa.
b = "Test Yourself With Exercises"
print(b.__len__())
print(len(b))

# Esercizio 33: Cosa stampa?
print(10 > 9)  # true
print(10 == 9)  # false
print(10 < 9)  # false

# Esercizio 34: Cosa stampa?
print(10 % 2)  # 0
print(10 / 2)  # 5
print(10 ** 2)  # 100
print(11 // 2)  # 5 (divisione intera)

# Esercizio 35: Scrivi un programma che, dati la base e l'altezza di un triangolo, ne calcoli l'area.
base = 50
altezza = 4
print((base*altezza)/2)

# Esercizio 36: Scrivere un programma per convertire le temperature da e verso Celsius, Fahrenheit.
gradi_celsius = 20
gradi_farenheit = gradi_celsius * (9/5) + 32
print(gradi_farenheit)