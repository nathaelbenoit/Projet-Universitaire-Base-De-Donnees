INSERT INTO `annee` (`numAnnee`) VALUES
(2023),
(2024),
(2025);


INSERT INTO `client` (`NUMCLI`, `nomCli`, `villeCli`, `precisionCli`) VALUES
(1, 'CAVANA', 'Marie', 'La Rochelle'),
(2, 'BURLET', 'Michel', 'Lagord'),
(3, 'PEUTOT', 'Maurice', 'Lagord'),
(4, 'ORGEVAL', 'Centrale d\'Achats', 'Surgères'),



INSERT INTO `concerner` (`NUMPDT`, `NUMSORT`, `qteSort_t_`) VALUES
( 1, 20241, 300),
( 2, 20241, 400),
( 1, 20242, 200),
( 1, 20243, 100),
( 2, 20243, 500);


INSERT INTO `entree` (`NUMENT`, `dateEnt`, `qteEnt__t_`, `NUMSAU`, `NUMPDT`) VALUES
(20241, '2024-06-16 00:00:00', 1000, 1, 1),
(20242, '2024-06-18 00:00:00', 500, 1, 2),
(20243, '2024-07-10 00:00:00', 1500, 2, 2);


INSERT INTO `prix` (`NUMPDT`, `numAnnee`, `prixAchat`, `prixVente`) VALUES
(1, 2023, 270, 280),
(1, 2024, 270, 290),
(1, 2025, 240, 300),
(2, 2023, 3900, 9500),
(2, 2024, 3800, 10000),
(2, 2025, 3500, 9000);


INSERT INTO `produit` (`NUMPDT`, `libPdt`, `stckPdt`) VALUES
(1, 'Gros sel', 2000),
(2, 'Fleur de sel', 1000);


INSERT INTO `saunier` (`NUMSAU`, `nomSau`, `prenomSau`, `villeSau`) VALUES
(1, 'YVAN', 'PIERRE', 'Ars-En-Ré'),
(2, 'PETIT', 'MARC', 'Loix'),


INSERT INTO `sortie` (`NUMSORT`, `dateSort`, `NUMCLI`) VALUES
(20241, '2024-07-16 00:00:00', 1),
(20242, '2024-07-18 00:00:00', 1),
(20243, '2024-08-10 00:00:00', 2);

