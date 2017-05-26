CREATE TABLE if not exists `get_weibo` (
  `id` int(20) not null auto_increment,
  `post_id` bigint NULL ,
  `user_id` bigint NULL ,
  `content` text NULL ,
   `unkown1` int(20) NULL ,
   `unkown2` int(20) NULL ,
   `create_time` varchar(50) NULL ,
   `origin_post_id` bigint NULL ,
   `unkown3`  bigint NULL ,
  PRIMARY KEY (`id`)
)DEFAULT CHAR SET utf8;