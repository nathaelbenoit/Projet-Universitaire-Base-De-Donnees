-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le :  mer. 19 mars 2025 à 09:28
-- Version du serveur :  5.7.17
-- Version de PHP :  5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `sea.selmarin`
--

-- --------------------------------------------------------

--
-- Structure de la table `annee`
--

CREATE TABLE `annee` (
  `numAnnee` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `annee`
--

INSERT INTO `annee` (`numAnnee`) VALUES
(2023),
(2024),
(2025);

-- --------------------------------------------------------

--
-- Structure de la table `client`
--

CREATE TABLE `client` (
  `NUMCLI` int(11) NOT NULL,
  `nomCli` varchar(50) NOT NULL,
  `villeCli` varchar(50) NOT NULL,
  `precisionCli` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `client`
--

INSERT INTO `client` (`NUMCLI`, `nomCli`, `villeCli`, `precisionCli`) VALUES
(1, 'CAVANA', 'Marie', 'La Rochelle'),
(2, 'BURLET', 'Michel', 'Lagord'),
(3, 'PEUTOT', 'Maurice', 'Lagord'),
(4, 'ORGEVAL', 'Centrale d\'Achats', 'Surgères'),
(5, 'SICAAP', 'Centrale d\'Achats', 'FONTCOUVERTE'),
(6, 'GIE DE L\'AUNIS', 'Centrale d\'Achats', 'VOUHE'),
(7, 'EVEILLE', 'Johann', 'LA ROCHELLE'),
(8, 'BARBOTTIN', 'Olivier', 'MEURSAC'),
(9, 'UNION DES PRODUCTEURS DE LA MER', 'Centrale d\'Achats', 'RIVEDOUX'),
(10, 'LIDL', 'Centrale d\'Achats', 'PUILBOREAU'),
(11, 'CARREFOUR', 'Centrale d\'Achats', 'LA ROCHELLE');

-- --------------------------------------------------------

--
-- Structure de la table `concerner`
--

CREATE TABLE `concerner` (
  `NUMPDT` int(11) NOT NULL,
  `NUMSORT` int(11) NOT NULL,
  `qteSort_t_` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `concerner`
--

INSERT INTO `concerner` (`NUMPDT`, `NUMSORT`, `qteSort_t_`) VALUES
(1, 20201, 500),
(1, 20204, 250),
(1, 20205, 150),
(1, 20207, 500),
(1, 20241, 300),
(1, 20242, 200),
(1, 20243, 100),
(1, 202010, 700),
(1, 202011, 200),
(1, 202015, 100),
(1, 202016, 350),
(1, 202018, 100),
(1, 202019, 300),
(1, 202020, 400),
(1, 202022, 200),
(1, 202023, 400),
(1, 202024, 150),
(1, 202025, 300),
(1, 202027, 600),
(1, 202028, 400),
(1, 202029, 300),
(1, 202030, 100),
(1, 202031, 500),
(1, 202032, 200),
(1, 202033, 200),
(1, 202035, 200),
(1, 202037, 300),
(1, 202039, 200),
(1, 202040, 300),
(1, 202041, 200),
(1, 202042, 650),
(1, 202044, 500),
(1, 202045, 300),
(1, 202047, 100),
(1, 202048, 700),
(1, 202049, 300),
(1, 202051, 300),
(1, 202052, 400),
(1, 202054, 300),
(1, 202055, 400),
(1, 202057, 200),
(1, 202058, 300),
(1, 202059, 400),
(1, 202060, 200),
(2, 20201, 500),
(2, 20202, 200),
(2, 20203, 300),
(2, 20204, 200),
(2, 20206, 100),
(2, 20207, 500),
(2, 20208, 200),
(2, 20209, 200),
(2, 20241, 400),
(2, 20243, 500),
(2, 202010, 450),
(2, 202012, 200),
(2, 202014, 100),
(2, 202016, 400),
(2, 202017, 500),
(2, 202019, 300),
(2, 202020, 400),
(2, 202021, 200),
(2, 202025, 300),
(2, 202026, 300),
(2, 202028, 500),
(2, 202031, 500),
(2, 202034, 1000),
(2, 202036, 200),
(2, 202037, 600),
(2, 202043, 400),
(2, 202044, 200),
(2, 202046, 100),
(2, 202048, 1000),
(2, 202053, 700),
(2, 202056, 400),
(2, 202058, 300),
(2, 202059, 400),
(2, 202061, 300);

-- --------------------------------------------------------

--
-- Structure de la table `entree`
--

CREATE TABLE `entree` (
  `NUMENT` int(11) NOT NULL,
  `dateEnt` datetime NOT NULL,
  `qteEnt__t_` int(11) NOT NULL,
  `NUMSAU` int(11) NOT NULL,
  `NUMPDT` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `entree`
--

INSERT INTO `entree` (`NUMENT`, `dateEnt`, `qteEnt__t_`, `NUMSAU`, `NUMPDT`) VALUES
(20201, '2024-01-04 00:00:00', 2000, 1, 1),
(20202, '2024-01-04 00:00:00', 3000, 2, 1),
(20206, '2024-02-05 00:00:00', 3000, 2, 2),
(20209, '2024-05-07 00:00:00', 3000, 1, 1),
(20241, '2024-06-16 00:00:00', 1000, 1, 1),
(20242, '2024-06-18 00:00:00', 500, 1, 2),
(20243, '2024-07-10 00:00:00', 1500, 2, 2),
(202010, '2024-06-08 00:00:00', 3000, 1, 1),
(202011, '2024-06-08 00:00:00', 3000, 2, 1),
(202013, '2024-07-01 00:00:00', 1000, 2, 2);

-- --------------------------------------------------------

--
-- Structure de la table `prix`
--

CREATE TABLE `prix` (
  `NUMPDT` int(11) NOT NULL,
  `numAnnee` int(11) NOT NULL,
  `prixAchat` int(11) DEFAULT NULL,
  `prixVente` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `prix`
--

INSERT INTO `prix` (`NUMPDT`, `numAnnee`, `prixAchat`, `prixVente`) VALUES
(1, 2023, 270, 280),
(1, 2024, 270, 290),
(1, 2025, 240, 300),
(2, 2023, 3900, 9500),
(2, 2024, 3800, 10000),
(2, 2025, 3500, 9000);

-- --------------------------------------------------------

--
-- Structure de la table `produit`
--

CREATE TABLE `produit` (
  `NUMPDT` int(11) NOT NULL,
  `libPdt` varchar(50) NOT NULL,
  `stckPdt` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `produit`
--

INSERT INTO `produit` (`NUMPDT`, `libPdt`, `stckPdt`) VALUES
(1, 'Gros sel', 2000),
(2, 'Fleur de sel', 1000);

-- --------------------------------------------------------

--
-- Structure de la table `saunier`
--

CREATE TABLE `saunier` (
  `NUMSAU` int(11) NOT NULL,
  `nomSau` varchar(50) NOT NULL,
  `prenomSau` varchar(50) NOT NULL,
  `villeSau` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `saunier`
--

INSERT INTO `saunier` (`NUMSAU`, `nomSau`, `prenomSau`, `villeSau`) VALUES
(1, 'YVAN', 'PIERRE', 'Ars-En-Ré'),
(2, 'PETIT', 'MARC', 'Loix'),
(3, 'CARBRAC', 'Léonie', 'Rivedoux'),
(4, 'TARDIVEL', 'Thierry', 'La Couarde');

-- --------------------------------------------------------

--
-- Structure de la table `sortie`
--

CREATE TABLE `sortie` (
  `NUMSORT` int(11) NOT NULL,
  `dateSort` datetime NOT NULL,
  `NUMCLI` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `sortie`
--

INSERT INTO `sortie` (`NUMSORT`, `dateSort`, `NUMCLI`) VALUES
(20201, '2024-01-05 00:00:00', 10),
(20202, '2024-01-06 00:00:00', 2),
(20203, '2024-01-06 00:00:00', 5),
(20204, '2024-01-06 00:00:00', 11),
(20205, '2024-01-09 00:00:00', 2),
(20206, '2024-01-09 00:00:00', 3),
(20207, '2024-01-12 00:00:00', 11),
(20208, '2024-01-12 00:00:00', 6),
(20209, '2024-01-23 00:00:00', 1),
(20241, '2024-07-16 00:00:00', 1),
(20242, '2024-07-18 00:00:00', 1),
(20243, '2024-08-10 00:00:00', 2),
(202010, '2024-02-14 00:00:00', 10),
(202011, '2024-02-14 00:00:00', 3),
(202012, '2024-02-16 00:00:00', 10),
(202013, '2024-02-28 00:00:00', 9),
(202014, '2024-03-08 00:00:00', 1),
(202015, '2024-03-09 00:00:00', 2),
(202016, '2024-03-10 00:00:00', 10),
(202017, '2024-03-19 00:00:00', 7),
(202018, '2024-03-22 00:00:00', 1),
(202019, '2024-03-23 00:00:00', 10),
(202020, '2024-04-04 00:00:00', 11),
(202021, '2024-04-05 00:00:00', 4),
(202022, '2024-04-06 00:00:00', 11),
(202023, '2024-04-17 00:00:00', 10),
(202024, '2024-04-20 00:00:00', 1),
(202025, '2024-04-29 00:00:00', 11),
(202026, '2024-05-02 00:00:00', 3),
(202027, '2024-05-04 00:00:00', 7),
(202028, '2024-05-22 00:00:00', 11),
(202029, '2024-06-03 00:00:00', 10),
(202030, '2024-06-03 00:00:00', 1),
(202031, '2024-06-04 00:00:00', 11),
(202032, '2024-06-05 00:00:00', 6),
(202033, '2024-06-06 00:00:00', 7),
(202034, '2024-06-07 00:00:00', 8),
(202035, '2024-06-09 00:00:00', 2),
(202036, '2024-06-30 00:00:00', 5),
(202037, '2024-07-01 00:00:00', 10),
(202038, '2024-07-01 00:00:00', 9),
(202039, '2024-07-02 00:00:00', 11),
(202040, '2024-07-13 00:00:00', 5),
(202041, '2024-07-24 00:00:00', 7),
(202042, '2024-08-05 00:00:00', 10),
(202043, '2024-08-06 00:00:00', 10),
(202044, '2024-08-06 00:00:00', 11),
(202045, '2024-09-02 00:00:00', 5),
(202046, '2024-09-08 00:00:00', 1),
(202047, '2024-09-19 00:00:00', 7),
(202048, '2024-10-10 00:00:00', 11),
(202049, '2024-10-11 00:00:00', 4),
(202050, '2024-11-02 00:00:00', 9),
(202051, '2024-11-13 00:00:00', 11),
(202052, '2024-11-14 00:00:00', 10),
(202053, '2024-11-15 00:00:00', 10),
(202054, '2024-11-15 00:00:00', 4),
(202055, '2024-11-15 00:00:00', 6),
(202056, '2024-12-08 00:00:00', 11),
(202057, '2024-12-11 00:00:00', 4),
(202058, '2024-12-20 00:00:00', 10),
(202059, '2024-12-21 00:00:00', 11),
(202060, '2024-12-22 00:00:00', 6),
(202061, '2024-12-23 00:00:00', 2);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `annee`
--
ALTER TABLE `annee`
  ADD PRIMARY KEY (`numAnnee`);

--
-- Index pour la table `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`NUMCLI`),
  ADD UNIQUE KEY `nomCli` (`nomCli`,`villeCli`);

--
-- Index pour la table `concerner`
--
ALTER TABLE `concerner`
  ADD PRIMARY KEY (`NUMPDT`,`NUMSORT`),
  ADD KEY `NUMSORT` (`NUMSORT`);

--
-- Index pour la table `entree`
--
ALTER TABLE `entree`
  ADD PRIMARY KEY (`NUMENT`),
  ADD KEY `NUMSAU` (`NUMSAU`),
  ADD KEY `NUMPDT` (`NUMPDT`);

--
-- Index pour la table `prix`
--
ALTER TABLE `prix`
  ADD PRIMARY KEY (`NUMPDT`,`numAnnee`),
  ADD KEY `numAnnee` (`numAnnee`);

--
-- Index pour la table `produit`
--
ALTER TABLE `produit`
  ADD PRIMARY KEY (`NUMPDT`),
  ADD UNIQUE KEY `libPdt` (`libPdt`);

--
-- Index pour la table `saunier`
--
ALTER TABLE `saunier`
  ADD PRIMARY KEY (`NUMSAU`);

--
-- Index pour la table `sortie`
--
ALTER TABLE `sortie`
  ADD PRIMARY KEY (`NUMSORT`),
  ADD KEY `NUMCLI` (`NUMCLI`);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `concerner`
--
ALTER TABLE `concerner`
  ADD CONSTRAINT `concerner_ibfk_1` FOREIGN KEY (`NUMPDT`) REFERENCES `produit` (`NUMPDT`),
  ADD CONSTRAINT `concerner_ibfk_2` FOREIGN KEY (`NUMSORT`) REFERENCES `sortie` (`NUMSORT`);

--
-- Contraintes pour la table `entree`
--
ALTER TABLE `entree`
  ADD CONSTRAINT `entree_ibfk_1` FOREIGN KEY (`NUMSAU`) REFERENCES `saunier` (`NUMSAU`),
  ADD CONSTRAINT `entree_ibfk_2` FOREIGN KEY (`NUMPDT`) REFERENCES `produit` (`NUMPDT`);

--
-- Contraintes pour la table `prix`
--
ALTER TABLE `prix`
  ADD CONSTRAINT `prix_ibfk_1` FOREIGN KEY (`NUMPDT`) REFERENCES `produit` (`NUMPDT`),
  ADD CONSTRAINT `prix_ibfk_2` FOREIGN KEY (`numAnnee`) REFERENCES `annee` (`numAnnee`);

--
-- Contraintes pour la table `sortie`
--
ALTER TABLE `sortie`
  ADD CONSTRAINT `sortie_ibfk_1` FOREIGN KEY (`NUMCLI`) REFERENCES `client` (`NUMCLI`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
