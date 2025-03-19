import mysql.connector
import csv
from datetime import datetime
from tkinter import *
from tkinter import messagebox
import mysql.connector
import os


def long(longueur : int) -> str:
    if longueur == 1:
        text = "(%s)"
    elif longueur == 2:
        text = "(%s, %s)"
    elif longueur == 3:
        text = "(%s, %s, %s)"
    elif longueur == 4:
        text = "(%s, %s, %s, %s)"
    elif longueur == 5:
        text = "(%s, %s, %s, %s, %s)"
    return text

def ajout(nomBd, row):
    db = mysql.connector.connect(host="localhost", user="root", password="", database="sea.selmarin")
    db.autocommit = True
    with db.cursor() as c:
        try:
            c.execute("INSERT INTO " + nomBd + " VALUES " + long(len(row)), tuple(row))
        except mysql.connector.errors.IntegrityError:
            print(nomBd + " : La clé primaire déjà existante OU clé étrangère inexistante")
    db.close()

def ajoutBd(nomFichier, longueur):
    db = mysql.connector.connect(host="localhost", user="root", password="", database="sea.selmarin")
    db.autocommit = True
    
    long(longueur)

    try:
        with open(nomFichier +".csv", 'r') as file:
            reader = csv.reader(file, delimiter=";")
            # Sauter l'en-tête si nécessaire (si le fichier CSV a des titres de colonnes)
            header = next(reader)
            for row in reader:
                if nomFichier == "entree" or nomFichier == "sortie":
                    date = list(row[1])
                    date[6:10], date[3:5], date[:2] = date[:2], date[3:5], date[6:10]
                    date = ''.join(date)
                    row[1] = datetime.strptime(date, '%Y/%m/%d')
            
                if nomFichier == "sortie":
                    rowConcerner = [row[3]] + [row[0]] + [row[4]]
                    row = row[:3]
                    ajout("concerner", rowConcerner)
                
                ajout(nomFichier, row)
    except FileNotFoundError:
        print(f"Erreur : Le fichier {nomFichier} n'a pas été trouvé.")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {nomFichier} : {e}")

    # Fermeture de la connexion à la base de données
    db.close()

if __name__ == "__main__":
    ajoutBd("client", 4)
    ajoutBd("sortie", 3)
    ajoutBd("entree", 5)
    ajoutBd("saunier", 4)