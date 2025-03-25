from tkinter import *
from fonctions import *

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
    
    bouton_valider = Button(cadre, text="Valider", command=lambda: ajoutExcelBd(variable_fichier.get(), nombre_colonnes(variable_fichier.get())))
    bouton_valider.pack(pady=5)
    
    # Section pour exécuter des requêtes SQL
    label_requete = Label(cadre, text="Exécuter une requête SQL")
    label_requete.pack(pady=5)
    
    liste_sql = ["Rien",
                "Moyenne des prix",
                "Clients n'ayant pas commandé tous les produits",
                "Classement des clients qui sont le plus commandé",
                "Stock restant par produit",
                "Saunier ayant fourni le plus de sel",
                "Chiffre d'affaires total par année",
                "Clients ayant passé plus de 3 commandes",
                "Modifier le nom d'un client",
                "Classement des produits par nb de commandes",
                "Évolution des prix entre 2023 et 2025"]
    requetes_sql = [
        "NONE",
        "SELECT libPdt, AVG(prixVente) As moyennePrixVente FROM prix, produit  WHERE produit.NUMPDT = prix.NUMPDT GROUP BY prix.NUMPDT;",
        "SELECT client.nomCli, client.precisionCli, client.villeCli, (SELECT libPdt FROM produit WHERE NUMPDT = 1) AS produit_non_commande FROM client WHERE NUMCLI NOT IN (SELECT DISTINCT s.NUMCLI FROM sortie s, concerner c WHERE s.NUMSORT = c.NUMSORT AND c.NUMPDT = 1);",
        "SELECT client.nomCli, client.precisionCli, client.villeCli, SUM(concerner.qteSort_t_ * prix.prixVente) AS total_achat FROM client, sortie, concerner, prix WHERE client.NUMCLI = sortie.NUMCLI AND sortie.NUMSORT = concerner.NUMSORT AND concerner.NUMPDT = prix.NUMPDT AND prix.numAnnee = YEAR(sortie.dateSort) GROUP BY client.NUMCLI ORDER BY total_achat DESC;",
        "SELECT p.libPdt,(SUM(e.qteEnt__t_) - SUM(c.qteSort_t_)) AS stock_restant FROM produit p, entree e, concerner c WHERE p.NUMPDT = e.NUMPDT AND p.NUMPDT = c.NUMPDT GROUP BY p.NUMPDT;",
        "SELECT s.nomSau, s.prenomSau, s.villeSau, SUM(c.qteSort_t_) AS total_sel_fournit FROM saunier s, concerner c, sortie so, entree e WHERE e.NUMSAU = s.NUMSAU AND c.NUMSORT = so.NUMSORT AND c.NUMPDT = 1  AND e.NUMPDT = c.NUMPDT GROUP BY s.NUMSAU ORDER BY total_sel_fournit DESC;",
        "SELECT a.numAnnee, SUM((p.prixVente * c.qteSort_t_)) AS chiffre_affaires_total FROM annee a, prix p, concerner c, sortie so WHERE p.numAnnee = a.numAnnee AND c.NUMSORT = so.NUMSORT AND c.NUMPDT = p.NUMPDT GROUP BY a.numAnnee ORDER BY a.numAnnee;",
        "SELECT cl.nomCli, COUNT(so.NUMSORT) AS nombre_achats FROM client cl, sortie so WHERE cl.NUMCLI = so.NUMCLI GROUP BY cl.NUMCLI HAVING COUNT(so.NUMSORT) > 3;",
        "UPDATE client SET nomCli = 'INTERMARCHÉ' WHERE NUMCLI = 11;",
        "SELECT p.NUMPDT, p.libPdt, COUNT(c.NUMSORT) AS nombre_commandes FROM produit p LEFT JOIN concerner c ON p.NUMPDT = c.NUMPDT GROUP BY p.NUMPDT, p.libPdt ORDER BY nombre_commandes DESC;",
        "SELECT p.NUMPDT, p.libPdt,ROUND(((MAX(CASE WHEN prix.numAnnee = 2025 THEN prix.prixVente END) - MAX(CASE WHEN prix.numAnnee = 2023 THEN prix.prixVente END)) / MAX(CASE WHEN prix.numAnnee = 2023 THEN prix.prixVente END) * 100), 2) AS evolution_pourcentage FROM produit p JOIN prix ON p.NUMPDT = prix.NUMPDT WHERE prix.numAnnee IN (2023, 2025) GROUP BY p.NUMPDT, p.libPdt ORDER BY evolution_pourcentage DESC;"
    ]
    
    variable_requete = StringVar(fenetre)
    variable_requete.set(liste_sql[0] if liste_sql else "")
    
    liste_requetes = OptionMenu(cadre, variable_requete, *liste_sql)
    liste_requetes.pack(pady=5)
    
    # Zone de texte pour écrire des requêtes SQL personnalisées
    label_requete_personnalisee = Label(cadre, text="Ou écrire une requête SQL personnalisée")
    label_requete_personnalisee.pack(pady=5)
    
    texte_requete = Text(cadre, height=10, width=50)
    texte_requete.pack(pady=5)

    bouton_requete = Button(cadre, text="Exécuter", command=lambda: executer_requete(variable_requete, texte_requete, afficher_resultats, lambda text: trouverSQL(text, liste_sql, requetes_sql),fenetre))
    bouton_requete.pack(pady=5)
    
    fenetre.mainloop()