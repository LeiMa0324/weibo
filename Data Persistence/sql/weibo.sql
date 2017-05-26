CREATE TABLE `weibo` (
  `mid` bigint(20) NOT NULL,
  `uid` bigint(20) DEFAULT NULL,
  `text` longtext,
  `source` longtext,
  `pic_url` longtext,
  `repost_count` int(20) DEFAULT NULL,
  `comment_count` int(20) DEFAULT NULL,
  `created_at` varchar(45) DEFAULT NULL,
  `ori_mid` bigint(20) DEFAULT NULL,
  `flag` int(20) DEFAULT NULL,
  `parent_mid` bigint(20) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;
