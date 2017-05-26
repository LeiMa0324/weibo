#coding:utf-8
import pymysql
import csv

'''
该程序负责从三张表中提取出满足以下条件的节点：
1、具有完整的关注关系（在relation表的第一列中）
2、具有已爬取的微博（在weibo表的uid中）
3、发布的微博有评论信息（在comment表的uid中）

以这些节点构建完整的网络
'''
def NodeSelection():
    #检查follow_relation第二列中共涉及了多少个user，有多少在第一列的
    reader = csv.reader("F:\WeiboDataset\followers.csv")
    for row in reader:
        #每一行所有的follower列表
        followers = row[1].split(";")
        print followers
        #批量检查是否满足条件i,插入user_selection表
        batchCheckCondition(followers)



#检查用户是否满足条件i
def batchCheckCondition(users,conditionnum):
    conn = pymysql.connect(host="localhost",user="root",passwd="root",charset="utf8mb4")
    conditionSqldic ={1:"select * from follow_relation where user_id=%s;",
                        2:"select * from weibo where uid=%s;",
                        3:"select * from weibo_comment_info where uid=%s;"}
    #TODO:给weibo_comment_info 加上uid列
    checkResult=[]
    try:
        conn.select_db("weibo")
        cur = conn.cursor()
        for user in users:
            #检查user_selection中是否已存在
            existedflag = cur.fetchone("select * from user_selection where uid=%s;"%user)
            if existedflag:
                pass
            #不存在，建档
            else:
                singleResult=[user]
                for i in range(1,4):
                    result = cur.fetchone(conditionSqldic[i],user)
                    if result:
                        singleResult.append(1)
                    else:
                        singleResult.append(0)
                checkResult.append(singleResult)
        #插入数据库
        cur.executemany("insert into user_selection VALUES (%s,%s,%s,%s)",checkResult)
        conn.commit()
    except Exception,e:
        print e
    finally:
        conn.close()
    print "Batch check finished!"


