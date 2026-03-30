
SET parallel_leader_participation = off;
set max_parallel_workers = '0';
set max_parallel_workers_per_gather = '0';
set shared_buffers = '512MB';
set temp_buffers = '2047MB';
set work_mem = '2047MB';
set effective_cache_size = '4 GB';
set statement_timeout = '1000s';
set default_statistics_target = 100;


select
   min(w_state) as min_w_state
  ,min(i_item_id) as min_i_item_id
  ,min(cs_item_sk) as min_cs_item_sk
  ,min(cs_order_number) as min_cs_order_number
  ,min(cr_item_sk) as min_cr_item_sk
  ,min(cr_order_number) as min_cr_order_number
 from
   catalog_sales left outer join catalog_returns on
       (cs_order_number = cr_order_number
        and cs_item_sk = cr_item_sk)
  ,warehouse
  ,item
  ,date_dim
 where
 i_item_sk          = cs_item_sk
 and cs_warehouse_sk    = w_warehouse_sk
 and cs_sold_date_sk    = d_date_sk
 and d_date between (cast ('2001-05-21' as date) - interval '30 day')
                and (cast ('2001-05-21' as date) + interval '30 day') 
 and i_category  = 'Books'
 and i_manager_id between 61 and 100
 and cs_wholesale_cost between 81 and 100
 and cr_reason_sk = 5
;


