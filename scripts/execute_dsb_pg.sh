#!/bin/bash

if [ -z "$1" ]; then
  echo "Please enter qs_Official, qs_QuerySplit, or wo_multi_block!"
  exit 1
fi

if [ -z "$2" ]; then
  echo "Please enter scale factor to choose the correct database!"
  exit 1
fi

dir_1="${PWD}/../code/tools/1_instance_out_$1/1/"
dir_2="${PWD}/../code/tools/1_instance_out_$1/2/"
iteration=1

log_name=pg_dsb_$1.txt

rm -f dsb_$2_result/*
mkdir -p dsb_$2_result/

for i in $(eval echo {1.."${iteration}"}); do
  for sql in $(find "$dir_1" "$dir_2" -type f -name "*.sql"); do
    echo "execute ${sql}" 2>&1|tee -a ${log_name};
    psql -U postgres -d dsb_$2 -f "${sql}" 2>&1|tee -a ${log_name};
  done
done

mv ${log_name} dsb_$2_result/.
