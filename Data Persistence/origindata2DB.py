# -*- coding: utf-8 -*-

import pymysql

'''
将新浪原始数据集存入数据库
'''


def read(path):
    commentlist=[]
    with open(path, "rb") as f:
        lines = f.readlines()
        for l in lines:
            comment = []
            comment = l.strip('\n').strip('\r').split(',')
            commentlist.append(comment)
    print len(commentlist)
    print commentlist[0]
    return commentlist

# #批量插入数据库
def insert2DB(commentlist):
    conn = pymysql.connect(host="localhost",user="root",passwd="root",charset="utf8")
    try:
        cur = conn.cursor()
        conn.select_db("weibo")
        sql = "INSERT INTO get_weibo(post_id,user_id,content,unkown1,unkown2,create_time,origin_post_id,unkown3) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
        #
        cur.execute("set names 'utf8mb4'")
        cur.executemany(sql,commentlist)
        conn.commit()
        print "success!"
    except Exception,e:
        print e
    finally:
        conn.close()


if __name__ == '__main__':
    insert2DB(read("F:\wang\dataset\Sina\GetWeibo_weibo.txt"))

