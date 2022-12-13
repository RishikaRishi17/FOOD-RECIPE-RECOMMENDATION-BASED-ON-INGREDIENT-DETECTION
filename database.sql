/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - recipie
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`recipie` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `recipie`;

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_id` int(11) DEFAULT NULL,
  `User_Name` varchar(30) DEFAULT NULL,
  `Feedback` varchar(30) DEFAULT NULL,
  `Rating` varchar(30) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

/*Table structure for table `help` */

DROP TABLE IF EXISTS `help`;

CREATE TABLE `help` (
  `Help_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_id` int(11) NOT NULL,
  `Question` varchar(30) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `Answer` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Help_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `help` */

insert  into `help`(`Help_id`,`User_id`,`Question`,`date`,`Answer`) values 
(1,2,'tyghjk','2022-08-17','asdfghjkl');

/*Table structure for table `ingredient` */

DROP TABLE IF EXISTS `ingredient`;

CREATE TABLE `ingredient` (
  `Ingrdnt_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_id` int(11) NOT NULL,
  `User_name` varchar(30) NOT NULL,
  `ingredient_Name` varchar(30) DEFAULT NULL,
  `Ingredient_Image` varchar(30) NOT NULL,
  PRIMARY KEY (`Ingrdnt_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `ingredient` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `Login_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_Name` varchar(30) NOT NULL,
  `Password` varchar(30) NOT NULL,
  `Login_Type` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`Login_id`,`User_Name`,`Password`,`Login_Type`) values 
(1,'Rishika','Rishi@17','admin');

/*Table structure for table `post` */

DROP TABLE IF EXISTS `post`;

CREATE TABLE `post` (
  `Post_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_id` int(11) DEFAULT NULL,
  `User_Name` int(11) DEFAULT NULL,
  `Caption` varchar(30) DEFAULT NULL,
  `Image` varchar(30) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `comment` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Post_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `post` */

/*Table structure for table `recipie` */

DROP TABLE IF EXISTS `recipie`;

CREATE TABLE `recipie` (
  `Recipie_id` int(11) NOT NULL AUTO_INCREMENT,
  `Recipie_Name` varchar(30) NOT NULL,
  `Recipie_Description` varchar(80) NOT NULL,
  PRIMARY KEY (`Recipie_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `recipie` */

insert  into `recipie`(`Recipie_id`,`Recipie_Name`,`Recipie_Description`) values 
(1,'qwerty','asddfghjklqdhefbcebhbhr');

/*Table structure for table `tips` */

DROP TABLE IF EXISTS `tips`;

CREATE TABLE `tips` (
  `tip_id` int(11) NOT NULL AUTO_INCREMENT,
  `tips` varchar(30) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  PRIMARY KEY (`tip_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `tips` */

insert  into `tips`(`tip_id`,`tips`,`Date`) values 
(1,'tipstips','2022-08-26');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `User_id` int(11) NOT NULL AUTO_INCREMENT,
  `Login_id` int(11) NOT NULL,
  `First_Name` varchar(30) NOT NULL,
  `Address` varchar(30) DEFAULT NULL,
  `dateOfBirth` date DEFAULT NULL,
  `Level` varchar(30) NOT NULL,
  `Phone_Number` bigint(11) DEFAULT NULL,
  `Gender` varchar(20) DEFAULT NULL,
  `Last_Name` varchar(30) NOT NULL,
  PRIMARY KEY (`User_id`,`Login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`User_id`,`Login_id`,`First_Name`,`Address`,`dateOfBirth`,`Level`,`Phone_Number`,`Gender`,`Last_Name`) values 
(1,2,'gfhjk','chgvbjnj,m','2022-08-16','bgfghjk',741852963,'male','gfhbjnm,');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
