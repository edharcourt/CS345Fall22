import psycopg2

"""
Got the list of database names 
    SELECT datname FROM pg_database WHERE datname LIKE '%\_%';

Or something similar
"""

try:
   conn = psycopg2.connect(
       dbname   = 'postgres',
       user     = 'ed',
       host     = 'ada.hpc.stlawu.edu',
       password = 'postgresisawesome')
except:
   print("Error: unable to connect to the database")
   exit()

cur = conn.cursor()

# Turn off transaction mode because DROP DATABASE
# cannot be run within a transaction
conn.autocommit = True

for db in open('dbs.txt'):
    cmd = f'DROP DATABASE IF EXISTS {db.strip()};'
    print(cmd)
    try:
        cur.execute(cmd)
        # cur.commit()  # not running within a transaction
    except psycopg2.Error as e:
        print(f'Error: unable to delete DB {db.strip()}. {e}')

conn.close()
