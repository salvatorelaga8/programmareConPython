# Lezione #6

# Esercizio n.1
# Creare una classe per rappresentare una persona (o utilizzarne una precedentemente creata)
# che abbia le proprietà anagrafiche e relativi getter e setter;
# creare poi una classe per rappresentare uno studente e un professore a partire dalla persona,
# aggiungendo proprietà come il numero di matricola e l'elenco degli esami sostenuti (per lo studente),
# e la materia insegnata (per il professore).
import math


class Persona:

    def __init__(self, nome, cognome, data_di_nascita):
        self.nome = nome
        self.cognome = cognome
        self.data_di_nascita = data_di_nascita

    def __repr__(self):
        print({'nome': self.nome, 'cognome': self.cognome, 'data di nascita': self.data_di_nascita})

    def getNome(self):
        return self.nome

    def getCognome(self):
        return self.cognome

    def getDataDiNascita(self):
        return self.data_di_nascita

    def setNome(self, new_nome):
        self.nome = new_nome

    def setCognome(self, new_cognome):
        self.cognome = new_cognome

    def setDataDiNascita(self, new_data_di_nascita):
        self.data_di_nascita = new_data_di_nascita


class Studente(Persona):

    def __init__(self, nome, cognome, data_di_nascita, esami_sostenuti):
        super().__init__(nome, cognome, data_di_nascita)
        self.esami_sostenuti = esami_sostenuti

    def __repr__(self):
        print({'nome': self.nome, 'cognome': self.cognome, 'data di nascita': self.data_di_nascita,
               'esami sostenuti': self.esami_sostenuti})

    def getEsamiSostenuti(self):
        return self.esami_sostenuti

    def setEsamiSostenuti(self, new_esami_sostenuti):
        self.esami_sostenuti = new_esami_sostenuti


class Professore(Persona):

    def __init__(self, nome, cognome, data_di_nascita, materia_insegnata):
        super().__init__(nome, cognome, data_di_nascita)
        self.materia_insegnata = materia_insegnata

    def __repr__(self):
        print({'nome': self.nome, 'cognome': self.cognome, 'data di nascita': self.data_di_nascita,
               'materia insegnata': self.materia_insegnata})

    def getMateriaInsegnata(self):
        return self.materia_insegnata

    def setMateriaInsegnata(self, new_materia_insegnata):
        self.materia_insegnata = new_materia_insegnata


print('Esercizio 1')
studente_a = Studente('Salvatore', 'Laganà', '08/06/1992', {'Algebra': 30, 'Geometria': 30, 'Chimica': 28})
studente_a.__repr__()
print(studente_a.getNome())
print(studente_a.getEsamiSostenuti())
professore_a = Professore('Salvatore', 'Laganà', '08/06/1992', 'Informatica')
professore_a.__repr__()
print()


# Esercizio n.2
# Creare una classe poligono che abbia come attributo il numero di lati e i relativi getter e setter.
# Creare poi una classe per il triangolo e il quadrato, aggiungendo i metodi necessari per calcolare perimetro e area.

class Poligono:

    def __init__(self, numero_lati):
        self.numero_lati = numero_lati

    def __repr__(self):
        return 'Poligono con ' + self.numero_lati + " lati"

    def getNumeroLati(self):
        return self.numero_lati

    def setNumeroLati(self, new_numero_lati):
        self.numero_lati = new_numero_lati


class Triangolo(Poligono):

    def __init__(self, numero_lati, lato_1, lato_2, lato_3):
        super().__init__(numero_lati)
        self.lato_1 = lato_1
        self.lato_2 = lato_2
        self.lato_3 = lato_3

    def __repr__(self):
        return 'Triangolo con ' + str({'lato 1': self.lato_1, 'lato 2': self.lato_2, 'lato 3': self.lato_3})

    def getLato1(self):
        return self.lato_1

    def getLato2(self):
        return self.lato_2

    def getLato3(self):
        return self.lato_3

    def setLato1(self, new_lato_1):
        self.lato_1 = new_lato_1

    def setLato2(self, new_lato_2):
        self.lato_2 = new_lato_2

    def setLato3(self, new_lato_3):
        self.lato_3 = new_lato_3

    def perimetro(self):
        return self.lato_1 + self.lato_2 + self.lato_3

    def area(self):
        semi_perimetro = self.perimetro() / 2
        return math.sqrt(semi_perimetro * (semi_perimetro - self.lato_1) * (semi_perimetro - self.lato_2)
                         * (semi_perimetro - self.lato_3))


class Quadrato(Poligono):

    def __init__(self, numero_lati, lato):
        super().__init__(numero_lati)
        self.lato = lato

    def __repr__(self):
        return 'Quadrato di lato ' + str(self.lato)

    def getLato(self):
        return self.lato

    def setLato(self, new_lato):
        self.lato = new_lato

    def perimetro(self):
        return self.lato * 4

    def area(self):
        return self.lato * self.lato


