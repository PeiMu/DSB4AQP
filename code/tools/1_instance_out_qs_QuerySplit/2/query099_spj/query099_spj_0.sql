
switch to c_r;
switch to relationshipcenter;

SET parallel_leader_participation = off;
set max_parallel_workers = '0';
set max_parallel_workers_per_gather = '0';
set shared_buffers = '512MB';
set temp_buffers = '2047MB';
set work_mem = '2047MB';
set effective_cache_size = '4 GB';
set statement_timeout = '1000s';
set default_statistics_target = 100;


select min(w_warehouse_name) as min_w_warehouse_name
  ,min(sm_type) as min_sm_type
  ,min(cc_name) as min_cc_name
  ,min(cs_order_number) as min_cs_order_number
  ,min(cs_item_sk) as min_cs_item_sk
from
   catalog_sales
  ,warehouse
  ,ship_mode
  ,call_center
  ,date_dim
where
    d_month_seq between 1201 and 1201 + 23
and cs_ship_date_sk   = d_date_sk
and cs_warehouse_sk   = w_warehouse_sk
and cs_ship_mode_sk   = sm_ship_mode_sk
and cs_call_center_sk = cc_call_center_sk
and cs_list_price between 248 and 277
and sm_type = 'LIBRARY'
and cc_class = 'small'
and w_gmt_offset = -5
;


