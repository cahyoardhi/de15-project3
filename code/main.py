import psycopg2
import csv

# connect to postgresql
conn = psycopg2.connect('host=localhost dbname=postgres user=postgres password=digitalskola')
cur = conn.cursor()

#create table
cur.execute('''CREATE TABLE IF NOT EXISTS latihan_users(id serial PRIMARY KEY, email text, name text, phone text, postal_code text)''')

with open('./source/users_w_postal_code.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        cur.execute('INSERT INTO latihan_users VALUES (default, %s, %s, %s, %s) ON CONFLICT DO NOTHING', row)

# commit the channges
conn.commit()

#output the result
cur.execute('SELECT * FROM latihan_users')
conn.commit()
print(cur.fetchall())

