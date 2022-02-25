# A prototype binary file archive
# 
import sqlite3

from play import play


def random_clip(cur: sqlite3.Cursor) -> str:
    # Pick one clip at random
    cur.execute('SELECT name, content FROM tunes ORDER BY random() LIMIT 1')
    row = cur.fetchone()
    return (row[0], row[1])


if __name__ == '__main__':
    con = sqlite3.connect('music.db')
    cur = con.cursor()

    name, blob = random_clip(cur)
    print(f"about to play:{name}")

    play(blob)
