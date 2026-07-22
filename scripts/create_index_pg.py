import os
import pg_util
import sys


scale = 10
if len(sys.argv) > 1:
    scale = sys.argv[1]

db_name = r'dsb_' + str(scale) # database name
bin_path = r'/home/pei/Project/project_bins/bin/postgres' # e.g, r'xxx/bin/postgres' # binary of Postgres
sql_path = r'../../scripts/dsb_index_pg.sql'

# start database service
pg_util.start_server()

# postgres credential
user = 'postgres'
password = ''

# connect to the database
conn = pg_util.connect(user = user, password = password, db_name = db_name)
cursor = conn.cursor()

pg_util.execute(cursor, "SET statement_timeout = 0;", verbose=True)
pg_util.execute(cursor, "SET maintenance_work_mem = '1GB';", verbose=True)

# create indexes one at a time
import re
import time
sql = open(sql_path, 'r').read()
stmts = [s.strip() for s in re.split(r';\s*\n', sql) if s.strip() and s.strip() != '--']
for i, stmt in enumerate(stmts):
    if not stmt.lower().startswith('create index'):
        continue
    t0 = time.time()
    print(f'[{i+1}/{len(stmts)}] {stmt[:80]}...')
    pg_util.execute(cursor, stmt, verbose=False)
    print(f'  done in {time.time()-t0:.1f}s')

cursor.close()
conn.close()
