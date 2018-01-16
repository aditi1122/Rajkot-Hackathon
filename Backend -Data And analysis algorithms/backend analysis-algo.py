import MySQLdb

conn = MySQLdb.connect(user="root", passwd="root", db="try1")
cur1 = conn.cursor()
cur2 = conn.cursor()
id1 = conn.cursor()
id2 = conn.cursor()
id3 = conn.cursor()
id4 = conn.cursor()
e = conn.cursor()
updt = conn.cursor()

id1.execute("SELECT sum(overtime) from a1;")
over_time1 = id1.fetchone()

id2.execute("SELECT sum(overtime) from a2;")
over_time2 = id2.fetchone()

id3.execute("SELECT sum(overtime) from a3;")
over_time3 = id3.fetchone()

id4.execute("SELECT sum(overtime) from a4;")
over_time4 = id4.fetchone()

cur1.execute("Select id,easy,medium,hard,rating,score from mock limit 4;")
points1 = cur1.fetchone()

cur2.execute("Select id,sick,casual,earned from b limit 4;")
points2 = cur2.fetchone()

e.execute("Select * from e;")
e1 = e.fetchone()

score = [0,0,0,0,0]

for i in range (1,5):
    score[i] = points1[4]*(points1[1]*2 + points1[2]*4 + points1[3]*7) + points2[1]*3 + points2[2]*5 + points2[3]*8 + e1[1]*5
    if i == 1:
        score[i] = score[i] + over_time1[0]*4
    if i == 2:
        score[i] = score[i] + over_time2[0]*4
    if i == 3:
        score[i] = score[i] + over_time3[0]*4
    if i == 4:
        score[i] = score[i] + over_time4[0]*4

    updt.execute("""update mock set score = %s where id = %s ;""",(score[i],i))
    #cur1.fetchone()
    #cur2.fetchone()
    print i,score[i],points1[5]
    points1 = cur1.fetchone()
    points2 = cur2.fetchone()
    e1 = e.fetchone()
    #print i,score[i],points1[5]
cur1.close()
cur2.close()
id1.close()
id2.close()
id3.close()
id4.close()
conn.commit()
conn.close()

