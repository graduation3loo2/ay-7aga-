CREATE Database Exodus;

DROP TABLE IF EXISTS `Agencies`;
CREATE TABLE `Agencies` (
  `Agency_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `Address` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `E-mail` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `commercial_id` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `bio` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `promo-code` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `Rate` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `photo_URL` tinytext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`Agency_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `Agencies` VALUES (1,'Lucky Tour','some where','lucky@unlucky.com','1212123','some company','1212122','2','someurl.com'),(2,'Luxor Tour','address','luxor@luxor.com','4544444','another company','4545455','3','anotherurl.com'),(3,'Some company','another address','some@some.com','56456456','yet another comapny','456456456','4','url.com');

DROP TABLE IF EXISTS `Follows`;
CREATE TABLE `Follows` (
  `user_id` int(11) NOT NULL,
  `agency_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`,`agency_id`),
  KEY `Follows_Table_FK_Agency_id_const_idx` (`agency_id`),
  CONSTRAINT `Follows_Table_FK_Agency_id_const` FOREIGN KEY (`agency_id`) REFERENCES `Agencies` (`Agency_id`),
  CONSTRAINT `Follows_Table_FK_User_id_const` FOREIGN KEY (`user_id`) REFERENCES `Users` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

DROP TABLE IF EXISTS `Reports`;
CREATE TABLE `Reports` (
  `report_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `agency_id` int(11) NOT NULL,
  `Message` text COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`report_id`),
  KEY `Reports_table_FK_user_id_const_idx` (`user_id`),
  KEY `Reports_table_FK_Agency_id_const_idx` (`agency_id`),
  CONSTRAINT `Report_Table_FK_Agency_id_Const` FOREIGN KEY (`agency_id`) REFERENCES `Agencies` (`Agency_id`),
  CONSTRAINT `Report_Table_FK_User_id_Const` FOREIGN KEY (`user_id`) REFERENCES `Users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

DROP TABLE IF EXISTS `Response`;
CREATE TABLE `Response` (
  `Vote_id` int(11) NOT NULL,
  `User_id` int(11) NOT NULL,
  `Interested` int(11) NOT NULL,
  `Not_Interested` int(11) NOT NULL,
  PRIMARY KEY (`Vote_id`,`User_id`),
  KEY `Response_Table_FK_User_id_Const_idx` (`User_id`),
  CONSTRAINT `Response_Table_FK_User_id_Const` FOREIGN KEY (`User_id`) REFERENCES `Users` (`user_id`),
  CONSTRAINT `Response_Table_FK_Vote_id_Const` FOREIGN KEY (`Vote_id`) REFERENCES `Vote` (`Vote_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `Response` VALUES (1,1,1,2),(2,1,4,1);

DROP TABLE IF EXISTS `Trip_Photos'`;
CREATE TABLE `Trip_Photos'` (
  `Trip_id` int(11) NOT NULL,
  `URL` text COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`Trip_id`),
  CONSTRAINT `Trip_Photos'_PK_Trip_id_Cons` FOREIGN KEY (`Trip_id`) REFERENCES `Trips` (`Trip_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `Trip_Photos'` VALUES (1,'https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tux.svg/1200px-Tux.svg.png'),(2,'https://media.wired.com/photos/59265fd2af95806129f4f397/master/w_2400,c_limit/MicrosoftVista-4x3.jpg'),(3,'https://media.idownloadblog.com/wp-content/uploads/2018/07/Apple-logo-black-and-white.png'),(4,'https://www.incimages.com/uploaded_files/image/970x450/getty_883231284_200013331818843182490_335833.jpg');

DROP TABLE IF EXISTS `Trips`;

CREATE TABLE `Trips` (
  `Trip_id` int(11) NOT NULL AUTO_INCREMENT,
  `Agency_id` int(11) NOT NULL,
  `Name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `From_Location` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `To_Location` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `Date_From` datetime NOT NULL,
  `Date_To` datetime NOT NULL,
  `Deadline` datetime NOT NULL,
  `Meals` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `Price` double NOT NULL,
  `Description` text COLLATE utf8_unicode_ci NOT NULL,
  `Views` int(10) unsigned NOT NULL DEFAULT 0,
  `Rate` double unsigned NOT NULL DEFAULT 0,
  PRIMARY KEY (`Trip_id`),
  KEY `TripsTable_FK_Agency_id_Const_idx` (`Agency_id`),
  CONSTRAINT `TripsTable_FK_Agency_id_Const` FOREIGN KEY (`Agency_id`) REFERENCES `Agencies` (`Agency_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `Trips` VALUES (1,1,'trip1','Cairo','Giza','2019-05-02 16:13:31','2019-05-07 16:13:28','2019-04-25 16:13:29','fullboard',1200,'some description',80,1),(2,2,'trip2','Luxor','Aswan','2019-06-17 16:14:23','2019-07-10 16:14:31','2019-06-12 16:14:41','halfboard',350,'some another description',120,2),(3,1,'trip3','Cairo','Alexandria','2019-06-09 16:19:58','2019-06-19 16:20:02','2019-06-08 16:20:06','halfboard',1800,'some third description',50,3),(4,3,'trop4','giza','fayoum','2020-04-02 02:20:19','2020-05-04 02:20:20','2019-06-21 02:21:16','fullboard',5000,'fdjhgkjfdhgkjfdhgkjfdhgkjfhd hgfkdhg kjfdhg kjfdhgkjfdh gkhfd kgjhfdkghfdkhgkfdhgkfdhgkfhdkgk hgkfdhgkhfdgkhfdkgh kfdhghfdghfdkhgkjfd kghfdhgfhdgkfhdkjgf',200,4);

DROP TABLE IF EXISTS `Users`;
CREATE TABLE `Users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET latin1 NOT NULL,
  `password` varchar(50) CHARACTER SET latin1 NOT NULL,
  `phone` varchar(11) COLLATE utf8_unicode_ci DEFAULT NULL,
  `city` varchar(45) CHARACTER SET latin1 NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `Users` VALUES (1,'Some one','21212312q','01252545454','Cairo'),(2,'another one','454545454545w','01212313254','Luxor');

DROP TABLE IF EXISTS `Vote`;
CREATE TABLE `Vote` (
  `Vote_id` int(11) NOT NULL AUTO_INCREMENT,
  `Agency_id` int(11) NOT NULL,
  `Name` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `Description` text COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`Vote_id`),
  KEY `Vote_Table_FK_Agency_id_Const_idx` (`Agency_id`),
  CONSTRAINT `Vote_Table_FK_Agency_id_Const` FOREIGN KEY (`Agency_id`) REFERENCES `Agencies` (`Agency_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

;
INSERT INTO `Vote` VALUES (1,1,'vote 1','this is the first vote ever Damn you all kfdsjhfdsjhfjdshfjdkshfkjdshfkj  dskjfhjkdshfkjdshkj fshdjkfhdsjkfhkj hfdskjfh jkdshf kjdshfkj dshf sdjkfhkjdshfjkdshkj dskjf jkhsdkj fhds fsfklsdfsdl kjgfjglkfjklgjfklj fskljgklfjgklfjgklfjgklfjgkljfkl fklgjkldfjgklfdjgkldf'),(2,2,'vote 2','dflkgklfgkldgkjfdkljg lkfdjg kldjg; lkfdjlg dfjg ljdfgjdflkjg lkfdjglkdfjg lkdfjg kljdfklg jfdljg klfdjg lkfdjg lkfdjgkldfjg kldfjg kldfjgkl jdfkl gjdfklg jdfklj glkdfjg ljgldfjgjsdfgl jdflk gjdflk jgkldfjg lkdfjg lkdfjsg lkfdjg kldfjgkl jdfklgj dfklgj fklsdgjldfkjglfkdjg lkfdjg lksfdjg lkdsfjg lkdfjglkdfjgdjg dflk');

DROP TABLE IF EXISTS `going_to`;
CREATE TABLE `going_to` (
  `User_id` int(11) NOT NULL,
  `Trip_id` int(11) NOT NULL,
  PRIMARY KEY (`User_id`),
  KEY `Trip_id_fk` (`Trip_id`),
  CONSTRAINT `Trip_id_fk` FOREIGN KEY (`Trip_id`) REFERENCES `Trips` (`Trip_id`),
  CONSTRAINT `User_id_fk` FOREIGN KEY (`User_id`) REFERENCES `Users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS `phones`;
CREATE TABLE `phones` (
  `Agency_id` int(11) NOT NULL,
  `phone` varchar(13) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`Agency_id`,`phone`),
  CONSTRAINT `Phone_Table_FK_Agency_id_Const` FOREIGN KEY (`Agency_id`) REFERENCES `Agencies` (`Agency_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;