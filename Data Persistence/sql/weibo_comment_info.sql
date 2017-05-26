CREATE TABLE if not exists `weibo_comment_info` (
  `id` int(20) not null auto_increment,
  `coment_time` varchar(50) NULL ,
  `origin_post_id` bigint NULL ,
  `comment_post_id` bigint NULL ,
  `comment_user_id` bigint NULL ,
  PRIMARY KEY (`id`)
)DEFAULT CHAR SET utf8;