print('Esercizio 2')
triangolo = Triangolo(3, 20, 25, 15)
print(triangolo.__repr__())
print('Perimetro Triangolo', triangolo.perimetro())
print('Area Triangolo', triangolo.area())
quadrato = Quadrato(4, 3)
print(quadrato.__repr__())
print('Perimetro Quadrato', quadrato.perimetro())
print('Area Quadrato', quadrato.area())
print()


# Esercizio n.3
# Creare una classe che rappresenti un elettrodomestico che abbia come attributo
# il consumo energetico,
# la marca e
# il modello
# e i relativi getter e setter.
# Creare poi una classe per le lavatrici e per i frigoriferi,
# aggiungendo i metodi necessari per restituire informazioni sul numero di giri della centrifuga
# o il numero di porte.

class Elettrodomestico:

    def __init__(self, marca, modello, consumo_energetico):
        self.marca = marca
        self.modello = modello
        self.consumo_energetico = consumo_energetico

    def __repr__(self):
        return str({'marca': self.marca, 'modello': self.modello, 'consumo energetico': self.consumo_energetico})

    def getMarca(self):
        return self.marca

    def getModello(self):
        return self.modello

    def getConsumoEnergetico(self):
        return self.consumo_energetico

    def setMarca(self, new_marca):
        self.marca = new_marca

    def setModello(self, new_modello):
        self.modello = new_modello

    def setConsumoEnergetico(self, new_consumo_energetico):
        self.consumo_energetico = new_consumo_energetico


class Lavatrice(Elettrodomestico):

    def __init__(self, marca, modello, consumo_energetico, numero_giri_centrifuga):
        super().__init__(marca, modello, consumo_energetico)
        self.numero_giri_centrifuga = numero_giri_centrifuga

    def __repr__(self):
        return str({'marca': self.marca, 'modello': self.modello,
                    'consumo energetico': self.consumo_energetico,
                    'numero giri centrifuga': self.numero_giri_centrifuga})

    def getNumeroGiriCentrifuga(self):
        return self.numero_giri_centrifuga

    def setNumeroGiriCentrifuga(self, new_numero_giri_centrifuga):
        self.numero_giri_centrifuga = new_numero_giri_centrifuga


class Frigorifero(Elettrodomestico):

    def __init__(self, marca, modello, consumo_energetico, numero_porte):
        super().__init__(marca, modello, consumo_energetico)
        self.numero_porte = numero_porte

    def __repr__(self):
        return str({'marca': self.marca, 'modello': self.modello,
                    'consumo energetico': self.consumo_energetico,
                    'numero porte': self.numero_porte})

    def getNumeroPorte(self):
        return self.numero_porte

    def setNumeroPorte(self, new_numero_porte):
        self.numero_porte = new_numero_porte


print('Esercizio 3')
lavatrice = Lavatrice('Ariston', 'BK7E', 'A++', '400')
print(lavatrice.__repr__())
lavatrice.setNumeroGiriCentrifuga('500')
print(lavatrice.__repr__())
frigorifero = Frigorifero('Smeg', 'ABC768', 'A++', '3')
print(frigorifero.__repr__())
frigorifero.setNumeroPorte('4')
print(frigorifero.__repr__())
print()


# Esercizio n.5
# Scrivere una classe Opera, che ha come attributi
# un titolo,
# un autore,
# un anno di commissione,
# un luogo d'esposizione ed
# un anno di ritrovamento.
# Un'opera può essere un quadro o una scultura:
# un quadro può avere
# una tecnica di pittura,
# una cornice
# e un restauratore;
# una scultura può
# essere di diversi materiale,
# avere una base oppure no.
# Scrivere quindi le opportune funzioni e inizializzare degli oggetti per testare la classe.

class Opera:

    def __init__(self, titolo, autore, anno_commissione, luogo_esposizione, anno_ritrovamento):
        self.titolo = titolo
        self.autore = autore
        self.anno_commissione = anno_commissione
        self.luogo_esposizione = luogo_esposizione
        self.anno_ritrovamento = anno_ritrovamento

    def __repr__(self):
        return str({'titolo': self.titolo, 'autore': self.autore, 'anno commissione': self.anno_commissione,
                    'luogo esposizione': self.luogo_esposizione, 'anno ritrovamento': self.anno_ritrovamento})

    def getTitolo(self):
        return self.titolo

    def getAutore(self):
        return self.autore

    def getAnnoCommissione(self):
        return self.anno_commissione

    def getLuogoEsposizione(self):
        return self.luogo_esposizione

    def getAnnoRitrovamento(self):
        return self.anno_ritrovamento


