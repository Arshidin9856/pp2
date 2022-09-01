import psycopg2
conn = psycopg2.connect(
	host='localhost',
	database="pp2demo",
	user='pp2demo_user',
	password='pp2demo',)
cursor = conn.cursor()


data = [('Babita', '87761812566'), ('Anushka', '87761812656'),
		('Anamika', '87761951256'), ('Sanaya', '87761995656'),
		('Radha', '8744000')]

for d in data:
	cursor.execute('INSERT into phonebook(name, phone) VALUES (%s, %s)', d)
print(True)
conn.commit()
conn.close()
