import psycopg2
import csv

# connect to postgresql
conn = psycopg2.connect('host=localhost dbname=postgres user=postgres password=digitalskola')
cur = conn.cursor()

#create table
cur.execute('''CREATE TABLE IF NOT EXISTS user_using_copy(id serial PRIMARY KEY, email text, name text, phone text, postal_code text)''')

with open('./source/users_w_postal_code.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader)
    cur.copy_from(f, 'user_using_copy', sep=',', columns=('email', 'name', 'phone', 'postal_code'))
    # for row in csv_reader:
        # cur.execute('INSERT INTO user_using_copy VALUES (default, %s, %s, %s, %s) ON CONFLICT DO NOTHING', row)

# commit the channges
conn.commit()

#output the result
cur.execute('SELECT * FROM user_using_copy')
conn.commit()
print(cur.fetchall())

