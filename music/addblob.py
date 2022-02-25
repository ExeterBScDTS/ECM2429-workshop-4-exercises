# A prototype binary file archive
# 
import sqlite3
import logging
import sys
import os

logging.basicConfig(level=logging.DEBUG)


def add_blob(cursor, name: str, content: any, size: int, album: str) -> bool:
    logging.debug(f'add_blob({name})')
    sql_insert = 'INSERT INTO "tunes" ("name", "content", "size", "album") VALUES (?, ?, ?, ?)'
    cursor.execute(sql_insert, (name, content, size, album))
    return True


if __name__ == '__main__':
    try:
        album = sys.argv[1]
        con = sqlite3.connect('music.db')
        cur = con.cursor()
    except IndexError:
        sys.exit("Usage: addalbum.py album_name")

    for p in os.listdir(album):
        if p.endswith(".wav"):
            data = open(album + "/" + p, "rb").read()
            size = len(data)
            name = p[3:-4]
            print(f"{name} {size}")
            add_blob(cur, name, data, size, album)
    
    con.commit()
    con.close()
