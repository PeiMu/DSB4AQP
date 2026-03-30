
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


select min(i_brand_id) as min_i_brand_id, min(i_manufact_id) as min_i_manufact_id,
 	min(ss_ext_sales_price) as min_ss_ext_sales_price
 from date_dim, store_sales, item,customer,customer_address,store
 where d_date_sk = ss_sold_date_sk
   and ss_item_sk = i_item_sk
   and ss_customer_sk = c_customer_sk
   and c_current_addr_sk = ca_address_sk
   and ss_store_sk = s_store_sk
   AND i_category  = 'Books'
   and d_year=2001
   and d_moy = 2
   and substring(ca_zip,1,5) <> substring(s_zip,1,5)
   and ca_state  = 'IL'
   and c_birth_month = 9
   and ss_wholesale_cost BETWEEN 73 AND 93
 ;


