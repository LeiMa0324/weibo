# coding:utf-8
import csv
import pymysql
import getpass
import sys
import codecs

# reload(sys)

# sys.setdefaultencoding('utf8')
csv.field_size_limit(sys.maxint)

def Ecelrd(excelname):
    rows=[]
    linemum=0
    with open(excelname,'rb') as f:
        # for line in f.readlines():
        #     row = line.strip("\r\n").split(" ")
        #     rows.append(row[0])
        #     print row
        reader =csv.reader(f)
        for line in reader:
            if linemum==0:
                pass
            else:
                line.append(0)
                line.append(0)
                line.append(0)
                rows.append(line)
                print line
            linemum +=1
    return rows


# #批量插入数据库
def insert2DB(rows):
    conn = pymysql.connect(host="localhost", user="root", passwd="root", charset="utf8mb4")
    try:
        conn.select_db("weibo")
        cur = conn.cursor()
        print "excuting..."
        # cur.executemany("insert into new_id_mapping(ori_id,nid) values(%s,%s);",rows)
        string="select uid,mid FROM weibo.weibo where mid=%s;"

        for row in rows:
            sql =string%row
            print "第%s个用户"% rows.index(row)
            cur.execute(sql)
            weibo_user = cur.fetchone()
            if weibo_user:
                tmplist = []
                for i in range(0,len(weibo_user)):
                    tmplist.append(str(weibo_user[i]))
                line = ','.join(tmplist)+'\n'
                print line
                with open("weibo_user.txt",'a') as f:
                    f.write(line)


        #TODO:检查recordlist中哪些不在44514个user中的，删除selecte_comment中的该条记录
        print "success!"

    except Exception,e:
        print e
    finally:
        conn.close()

def temp(rows):
    conn = pymysql.connect(host="localhost", user="root", passwd="root", charset="utf8mb4")
    try:
        conn.select_db("weibo_processed")
        cur = conn.cursor()
        insertsql="insert into count_by_user(uid,comment_num,repost_num,total_num) VALUES (%s,%s,%s,%s)"
        print "inserting..."
        cur.executemany(insertsql,rows)
        conn.commit()
        print "sucess!"
    except Exception,e:
        print e
    finally:
        conn.close()

temp(Ecelrd("users_not_been_commented.csv"))



# conn = pymysql.connect(host="localhost", user="root", passwd="root", charset="utf8mb4")
# try:
#     conn.select_db("weibo_processed")
#     cur = conn.cursor()
#     insertsql = "insert into commentcountbyuser_1(uid,comment_num,repost_num,total_num) VALUES (%s,%s,%s,%s)"
#     print "inserting..."
#     cur.executemany(insertsql, rows)
#     conn.commit()
# except Exception,e:
#     print e
# finally:
#     conn.close()


