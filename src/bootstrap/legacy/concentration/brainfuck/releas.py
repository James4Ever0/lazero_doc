import sqlite3
# how do you read a book? how do you execute a command?
# def init():
import random, time
# try debugging?
# why so many shits?
# not reading correct programs.
import traceback
# what does it mean really?
# i cannot explain.
def dum():
    r = random.random()*0.1
    time.sleep(r)
# nothing. believe it or not, there's only one thing over there. it is always right.
def createMain():
    conn = sqlite3.connect('Monitor.db', timeout=45)
    conn.text_factory=str
    c = conn.cursor()
    sql = "CREATE TABLE IF NOT EXISTS projects ( \
    ts float NOT NULL, \
    op_type text NOT NULL, \
    op_output text NOT NULL \
);"
    c.execute(sql)
    conn.commit()
    # this thing must be done after every execute.
    conn.close()
    # now bad guys are cops now?
    # so your chance to die is right there?
# i do not care about internal logic. all i need is to fuck it up.
def ins(_table, _t):
    conn = sqlite3.connect('Monitor.db', timeout=45)
    conn.text_factory=str
    c = conn.cursor()
    # sql = "SELECT name FROM "+_table+";"
    # at most two.
    # still not fast enough.
    def sql(t, x, y, z): return c.execute("INSERT INTO " + t +
                                          " (ts,op_type,op_output) VALUES(?,?,?);", (x, y, z))
    # f = []
    # hell is the formatter.
    # for row in c.execute(sql):
    #     f.append(row)
    for x, y, z in _t:
        # print(x, y, z)
        # z=str(z)
        if x is not None and y is not None and z is not None:
            # patience = 3
            patience = 5
            while patience > 0:
                try:
                    sql(_table, x, y, z)
                    conn.commit()
                    print("INSERTED!", y, z)
                    break
                except:
                    e = traceback.format_exc()
                    print(e)
                    # mainly because database is locked. but might have other reasons.
                    print("FAILED! CHANCE: {}".format(patience), y, z)
                    patience -= 1
                    dum()
            if patience == 0:
                print("SERIOUS PROBLEM ENCOUNTERED", y, z)
        else:
            print("GOT EMPTY FOR", y, z)
        # codec problem.
        # # this thing must be done after every execute.
        # # while True:
        # try:
        #     sql(_table, x, y, z)
        #     # break
        # except:
        #     # just do this??
        #     e= traceback.format_exc()
        #     print(e)
        #     # raise Exception("NOT AGAIN!")
        #         # break
    # return f
    conn.commit()
    conn.close()
# def checkTable()
# create a graph instead?
# they will never face the problem.