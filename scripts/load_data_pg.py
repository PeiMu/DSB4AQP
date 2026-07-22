import os
import time
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

primary_keys = {
    'call_center': ('call_center_pkey', ['cc_call_center_sk']),
    'catalog_page': ('catalog_page_pkey', ['cp_catalog_page_sk']),
    'catalog_returns': ('catalog_returns_pkey', ['cr_item_sk', 'cr_order_number']),
    'catalog_sales': ('catalog_sales_pkey', ['cs_item_sk', 'cs_order_number']),
    'customer': ('customer_pkey', ['c_customer_sk']),
    'customer_address': ('customer_address_pkey', ['ca_address_sk']),
    'customer_demographics': ('customer_demographics_pkey', ['cd_demo_sk']),
    'date_dim': ('date_dim_pkey', ['d_date_sk']),
    'household_demographics': ('household_demographics_pkey', ['hd_demo_sk']),
    'income_band': ('income_band_pkey', ['ib_income_band_sk']),
    'inventory': ('inventory_pkey', ['inv_date_sk', 'inv_item_sk', 'inv_warehouse_sk']),
    'item': ('item_pkey', ['i_item_sk']),
    'promotion': ('promotion_pkey', ['p_promo_sk']),
    'reason': ('reason_pkey', ['r_reason_sk']),
    'ship_mode': ('ship_mode_pkey', ['sm_ship_mode_sk']),
    'store': ('store_pkey', ['s_store_sk']),
    'store_returns': ('store_returns_pkey', ['sr_item_sk', 'sr_ticket_number']),
    'store_sales': ('store_sales_pkey', ['ss_item_sk', 'ss_ticket_number']),
    'time_dim': ('time_dim_pkey', ['t_time_sk']),
    'warehouse': ('warehouse_pkey', ['w_warehouse_sk']),
    'web_page': ('web_page_pkey', ['wp_web_page_sk']),
    'web_returns': ('web_returns_pkey', ['wr_item_sk', 'wr_order_number']),
    'web_sales': ('web_sales_pkey', ['ws_item_sk', 'ws_order_number']),
    'web_site': ('web_site_pkey', ['web_site_sk']),
}

bin_dir = os.getcwd()
bin_path = os.path.join(bin_dir, 'dsdgen')

data_path = bin_dir + "/out_" + str(scale) + "/"  # directory of data files
db_name = "dsb_" + str(scale)  # database name

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

# disable statement timeout and increase maintenance_work_mem
pg_util.execute(cursor, "SET statement_timeout = 0;", verbose=True)
pg_util.execute(cursor, "SET maintenance_work_mem = '2GB';", verbose=True)

# drop primary keys before loading
for table in tables:
    if table in primary_keys:
        pk_name = primary_keys[table][0]
        pg_util.execute(cursor, f'ALTER TABLE {table} DROP CONSTRAINT IF EXISTS {pk_name};', verbose=True)

# load data
for table in tables:
    file_path = os.path.join(data_path, table + '.dat')
    pg_util.execute(cursor, 'TRUNCATE ' + table + ';', verbose=True)
    t0 = time.time()
    pg_util.load_from_csv_file(cursor, file_path, table, delimiter='|')
    elapsed = time.time() - t0
    print(f'Loaded {table} in {elapsed:.1f}s')

# recreate primary keys for all 7 tables
for table, (pk_name, pk_cols) in primary_keys.items():
    cols = ', '.join(pk_cols)
    t0 = time.time()
    pg_util.execute(cursor, f'ALTER TABLE {table} ADD CONSTRAINT {pk_name} PRIMARY KEY ({cols});', verbose=True)
    elapsed = time.time() - t0
    print(f'Rebuilt {pk_name} in {elapsed:.1f}s')

# reset maintenance_work_mem to default
pg_util.execute(cursor, "RESET maintenance_work_mem;", verbose=True)

cursor.close()
conn.close()
