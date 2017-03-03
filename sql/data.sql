
DROP TABLE IF EXISTS `dmoz`;


CREATE TABLE `dmoz` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` text COMMENT '标题',
  `description` text COMMENT '描述',
  `link` text  COMMENT 'url链接',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


CREATE DATABASE ershouche DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
