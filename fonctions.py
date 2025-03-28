import mysql.connector
import csv
from datetime import datetime
from tkinter import *
from tkinter import messagebox
import mysql.connector
import os

def long(longueur : int) -> str:
    '''Retourne le texte correspondant à la longueur de la liste.'''
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
    '''Ajoute une ligne à la base de données.'''
    db = mysql.connector.connect(host="localhost", user="root", password="", database="selmarin_final")
    db.autocommit = True
    with db.cursor() as c:
        try:
            c.execute("INSERT INTO " + nomBd + " VALUES " + long(len(row)), tuple(row))
            print(nomBd + " : Ligne ajoutée")
        except mysql.connector.errors.IntegrityError:
            print(nomBd + " : La clé primaire déjà existante OU clé étrangère inexistante")
    db.close()

def ajoutExcelBd(nomFichier, longueur):
    '''Ajoute les données d'un fichier CSV à la base de données.'''
    db = mysql.connector.connect(host="localhost", user="root", password="", database="selmarin_final")
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

def lister_fichiers_csv():
    '''Liste les fichiers CSV dans le répertoire courant.'''
    fichiers_csv = [f[:-4] for f in os.listdir('.') if f.endswith('.csv')]
    return fichiers_csv

def nombre_colonnes(fichier_csv):
    '''Retourne le nombre de colonnes du fichier CSV.'''
    try:
        with open(fichier_csv + ".csv", newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                row_split = row[0].split(';')
                return len(row_split)
    except FileNotFoundError:
        print(f"Erreur : Le fichier {fichier_csv}.csv n'existe pas.")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {fichier_csv}.csv : {e}")

def executer_requete(variable_requete, texte_requete, afficher_resultats, trouverSQL, fenetre):
    '''Exécute une requête SQL.'''
    requete = trouverSQL(variable_requete.get())
    if requete == "NONE":
        return messagebox.showerror("Erreur", "Veuillez sélectionner une requête SQL.")
    requete_personnalisee = texte_requete.get("1.0", "end").strip()
    if requete_personnalisee:
        requete = requete_personnalisee
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="", database="selmarin_final")
        db.autocommit = True
        with db.cursor() as c:
            c.execute(requete)
            colonnes = [desc[0] for desc in c.description]
            resultats = c.fetchall()
        db.close()
        afficher_resultats(colonnes,resultats,fenetre)
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")

def afficher_resultats(colonnes,resultats,fenetre):
    '''Affiche les résultats de la requête SQL.'''
    fenetre_resultats = Toplevel(fenetre)
    fenetre_resultats.title("Résultats de la requête SQL")
    texte_resultats = Text(fenetre_resultats)
    texte_resultats.pack()
    texte_resultats.insert("end", "|".join(colonnes) + "\n")
    texte_resultats.insert("end", "-" * (len('|'.join(colonnes)) +2)+ "\n")
    for ligne in resultats:
        texte_resultats.insert("end",'|'.join(map(str,ligne)) + "\n")

def trouverSQL(text, liste_sql, requetes_sql):
    '''Trouve la requête SQL correspondant au texte.'''
    index = liste_sql.index(text)
    requete = requetes_sql[index]
    return requete