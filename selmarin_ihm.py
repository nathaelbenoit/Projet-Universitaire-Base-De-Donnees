from tkinter import *
from tkinter import messagebox
from selmarin import *
from tkinter import ttk

if __name__ == "__main__":
    fenetre = Tk()
    fenetre.title("Interface selmarin")
    
    cadre_principal = Frame(fenetre)
    cadre_principal.pack(padx=10, pady=10, fill="both")

    # Cadre gauche pour les fonctionnalités CSV & requêtes
    cadre_gauche = ttk.Frame(cadre_principal)
    cadre_gauche.pack(side="left", padx=10, anchor="n")

    # Cadre droit pour les boutons d'affichage de tables
    cadre_droit = ttk.Frame(cadre_principal)
    cadre_droit.pack(side="right", padx=10, anchor="n")
    
    # Section pour ajouter un fichier CSV
    TextCsv = Label(cadre_gauche, text="Ajouter un fichier CSV à la base de données",font=("Arial", 10, "bold"))
    TextCsv.pack(pady=5)
    
    fichiersCsv = lister_fichiers_csv()
    variableCSV = StringVar(fenetre)
    variableCSV.set(fichiersCsv[0] if fichiersCsv else "")
    
    listeCsv = ttk.Combobox(cadre_gauche, textvariable=variableCSV, values=fichiersCsv, state="readonly")
    listeCsv.pack(pady=5)
    
    boutonCsv = ttk.Button(cadre_gauche, text="Valider", command=lambda: ajoutExcelBd(variableCSV.get(), nombre_colonnes(variableCSV.get())))
    boutonCsv.pack(pady=5)
    
    # Section pour exécuter des requêtes SQL
    textRequete = Label(cadre_gauche, text="Exécuter une requête SQL",font=("Arial", 10, "bold"))
    textRequete.pack(pady=5)
    
    nomsSQL = ["",
                "Prix moyen des produits par tonne",
                "Clients n'ayant pas commandé certains produits",
                "Classement des clients qui ont le plus commandé",
                "Stock restant par produit",
                "Saunier ayant fourni le plus de sel",
                "Chiffre d'affaires total par année",
                "Clients ayant passé plus de 3 commandes",
                "Renommer le client 11 en INTERMARCHÉ",
                "Classement des produits par nb de commandes",
                "Évolution des prix entre 2023 et 2025"]
    requeteSQL = [
        "NONE",
        "SELECT libPdt, AVG(prixVente) As prix_moyen_T FROM prix, produit  WHERE produit.NUMPDT = prix.NUMPDT GROUP BY prix.NUMPDT;",
        "SELECT client.nomCli, client.precisionCli, client.villeCli, (SELECT libPdt FROM produit WHERE NUMPDT = 1) AS produit_non_commande FROM client WHERE NUMCLI NOT IN (SELECT DISTINCT s.NUMCLI FROM sortie s, concerner c WHERE s.NUMSORT = c.NUMSORT AND c.NUMPDT = 1);",
        "SELECT client.nomCli, client.precisionCli, client.villeCli, SUM(concerner.qteSort_t_ * prix.prixVente) AS somme_achats_euros FROM client, sortie, concerner, prix WHERE client.NUMCLI = sortie.NUMCLI AND sortie.NUMSORT = concerner.NUMSORT AND concerner.NUMPDT = prix.NUMPDT AND prix.numAnnee = YEAR(sortie.dateSort) GROUP BY client.NUMCLI ORDER BY somme_achats_euros DESC;",
        "SELECT p.libPdt,(SUM(e.qteEnt__t_) - SUM(c.qteSort_t_)) AS stock_restant FROM produit p, entree e, concerner c WHERE p.NUMPDT = e.NUMPDT AND p.NUMPDT = c.NUMPDT GROUP BY p.NUMPDT;",
        "SELECT s.nomSau, s.prenomSau, s.villeSau, SUM(c.qteSort_t_) AS total_sel_fournit FROM saunier s, concerner c, sortie so, entree e WHERE e.NUMSAU = s.NUMSAU AND c.NUMSORT = so.NUMSORT AND c.NUMPDT = 1  AND e.NUMPDT = c.NUMPDT GROUP BY s.NUMSAU ORDER BY total_sel_fournit DESC;",
        "SELECT a.numAnnee, SUM((p.prixVente * c.qteSort_t_)) AS chiffre_affaires_total FROM annee a, prix p, concerner c, sortie so WHERE p.numAnnee = a.numAnnee AND c.NUMSORT = so.NUMSORT AND c.NUMPDT = p.NUMPDT GROUP BY a.numAnnee ORDER BY a.numAnnee DESC;",
        "SELECT cl.nomCli, COUNT(so.NUMSORT) AS nombre_achats FROM client cl, sortie so WHERE cl.NUMCLI = so.NUMCLI GROUP BY cl.NUMCLI HAVING COUNT(so.NUMSORT) > 3 ORDER BY nombre_achats DESC;",
        "UPDATE client SET nomCli = 'INTERMARCHÉ' WHERE NUMCLI = 11;",
        "SELECT p.libPdt, COUNT(c.NUMSORT) AS nombre_commandes FROM produit p LEFT JOIN concerner c ON p.NUMPDT = c.NUMPDT GROUP BY p.NUMPDT, p.libPdt ORDER BY nombre_commandes DESC;",
        "SELECT p.libPdt,ROUND(((MAX(CASE WHEN prix.numAnnee = 2025 THEN prix.prixVente END) - MAX(CASE WHEN prix.numAnnee = 2023 THEN prix.prixVente END)) / MAX(CASE WHEN prix.numAnnee = 2023 THEN prix.prixVente END) * 100), 2) AS evolution_pourcentage FROM produit p JOIN prix ON p.NUMPDT = prix.NUMPDT WHERE prix.numAnnee IN (2023, 2025) GROUP BY p.NUMPDT, p.libPdt ORDER BY evolution_pourcentage DESC;"
    ]
    
    variableRequete = StringVar(fenetre)
    variableRequete.set(nomsSQL[0] if nomsSQL else "")
    
    listeRequetes = ttk.Combobox(cadre_gauche, textvariable=variableRequete, values=nomsSQL, state="readonly", width=50)
    listeRequetes.pack(pady=5)
    
    # Zone de texte pour écrire des requêtes SQL personnalisées
    textPerso = Label(cadre_gauche, text="Ou écrire une requête SQL personnalisée",font=("Arial", 8, "bold"))
    textPerso.pack(pady=5)
    
    zoneTextPerso = Text(cadre_gauche, height=10, width=50)
    zoneTextPerso.pack(pady=5)

    boutonRequete = ttk.Button(cadre_gauche, text="Exécuter", command=lambda: executer_requete(variableRequete, zoneTextPerso, afficher_resultats, lambda text: trouverSQL(text, nomsSQL, requeteSQL),fenetre))
    boutonRequete.pack(pady=5)
    
    # Section pour visualiser les tables

    tables = ["annee", "client", "concerner", "entree", "prix", "produit", "saunier", "sortie"]

    textTables = Label(cadre_droit, text="Visualiser une table", font=("Arial", 10, "bold"))
    textTables.pack(pady=5)

    tables = ["annee", "client", "concerner", "entree", "prix", "produit", "saunier", "sortie"]

    for nom_table in tables:
        bouton = ttk.Button(cadre_droit, text=nom_table.capitalize(), padding=(0,8), width=25,
                        command=lambda table=nom_table: (
                            zoneTextPerso.delete("1.0", END),
                            zoneTextPerso.insert(END, f"SELECT * FROM {table};"),
                            executer_requete(variableRequete, zoneTextPerso, afficher_resultats, lambda text: "NONE", fenetre),
                            zoneTextPerso.delete("1.0", END)
                        ))
        bouton.pack(pady=3)
        
    fenetre.mainloop()
