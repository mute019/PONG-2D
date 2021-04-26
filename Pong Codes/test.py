import _sqlite3


conn =  _sqlite3.connect('game.db')
c = conn.cursor()

c.execute("select score, userID from gametab")

result = c.fetchall()
print(result)
conn.commit()
conn.close()