class Quadro(Opera):

    def __init__(self, titolo, autore, anno_commissione, luogo_esposizione, anno_ritrovamento,
                 tecnica_di_pittura, cornice=None, restauratore=None):
        super().__init__(titolo, autore, anno_commissione, luogo_esposizione, anno_ritrovamento)
        self.tecnica_di_pittura = tecnica_di_pittura
        self.cornice = cornice
        self.restauratore = restauratore

    def __repr__(self):
        return str({'titolo': self.titolo, 'autore': self.autore, 'anno commissione': self.anno_commissione,
                    'luogo esposizione': self.luogo_esposizione, 'anno ritrovamento': self.anno_ritrovamento,
                    'tecnica di pittura': self.tecnica_di_pittura, 'cornice': self.cornice,
                    'restauratore': self.restauratore})

    def getTecnicaDiPittura(self):
        return self.tecnica_di_pittura

    def getCornice(self):
        return self.cornice

    def getRestauratore(self):
        return self.restauratore

    def setTecnicaDiPittura(self, new_tecnica_di_pittura):
        self.tecnica_di_pittura = new_tecnica_di_pittura

    def setCornice(self, new_cornice):
        self.cornice = new_cornice

    def setRestauratore(self, new_restauratore):
        self.restauratore = new_restauratore


class Scultura(Opera):

    def __init__(self, titolo, autore, anno_commissione, luogo_esposizione, anno_ritrovamento, lista_materiali, base):
        super().__init__(titolo, autore, anno_commissione, luogo_esposizione, anno_ritrovamento)
        self.lista_materiali = lista_materiali
        self.base = base

    def __repr__(self):
        return str({'titolo': self.titolo, 'autore': self.autore, 'anno commissione': self.anno_commissione,
                    'luogo esposizione': self.luogo_esposizione, 'anno ritrovamento': self.anno_ritrovamento,
                    'lista materiali': self.lista_materiali, 'base': self.base})

    def getListaMateriali(self):
        return self.lista_materiali

    def getBase(self):
        return self.base

    def setListaMateriali(self, new_lista_materiali):
        self.lista_materiali = new_lista_materiali

    def setBase(self, new_base):
        self.base = new_base

print('Esercizio 5')
quadro = Quadro('La libertà che guida il popolo', 'Eugène Delacroix', '1830', 'Museo del Louvre, Parigi', '1830',
                'olio su tela')
print(quadro.__repr__())
print(quadro.getRestauratore())
print()

# Esercizio n.6
# Scrivere una classe Animale, che ha come attributi una specie, un habitat e una certa vita media.
# Un animale può essere di moltissime specie, ma ne prendiamo in esame solo due: un cane ed un elefante.
# Attribuire ai due animali i giusti attributi che li distinguano e scrivere quindi le opportune funzioni,
# inizializzando degli oggetti per testare la classe.

class Animale:

    def __init__(self, specie, habitat, vita_media):
        self.specie = specie
        self.habitat = habitat
        self.vita_media = vita_media

    def __repr__(self):
        return str({'specie': self.specie, 'habitat': self.habitat, 'vita media': self.vita_media})

    def getSpecie(self):
        return self.specie

    def getHabitat(self):
        return self.habitat

    def getVitaMedia(self):
        return self.vita_media

    def setSpecie(self, new_specie):
        self.specie = new_specie

    def setHabitat(self, new_habitat):
        self.habitat = new_habitat

    def setVitaMedia(self, new_vita_media):
        self.vita_media = new_vita_media


class Cane(Animale):

    def __init__(self, specie, habitat, vita_media, peso, colore):
        super().__init__(specie, habitat, vita_media)
        self.peso = peso
        self.colore = colore

    def __repr__(self):
        return str({'specie': self.specie, 'habitat': self.habitat, 'vita media': self.vita_media,
                    'peso': self.peso, 'colore': self.colore})

    def getPeso(self):
        return self.peso

    def getColore(self):
        return self.colore

    def setPeso(self, new_peso):
        self.peso = new_peso

    def setColore(self, new_colore):
        self.colore = new_colore


class Elefante(Animale):

    def __init__(self, specie, habitat, vita_media, peso, altezza):
        super().__init__(specie, habitat, vita_media)
        self.peso = peso
        self.altezza = altezza

    def __repr__(self):
        return str({'specie': self.specie, 'habitat': self.habitat, 'vita media': self.vita_media,
                    'peso': self.peso, 'altezza': self.altezza})

    def getPeso(self):
        return self.peso

    def getAltezza(self):
        return self.altezza

    def setPeso(self, new_peso):
        self.peso = new_peso

    def setAltezza(self, new_altezza):
        self.altezza = new_altezza