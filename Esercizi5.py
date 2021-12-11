# Lezione 5

# Esercizio n.1
# Correggere il seguente codice:
#
# list = [10, 20, 30, 40, 50, 60, 70]
#
# counter = 0
# for element in list:
#     if element % 5 = 0:
#         counter += 1
#
# print(counter)

list = [10, 20, 30, 40, 50, 60, 70]

counter = 0
for element in list:
    if element % 5 == 0:  # == e non =. = è assegnazione, qua bisogna usare == per effettuare un confronto
        counter += 1

print(counter)

# Esercizio n.2
# Correggere il seguente codice:
#
# lst = ['Alice', 'Bob', 'Carl']
# print(lst[3])

lst = ['Alice', 'Bob', 'Carl']
print(lst[2])

# lst[3] da errore perché una lista è indicizzata a partire da 0 fino a length-1 dove length è il numero
# di elementi della lista


# Esercizio n.3
# Correggere il seguente codice:
#
# tupla = ('Alice', 'Bob')
# print(tupla[2])

tupla = ('Alice', 'Bob')
print(tupla[1])


# tupla[2] da errore perché una tupla è indicizzata a partire da 0 fino a length-1 dove length è il numero
# di elementi della tupla


# Esercizio n.4
# Correggere il seguente codice:
#
# def area_cerchio(raggio):
#     print(3.14***raggio**2)
#
# def circonferenza(raggio):
#     print(3.14*raggio*2)
#
# area_cerchiO(3)
# circonfrenza(4)


def area_cerchio(raggio):
    print(3.14 * raggio ** 2)  # perché *** non esiste. L'area del cerchio è 3.14*raggio*raggio.


def circonferenza(raggio):
    print(3.14 * raggio * 2)


area_cerchio(3)  # è stato scritto in maniera sbagliata il nome della funzione da richiamare
circonferenza(4)  # è stato scritto in maniera sbagliata il nome della funzione da richiamare


# Esercizio n.5
# Correggere il seguente codice:
#
# def moltiplicazione(a,b):
#     print a*b
#
# moltiplicazione('a',1)


def moltiplicazione(a, b):
    print(a * b)  # mancavano le parentesi per la funzione print


moltiplicazione('a', 1)
print()


# Esercizio n.6
# Definire una classe che rappresenti un utente e i relativi attributi,
# come lo username, la mail e la data di nascita.

class User:

    def __init__(self, username, email, date_of_birth):
        self.username = username
        self.email = email
        self.date_of_birth = date_of_birth

    def __repr__(self):
        print({'username': self.username, 'email': self.email, 'date_of_birth': self.date_of_birth})

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_date_of_birth(self):
        return self.date_of_birth

    def set_username(self, new_username):
        self.username = new_username

    def set_email(self, new_email):
        self.email = new_email

    def set_date_of_birth(self, new_date_of_birth):
        self.date_of_birth = new_date_of_birth


user = User('salvatorelaga8', 'salvatorelaga8@gmail.com', '08/06/1992')
print("Rappresentazione User")
user.__repr__()
print("Email")
print(user.get_email())
print("Cambio mail in salvatorelaga_8@gmail.com")
user.set_email('salvatorelaga_8@gmail.com')
print('Aggiornamento dati utente')
user.__repr__()
print()


# Esercizio n.7
# Definire una classe che rappresenti
# un auto e i relativi attributi, come la marca, il modello, l'anno di immatricolazione e il numero di porte.

class Auto:

    def __init__(self, marca, modello, anno_immatricolazione, numero_porte):
        self.marca = marca
        self.modello = modello
        self.anno_immatricolazione = anno_immatricolazione
        self.numero_porte = numero_porte

    def __repr__(self):
        print({'marca': self.marca,
               'modello': self.modello,
               'anno di immatricolazione': self.anno_immatricolazione,
               'numero di poorte': self.numero_porte}
              )

    def get_marca(self):
        return self.marca

    def get_modello(self):
        return self.modello

    def get_anno_immatricolazione(self):
        return self.anno_immatricolazione

    def get_numero_porte(self):
        return self.numero_porte

    def set_marca(self, new_marca):
        self.marca = new_marca

    def set_modello(self, new_modello):
        self.modello = new_modello

    def set_anno_immatricolazione(self, new_anno_immatricolazione):
        self.anno_immatricolazione = new_anno_immatricolazione

    def set_numero_porte(self, new_numero_porte):
        self.numero_porte = new_numero_porte


auto = Auto('Ford', 'Fiesta', '01/01/2010', '4')
print('Caratteristiche Auto')
auto.__repr__()
print('Get Marca')
print(auto.get_marca())
print('Il proprietario ha modificato il numero di porte in 5')
auto.set_numero_porte(5)
print('Caratteristiche Auto dopo la modifica')
auto.__repr__()
print()


# Esercizio n.8
# Definire una classe che rappresenti un film: includere
# il regista,
# l'anno di distribuzione, u
# n elenco di attrici e attori,
# il titolo
# il genere.
# Includere i metodi setter e getter per ciascuna proprietà,
# e definire anche un metodo per stamparne i dettagli.

class Film:

    def __init__(self, titolo, genere, regista, anno_distribuzione, attori):
        self.titolo = titolo
        self.genere = genere
        self.regista = regista
        self.anno_distribuzione = anno_distribuzione
        self.attori = attori

    def __repr__(self):
        print({'titolo': self.titolo, 'genere': self.genere, 'regista': self.regista,
               'anno di distribuzione': self.anno_distribuzione, 'attori': self.attori})

    def get_titolo(self):
        return self.titolo

    def get_genere(self):
        return self.genere

    def get_regista(self):
        return self.regista

    def get_anno_distribuzione(self):
        return self.anno_distribuzione

    def get_attori(self):
        return self.attori

    def set_titolo(self, new_titolo):
        self.titolo = new_titolo

    def set_genere(self, new_genere):
        self.genere = new_genere

    def set_regista(self, new_regista):
        self.regista = new_regista

    def set_anno_distribuzione(self, new_anno_distribuzione):
        self.anno_distribuzione = new_anno_distribuzione

    def set_attori(self, new_attori):
        self.attori = new_attori


