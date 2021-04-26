import _sqlite3
import os
from pathlib import Path

def extractor(conn, playerID):
    j = 0
    c = conn.cursor()
    c.execute("select score from gametab where userid = (:userid)", {'userid':playerID})
    result = c.fetchone()
    for i in result:
        j = i
    return j
def Unique(players, c):
    status = False
    c.execute("select userid from gametab where userid = (:userid)",{'userid':players})
    if c.fetchone() is None:
        status = True
    elif players == c.fetchone():
        status =  False
    return status

def game_database(score, playerID):
    count = 0
    sum = 0
    if  Path('Resources/Database/game.db').is_file():
        conn = _sqlite3.connect('Resources/Database/game.db')
        c = conn.cursor()
        for i in playerID:
            if not Unique(i, c):
                s = extractor(conn, i)
                sum = s + score[count]
                c.execute("update gametab set score = ? where userid = ?", (sum, i))
                conn.commit()
            else:
                c.execute("Insert into gametab values (:userid, :score)", {'userid': i, 'score': score[count]})
                conn.commit()
            count = count + 1

    elif not Path('Resources/Database/game.db').is_file():
        conn = _sqlite3.connect('Resources/Database/game.db')
        c = conn.cursor()
        c.execute("""create table gametab(
                        userid TEXT PRIMARY KEY NOT NULL,
                        score INT NOT NULL
                        );""")

        for i in playerID:
            c.execute("Insert into gametab values (:userid, :score)", {'userid': i, 'score': score[count]})
            conn.commit()
            count = count + 1

    conn.close()


def main(score_1, score_2, player_1, player_2):
    player1 = player_1
    player2 = player_2
    score1 = score_1
    score2 = score_2
    player = [player1, player2]
    score = [score1,score2]
    game_database(score,player)



