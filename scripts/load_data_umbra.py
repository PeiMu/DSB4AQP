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
data_path = bin_dir + "/out_" + str(scale) + "/"
db_name = "dsb_" + str(scale)

create_table = True

# Umbra connection — uses PostgreSQL wire protocol
user = 'postgres'
password = 'postgres'
host = 'localhost'
port = 15432

conn = pg_util.connect(user=user, password=password, host=host, port=port)
cursor = conn.cursor()

if create_table:
    sql_path = bin_dir + "/../../scripts/create_tables.sql"
    print(sql_path)
    pg_util.execute(cursor, open(sql_path, 'r').read(), verbose=True)

for table in tables:
    file_path = os.path.join(data_path, table + '.dat')
    pg_util.execute(cursor, 'delete from ' + table + ';', verbose=True)
    pg_util.bulk_load_from_csv_file(cursor, file_path, None, table, delimiter='|')

cursor.close()
conn.close()
