import os
import pg_util
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
bin_path = os.path.join(bin_dir, 'dsdgen')

data_path = bin_dir + "/out_" + str(scale) + "/"  # directory of data files
db_name = "dsb_" + str(scale)  # database name
tmp_csv_path = data_path + "tmp"  # path of tmp csv file for bulk loading

create_db = False # If create the database
create_table = True # If create the tables

# postgres credential
user = 'postgres'
password = ''

# create database
if create_db:
    master_conn = pg_util.connect(user=user, password=password)
    pg_util.execute(master_conn.cursor(), 'create database ' + db_name, verbose=True)
    master_conn.close()

# connect to the database
conn = pg_util.connect(user=user, password=password, db_name=db_name)
cursor = conn.cursor()

# create tables
if create_table:
    sql_path = bin_dir + "/../../scripts/create_tables.sql"
    print(sql_path)
    pg_util.execute(cursor, open(sql_path, 'r').read(), verbose=True)

# insert tuples into tables
for table in tables:
    file_path = os.path.join(data_path, table + '.dat')
    pg_util.execute(cursor, 'delete from ' + table + ';', verbose=True)
    pg_util.bulk_load_from_csv_file(cursor, file_path, tmp_csv_path, table, delimiter='|') # if dat is larger than memory
    # pg_util.load_from_csv_file(cursor, file_path, table, delimiter='|') # if dat is smaller than memory

#os.remove(tmp_csv_path)

cursor.close()
conn.close()
