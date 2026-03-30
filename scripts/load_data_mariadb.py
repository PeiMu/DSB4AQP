import os
import mariadb_util
import sys


scale = 10
if len(sys.argv) > 1:
    scale = sys.argv[1]

tables = ['call_center',
          'catalog_page', 'catalog_returns',
          'catalog_sales',
          'customer', 'customer_address', 'customer_demographics',
          'date_dim', 'household_demographics', 'income_band', 'inventory', 'item', 'promotion', 'reason', 'ship_mode',
          'store', 'store_returns', 'store_sales',
          'time_dim', 'warehouse',
          'web_page', 'web_returns', 'web_sales', 'web_site'
          ]

bin_dir = os.getcwd()
data_path = os.path.join(bin_dir, 'out_' + str(scale))
db_name = 'dsb_' + str(scale)

create_db = False   # set True to create the database
create_table = True  # set True to (re)create tables

# MariaDB credentials
user = 'dsb_10'
password = ''
host = 'localhost'

# create database
if create_db:
    master_conn = mariadb_util.connect(user=user, password=password, host=host)
    master_cursor = master_conn.cursor()
    mariadb_util.execute(master_cursor, 'CREATE DATABASE IF NOT EXISTS ' + db_name, verbose=True)
    master_cursor.close()
    master_conn.close()

# connect to the database
conn = mariadb_util.connect(user=user, password=password, host=host, db_name=db_name)
cursor = conn.cursor()

# create tables
if create_table:
    sql_path = os.path.join(bin_dir, '..', '..', 'scripts', 'create_tables.sql')
    print(sql_path)
    mariadb_util.execute_sql_file(cursor, sql_path, verbose=True, if_not_exists=True)

# insert tuples into tables
for table in tables:
    file_path = os.path.join(data_path, table + '.dat')
    if not os.path.exists(file_path):
        print('Warning: ' + file_path + ' not found, skipping ' + table)
        continue
    mariadb_util.execute(cursor, 'DELETE FROM ' + table, verbose=True)
    mariadb_util.bulk_load(cursor, file_path, table)

cursor.close()
conn.close()
