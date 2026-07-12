#!/bin/bash

if [ -z "$1" ]; then
  echo "Please enter scale factor to choose the correct database!"
  exit 1
fi

rm -f ./dsb_$1.db

# compile vanillia duckdb
# cd ../ && make clean && GEN=ninja ENABLE_QUERY_SPLIT=0 VERBOSE=1 make

# create schema
echo "create dsb_$1 schema"
echo -ne ".read create_tables.sql" | duckdb ./dsb_$1.db

# load dsb_$1
for table in customer_address customer_demographics date_dim warehouse ship_mode time_dim reason income_band item store call_center customer web_site store_returns household_demographics web_page promotion catalog_page inventory catalog_returns web_returns web_sales catalog_sales store_sales 
do
  echo "duckdb load table from ${table}.tbl"
  command="copy ${table} from '${PWD}/../code/tools/out_$1/csv/${table}.csv' (quote '\"', escape '\\');"
  echo $command
  echo -ne "${command}" | duckdb ./dsb_$1.db
done

# execute queries with official duckdb to verify
dir_1="${PWD}/../code/tools/1_instance_out_wo_multi_block/1/"
dir_2="${PWD}/../code/tools/1_instance_out_wo_multi_block/2/"
iteration=1

rm -rf duckdb_dsb_$1_result/
mkdir -p duckdb_dsb_$1_result/

for i in $(eval echo {1.."${iteration}"}); do
  for sql in $(find "$dir_1" "$dir_2" -type f -name "*.sql"); do
    echo "execute ${sql}" 2>&1|tee -a duckdb_dsb_$1.txt;
    echo -ne ".read ${sql}" | duckdb ./dsb_$1.db 2>&1|tee -a duckdb_dsb_$1.txt;
  done
done

mv duckdb_dsb_$1.txt duckdb_dsb_$1_result/.