film = Film('Harry Potter e i Doni della Morte - Parte 2', 'Fantasy',
            'David Yates', '2011', ['Daniel Radcliffe', 'Rupert Grint', 'Emma Watson'])
print('Caratteristiche Film')
film.__repr__()
print('Titolo')
print(film.get_titolo())
print()


# Esercizio n.9
# Definire una classe che rappresenti un immobile, con le relative proprietà
# (locali, bagni, garage (si/no), piano, quartiere)
# e includere i metodi setter e getter per ciascuna proprietà;
# definire anche un metodo per stamparne i dettagli.

# assumo che locali sia una lista contenente le stanze

class Immobile:

    def __init__(self, locali, bagni, garage, piano, quartiere):
        self.locali = locali
        self.bagni = bagni
        self.garage = garage
        self.piano = piano
        self.quartiere = quartiere

    def __repr__(self):
        print({'locali': self.locali, 'bagni': self.bagni, 'garage': self.garage,
               'piano': self.piano, 'quartiere': self.quartiere})

    def get_locali(self):
        return self.locali

    def get_bagni(self):
        return self.bagni

    def get_garage(self):
        return self.garage

    def get_piano(self):
        return self.piano

    def get_quartiere(self):
        return self.quartiere

    def set_locali(self, new_locali):
        self.locali = new_locali

    def set_bagni(self, new_bagni):
        self.bagni = new_bagni

    def set_garage(self, new_garage):
        self.garage = new_garage

    def set_piano(self, new_piano):
        self.piano = new_piano

    def set_quartiere(self, new_quartiere):
        self.quartiere = new_quartiere


immobile = Immobile(['cucina', 'camera da letto', 'soggiorno'], '4', 'si', '2', 'Via Rosario Livatino')
print('Caratteristiche Immmobile')
immobile.__repr__()
print()


# Esercizio n.10
# Definire una classe per rappresentare un/a regista,
# che ne includa le proprietà anagrafiche ed anche i film girati.
# Includere i metodi setter e getter per ciascuna proprietà,
# e definire anche un metodo per stamparne i dettagli.

class Regista:

    def __init__(self, nome, cognome, data_di_nascita, film_girati):
        self.nome = nome
        self.cognome = cognome
        self.data_di_nascita = data_di_nascita
        self.film_girati = film_girati

    def __repr__(self):
        print({'nome': self.nome, 'cognome': self.cognome, 'data di nascita': self.data_di_nascita,
               'film girati': self.film_girati})

    def get_nome(self):
        return self.nome

    def get_cognome(self):
        return self.cognome

    def get_data_di_nascita(self):
        return self.data_di_nascita

    def get_film_girati(self):
        return self.film_girati

    def set_nome(self, new_nome):
        self.nome = new_nome

    def set_cognome(self, new_cognome):
        self.cognome = new_cognome

    def set_data_di_nascita(self, new_data_di_nascita):
        self.data_di_nascita = new_data_di_nascita

    def set_film_girati(self, new_film_girati):
        self.film_girati = new_film_girati


regista = Regista('David', 'Yates', '08-10-1963',
                  ['Harry Potter e l\'ordine della fenice',
                   'Harry Potter e il principe mezzosangue',
                   'Harry Potter e i doni della morte - Parte 1',
                   'Harry Potter e i doni della morte - Parte 2'])
print('Caratteristiche Regista')
regista.__repr__()
print()


# Gioco!
# Definisci una classe per creare un quiz a punti:
# come proprietà il quiz ha una serie di domande e risposte (suggerimento: rappresentarli tramite dizionario),
# per cui vanno definiti i metodi appropriati, tra cui i getter e setter e un metodo per poter giocare.
# Usare domande come le seguenti:
#
# "Quanto fa 5 x 2?": "10",
# "Qual è la radice quadrata di 64?": "8",
# "Quanti sono stati i re di Roma?": "7"

class Quiz:

    def __init__(self, domande_risposte):
        self.domande_risposte = domande_risposte

    def __repr__(self):
        print(self.domande_risposte)

    def get_domande_risposte(self):
        return self.domande_risposte

    def set_domande_risposte(self, new_domande_risposte):
        self.domande_risposte = new_domande_risposte

    def start_quiz(self):
        print('Quiz Game:')
        print('Ti farò una serie di domande. Riceverai 1 punto per ogni risposta corretta data')
        print('Riceverai invece 0 punti per ogni risposta non corretta data')
        print('Iniziamo!')
        punteggio = 0
        for domanda in self.domande_risposte.keys():
            risposta = input(domanda+" ")
            if risposta == self.domande_risposte[domanda]:
                punteggio = punteggio + 1
                print('Risposta corretta! Il tuo punteggio attuale è ', punteggio)
            else:
                print('Risposta sbagliata! Il tuo punteggio resta a', punteggio)
        print('Gioco Terminato. Hai totalizzato', punteggio, 'punti')



domande_risposte = {
    "Quanto fa 5 x 2?": "10",
    "Qual è la radice quadrata di 64?": "8",
    "Quanti sono stati i re di Roma?": "7"
}

quiz = Quiz(domande_risposte)
quiz.start_quiz()