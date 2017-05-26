CREATE TABLE if not exists `follow_relation` (
  `id` int(20) not null auto_increment,
  `user_id` bigint NULL ,
  `follower_id` bigint NULL ,
  PRIMARY KEY (`id`)
)DEFAULT CHAR SET utf8;