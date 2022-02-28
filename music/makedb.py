# Create a SQLite database with a table for storing music clips

import sqlite3

database = 'music.db'

con = sqlite3.connect(database)
cur = con.cursor()

# Identifiers don't need to be quoted, unless they are a keyword, however it's good practice to quote.
# https://www.sqlite.org/lang_keywords.html
cur.execute('CREATE TABLE "tunes" ("name" TEXT PRIMARY KEY, "content" BLOB, "size" INTEGER, "album" TEXT)')

con.commit()
con.close()
