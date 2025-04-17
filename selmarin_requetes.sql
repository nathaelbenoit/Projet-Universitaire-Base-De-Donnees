-- 1) moyenne des prix de vente par type de produit
SELECT libPdt, AVG(prixVente) As prix_moyen_T
FROM prix, produit  
WHERE produit.NUMPDT = prix.NUMPDT 
GROUP BY prix.NUMPDT;
 
-- 2) Clients qui n'ont pas commandé un certain type de produit, avec affichage du nom du produit
SELECT client.nomCli, client.precisionCli, client.villeCli, (SELECT libPdt 
                                                            FROM produit 
                                                            WHERE NUMPDT = 1) AS produit_non_commande 
FROM client 
WHERE NUMCLI NOT IN (SELECT DISTINCT s.NUMCLI 
                      FROM sortie s, concerner c 
                      WHERE s.NUMSORT = c.NUMSORT AND c.NUMPDT = 1);
        
-- 3) trier les clients en fonction de leur prix total d'achats
SELECT client.nomCli, client.precisionCli, client.villeCli, SUM(concerner.qteSort_t_ * prix.prixVente) AS somme_achats_euros
FROM client, sortie, concerner, prix 
WHERE client.NUMCLI = sortie.NUMCLI 
AND sortie.NUMSORT = concerner.NUMSORT 
AND concerner.NUMPDT = prix.NUMPDT 
AND prix.numAnnee = YEAR(sortie.dateSort) 
GROUP BY client.NUMCLI 
ORDER BY somme_achats_euros DESC;
       
-- 4) Calcul du stocks restants en fonction des entrees et des sorties
SELECT p.libPdt,(SUM(e.qteEnt__t_) - SUM(c.qteSort_t_)) AS stock_restant 
FROM produit p, entree e, concerner c 
WHERE p.NUMPDT = e.NUMPDT 
AND p.NUMPDT = c.NUMPDT 
GROUP BY p.NUMPDT;
      
-- 5) trouver les sauniers qui ont récoltés le plus de gros sel
SELECT s.nomSau, s.prenomSau, s.villeSau, SUM(c.qteSort_t_) AS total_sel_fournit 
FROM saunier s, concerner c, sortie so, entree e 
WHERE e.NUMSAU = s.NUMSAU 
AND c.NUMSORT = so.NUMSORT 
AND c.NUMPDT = 1  
AND e.NUMPDT = c.NUMPDT 
GROUP BY s.NUMSAU 
ORDER BY total_sel_fournit DESC;
        
-- 6) trouver le CA de l'entreprise par année
SELECT a.numAnnee, SUM((p.prixVente * c.qteSort_t_)) AS chiffre_affaires_total 
FROM annee a, prix p, concerner c, sortie so 
WHERE p.numAnnee = a.numAnnee 
AND c.NUMSORT = so.NUMSORT 
AND c.NUMPDT = p.NUMPDT 
GROUP BY a.numAnnee 
ORDER BY a.numAnnee DESC;
        
-- 7) trouver les clients qui ont fait plus de 3 achats
SELECT cl.nomCli, COUNT(so.NUMSORT) AS nombre_achats 
FROM client cl, sortie so 
WHERE cl.NUMCLI = so.NUMCLI 
GROUP BY cl.NUMCLI 
HAVING COUNT(so.NUMSORT) > 3 
ORDER BY nombre_achats DESC;
       
-- 8) renommer le client 11 en intermarché
UPDATE client SET nomCli = 'INTERMARCHÉ' WHERE NUMCLI = 11;

-- 9) Classement des produits par popularité (nombre de commandes)
SELECT p.libPdt, COUNT(c.NUMSORT) AS nombre_commandes 
FROM produit p LEFT JOIN concerner c ON p.NUMPDT = c.NUMPDT 
GROUP BY p.NUMPDT, p.libPdt 
ORDER BY nombre_commandes DESC;
        
-- 10) Taux d'évolution des prix en pourcentage par type de produit entre 2023 et 2025
SELECT p.NUMPDT, p.libPdt,
       ROUND(((MAX(CASE WHEN prix.numAnnee = 2025 THEN prix.prixVente END) - 
               MAX(CASE WHEN prix.numAnnee = 2023 THEN prix.prixVente END)) / 
               MAX(CASE WHEN prix.numAnnee = 2023 THEN prix.prixVente END) * 100), 2) AS evolution_pourcentage
FROM produit p
JOIN prix ON p.NUMPDT = prix.NUMPDT
WHERE prix.numAnnee IN (2023, 2025)
GROUP BY p.NUMPDT, p.libPdt
ORDER BY evolution_pourcentage DESC;

-- 11) Sauniers demi-milliardaires
CREATE VIEW Sauniers_Millionnaires AS
SELECT 
    s.nomSau AS Nom_Saunier,
    s.prenomSau AS Prenom_Saunier,
    s.villeSau AS Ville,
    SUM(c.qteSort_t_ * p.prixVente) AS Chiffre_Affaires
FROM saunier s
INNER JOIN entree e ON s.numSau = e.numSau
INNER JOIN concerner c ON e.numPdt = c.numPdt
INNER JOIN sortie so ON c.numSort = so.numSort
INNER JOIN prix p ON p.numPdt = c.numPdt
WHERE p.numAnnee = YEAR(so.dateSort)
GROUP BY s.numSau
HAVING SUM(c.qteSort_t_ * p.prixVente) > 500000000
ORDER BY Chiffre_Affaires DESC;

SELECT * FROM Sauniers_Millionnaires;

