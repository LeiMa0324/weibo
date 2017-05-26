ALTER TABLE weibo_comment_info ADD INDEX index_ori_com_comment (ori_post_id,com_post_id,comment_user_id);
ALTER TABLE follow_relation ADD INDEX index_userid (user_id);
ALTER TABLE weibo ADD INDEX index_uid_mid (uid,mid,ori_mid);
ALTER TABLE weibo_comment_info ADD INDEX index_ori (ori_post_id);