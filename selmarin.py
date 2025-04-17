import mysql.connector
import csv
from datetime import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import os

def long(longueur: int) -> str:
    '''
    Objectif : Générer une chaîne de caractères représentant un format de paramètres SQL pour une requête préparée.

    Paramètres : longueur : int
                 Nombre de paramètres à inclure dans la chaîne.

    Return : Chaîne de caractères : str
             Exemple : long(3) renvoie "(%s, %s, %s)"

    Exemple d'application : long(5) renvoie "(%s, %s, %s, %s, %s)"
    '''
    return "(" + ", ".join(["%s"] * longueur) + ")"

def ajout(nomFichier: str, row: list) -> None:
    '''
    Objectif : Ajouter une ligne dans une table de la base de données.

    Paramètres : nomFichier : str
                 Nom de la table dans laquelle insérer les données.
                 row : list
                 Liste des valeurs à insérer dans la table.

    Exemple d'application : ajout("utilisateurs", ["1", "Jean", "Doe"]) ajoute une ligne dans la table "utilisateurs".
    '''
    db = mysql.connector.connect(host="localhost", user="root", password="", database="selmarin_final")
    db.autocommit = True
    with db.cursor() as c:
        try:
            c.execute("INSERT INTO " + nomFichier + " VALUES " + long(len(row)), tuple(row))
            print(nomFichier + " : Ligne ajoutée")
        except mysql.connector.errors.IntegrityError:
            print(nomFichier + " : La clé primaire déjà existante OU clé étrangère inexistante")
    db.close()

def ajoutExcelBd(nomFichier: str, longueur: int) -> None:
    '''
    Objectif : Ajouter les données d'un fichier CSV dans une table de la base de données.

    Paramètres : nomFichier : str
                 Nom du fichier CSV (sans extension) et de la table cible.
                 longueur : int
                 Nombre de colonnes dans la table cible.

    Exemple d'application : ajoutExcelBd("produits", 5) insère les données du fichier "produits.csv" dans la table "produits".
    '''
    db = mysql.connector.connect(host="localhost", user="root", password="", database="selmarin_final")
    db.autocommit = True
    try:
        with open(nomFichier + ".csv", 'r') as file:
            reader = csv.reader(file, delimiter=";")
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
        messagebox.showinfo("Bonne exécution", "Les tables ont été correctement remplies")

    except FileNotFoundError:
        print(f"Erreur : Le fichier {nomFichier} n'a pas été trouvé.")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {nomFichier} : {e}")

    db.close()

def lister_fichiers_csv() -> list:
    '''
    Objectif : Lister tous les fichiers CSV présents dans le répertoire courant.

    Paramètres : Aucun.

    Return : Liste des noms de fichiers CSV (sans extension) : list.

    Exemple d'application : lister_fichiers_csv() renvoie ["produits", "clients"] si les fichiers "produits.csv" et "clients.csv" existent.
    '''
    fichiers_csv = [f[:-4] for f in os.listdir('.') if f.endswith('.csv')]
    return fichiers_csv

def nombre_colonnes(nomFichier: str) -> int:
    '''
    Objectif : Déterminer le nombre de colonnes dans un fichier CSV.

    Paramètres : nomFichier : str
                 Nom du fichier CSV (sans extension).

    Return : Nombre de colonnes : int.

    Exemple d'application : nombre_colonnes("produits") renvoie 5 si le fichier "produits.csv" contient 5 colonnes.
    '''
    try:
        with open(nomFichier + ".csv", newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                row_split = row[0].split(';')
                return len(row_split)
    except FileNotFoundError:
        print(f"Erreur : Le fichier {nomFichier}.csv n'existe pas.")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {nomFichier}.csv : {e}")

def executer_requete(variable_requete, texte_requete, afficher_resultats, trouverSQL, fenetre) -> None:
    '''
    Objectif : Exécuter une requête SQL et afficher les résultats si nécessaire.

    Paramètres : variable_requete : tkinter.StringVar
                 Variable contenant le texte de la requête sélectionnée.
                 texte_requete : tkinter.Text
                 Zone de texte contenant une requête personnalisée.
                 afficher_resultats : function
                 Fonction pour afficher les résultats dans une fenêtre.
                 trouverSQL : function
                 Fonction pour récupérer une requête SQL prédéfinie.
                 fenetre : tkinter.Tk
                 Fenêtre principale de l'application.

    Exemple d'application : executer_requete(variable_requete, texte_requete, afficher_resultats, trouverSQL, fenetre) exécute une requête SQL et affiche les résultats.
    '''
    requete = trouverSQL(variable_requete.get())
    requete_personnalisee = texte_requete.get("1.0", "end").strip()
    if requete_personnalisee:
        requete = requete_personnalisee
    if requete == "NONE":
        return messagebox.showwarning("Attention", "Veuillez sélectionner une requête SQL.")
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="", database="selmarin_final")
        db.autocommit = True
        if requete[:6].upper() != 'UPDATE' and requete[:6].upper() != 'INSERT'  and requete[:6].upper() != 'DELETE':
            with db.cursor() as c:
                c.execute(requete)
                colonnes = [desc[0] for desc in c.description]
                resultats = c.fetchall()
            db.close()
            afficher_resultats(colonnes, resultats, fenetre)
        else:
            with db.cursor() as c:
                c.execute(requete)
            db.close()
            messagebox.showinfo("Bonne exécution", "Requête exécutée avec succès")

    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")

def afficher_resultats(colonnes: list, resultats: list, fenetre) -> None:
    '''
    Objectif : Afficher les résultats d'une requête SQL dans une nouvelle fenêtre.

    Paramètres : colonnes : list
                 Liste des noms des colonnes des résultats.
                 resultats : list
                 Liste des lignes de résultats.
                 fenetre : tkinter.Tk
                 Fenêtre principale de l'application.

    Exemple d'application : afficher_resultats(["id", "nom"], [(1, "Jean"), (2, "Marie")], fenetre) affiche les résultats dans une fenêtre.
    '''
    fenetre_resultats = Toplevel(fenetre)
    fenetre_resultats.title("Résultats de la requête SQL")

    tree = ttk.Treeview(fenetre_resultats, columns=colonnes, show="headings")

    for col in colonnes:
        tree.heading(col, text=col, anchor="center")
        tree.column(col, anchor="center", width=150)

    for ligne in resultats:
        tree.insert("", "end", values=ligne)

    scrollbar = ttk.Scrollbar(fenetre_resultats, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)

    tree.pack(padx=10, pady=10, fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

def trouverSQL(text: str, liste_sql: list, requetes_sql: list) -> str:
    '''
    Objectif : Trouver une requête SQL prédéfinie correspondant à un texte donné.

    Paramètres : text : str
                 Texte correspondant à une requête SQL.
                 liste_sql : list
                 Liste des textes associés aux requêtes SQL.
                 requetes_sql : list
                 Liste des requêtes SQL.

    Return : Requête SQL correspondante : str.

    Exemple d'application : trouverSQL("Afficher tous les utilisateurs", ["Afficher tous les utilisateurs"], ["SELECT * FROM utilisateurs"]) renvoie "SELECT * FROM utilisateurs".
    '''
    index = liste_sql.index(text)
    requete = requetes_sql[index]
    return requete