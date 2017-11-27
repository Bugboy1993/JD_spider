#reate database JD_test character set gbk;
use JD_test;
DROP TABLE IF EXISTS `JD_name`;
CREATE TABLE `JD_name` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `good_id` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `price` varchar(255) DEFAULT NULL,
  `comment` varchar(255) DEFAULT NULL,
  `shop_name` varchar(255) DEFAULT NULL,
  `link` varchar(255) DEFAULT NULL,
  `score1count` varchar(255) DEFAULT NULL,
  `score2count` varchar(255) DEFAULT NULL,
  `score3count` varchar(255) DEFAULT NULL,
  `score4count` varchar(255) DEFAULT NULL,
  `score5count` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4;
truncate JD_name; 