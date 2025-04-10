import mysql.connector
import csv
from datetime import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import os

def long(longueur : int) -> str:
    '''Retourne le texte correspondant à la longueur de la liste.'''
    return "(" + ", ".join(["%s"] * longueur) + ")"

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
        messagebox.showinfo("Bonne exécution", "Les tables ont été correctement remplies")

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
            afficher_resultats(colonnes,resultats,fenetre)
        else:
            with db.cursor() as c:
                c.execute(requete)
            db.close()
            messagebox.showinfo("Bonne exécution", "Requête exécutée avec succès")

    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")

def afficher_resultats(colonnes, resultats, fenetre):
    fenetre_resultats = Toplevel(fenetre)
    fenetre_resultats.title("Résultats de la requête SQL")

    tree = ttk.Treeview(fenetre_resultats, columns=colonnes, show="headings")

    # Ajouter les en-têtes
    for col in colonnes:
        tree.heading(col, text=col, anchor="center")
        tree.column(col, anchor="center", width=150)  # Ajuste les largeurs si nécessaire

    # Insérer les données dans le Treeview
    for ligne in resultats:
        tree.insert("", "end", values=ligne)

    scrollbar = ttk.Scrollbar(fenetre_resultats, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)

    tree.pack(padx=10, pady=10, fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
def trouverSQL(text, liste_sql, requetes_sql):
    '''Trouve la requête SQL correspondant au texte.'''
    index = liste_sql.index(text)
    requete = requetes_sql[index]
    return requete
