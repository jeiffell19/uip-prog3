import csv, sqlite3

con = sqlite3.connect("Translator")
cur = con.cursor()

reader = csv.reader(open('list.csv', 'r'), delimiter=',')
for row in reader:
	to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8")]
	print(to_db)
	cur.execute("INSERT INTO 'Translation' ('SPANISH', 'ENGLISH') VALUES (?, ?)", to_db)
	con.commit()

