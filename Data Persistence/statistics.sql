#****************评论统计***********
# 内部评论170.6588W

#68.2169W条在内部相互评论的微博
select count(*) from (select ori_post_id from generated_comment group by ori_post_id)t;


# ori_weibo_id<3460000000000000 generated_comment_1
# ori_weibo_id>3460000000000000 and ori_weibo_id<3470000000000000 generated_comment_2
# ori_weibo_id>3470000000000000  generated_comment_3

#****************转发统计**********
#322.8710W条转发微博
SELECT count(*) FROM weibo_processed.generated_weibo where ori_mid!=0;

#内部转发:ori或者parent在generated_weibo中


#***************微博统计***********
#内部共发布了410.8546W条微博，113.1560W原创，322.8710W条转发
select count(*) from (select mid from generated_weibo order by mid);




##关闭数据库安全模式
SET SQL_SAFE_UPDATES = 0;


#TODO:获取每个用户被邻居转发的总数