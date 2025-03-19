from tkinter import *
from tkinter import messagebox
import mysql.connector
import os
import csv
from python import ajoutBd

def lister_fichiers_csv():
    '''Liste les fichiers CSV dans le répertoire courant.'''
    fichiers_csv = [f[:-4] for f in os.listdir('.') if f.endswith('.csv')]
    return fichiers_csv

def nombre_colonnes(fichier_csv):
    '''Retourne le nombre de colonnes du fichier CSV.'''
    with open(fichier_csv + ".csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            return len(row)

def ajouter_csv():
    '''Ajoute un fichier CSV à la base de données.'''
    fichier_csv = variable_fichier.get()
    if fichier_csv:
        fichier_csv_complet = fichier_csv + ".csv"
        if os.path.exists(fichier_csv_complet):
            nb_colonnes = nombre_colonnes(fichier_csv)
            ajoutBd(fichier_csv, nb_colonnes)
            messagebox.showinfo("Succès", "Le fichier CSV a été ajouté à la base de données avec succès.")
        else:
            messagebox.showerror("Erreur", f"Le fichier {fichier_csv_complet} n'existe pas.")

def executer_requete():
    requete = variable_requete.get()
    requete_personnalisee = texte_requete.get("1.0", END).strip()
    if requete_personnalisee:
        requete = requete_personnalisee
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="", database="selmarin_final")
        db.autocommit = True
        with db.cursor() as c:
            c.execute(requete)
            resultats = c.fetchall()
        db.close()
        afficher_resultats(resultats)
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")

def afficher_resultats(resultats):
    fenetre_resultats = Toplevel(fenetre)
    fenetre_resultats.title("Résultats de la requête SQL")
    texte_resultats = Text(fenetre_resultats)
    texte_resultats.pack()
    for ligne in resultats:
        texte_resultats.insert(END, str(ligne) + "\n")

if __name__ == "__main__":
    fenetre = Tk()
    fenetre.title("Interface selmarin")
    
    cadre = Frame(fenetre)
    cadre.pack(pady=10)
    
    # Section pour ajouter un fichier CSV
    label_csv = Label(cadre, text="Ajouter un fichier CSV à la base de données")
    label_csv.pack(pady=5)
    
    fichiers_csv = lister_fichiers_csv()
    variable_fichier = StringVar(fenetre)
    variable_fichier.set(fichiers_csv[0] if fichiers_csv else "")
    
    liste_deroulante = OptionMenu(cadre, variable_fichier, *fichiers_csv)
    liste_deroulante.pack(pady=5)
    
    bouton_valider = Button(cadre, text="Valider", command=ajouter_csv)
    bouton_valider.pack(pady=5)
    
    # Section pour exécuter des requêtes SQL
    label_requete = Label(cadre, text="Exécuter une requête SQL")
    label_requete.pack(pady=5)
    
    requetes_sql = [
        "NONE",
        "SELECT * FROM client",
        "SELECT * FROM sortie",
        "SELECT * FROM entree",
        "SELECT * FROM saunier"
    ]
    
    variable_requete = StringVar(fenetre)
    variable_requete.set(requetes_sql[0] if requetes_sql else "")
    
    liste_requetes = OptionMenu(cadre, variable_requete, *requetes_sql)
    liste_requetes.pack(pady=5)
    
    # Zone de texte pour écrire des requêtes SQL personnalisées
    label_requete_personnalisee = Label(cadre, text="Ou écrire une requête SQL personnalisée")
    label_requete_personnalisee.pack(pady=5)
    
    texte_requete = Text(cadre, height=10, width=50)
    texte_requete.pack(pady=5)

    bouton_requete = Button(cadre, text="Exécuter", command=executer_requete)
    bouton_requete.pack(pady=5)
    
    fenetre.mainloop()