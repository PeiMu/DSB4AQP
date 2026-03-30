-- DSB indexes for MariaDB.
-- Adapted from dsb_index_pg.sql: INCLUDE clauses removed (not supported in MariaDB),
-- index names > 64 characters shortened, duplicate key-column indexes removed.

-- store_sales
-- renamed: original name was 87 chars (exceeded MariaDB 64-char limit)
create index idx_ss_date_profit_price_hdemo_store_cdemo_addr on store_sales
(
    ss_sold_date_sk asc,
    ss_net_profit asc,
    ss_sales_price asc,
    ss_hdemo_sk asc,
    ss_store_sk asc,
    ss_cdemo_sk asc,
    ss_addr_sk asc
);
create index _dta_index_store_sales_6_1333579789__k1_k5_k8_k3 on store_sales
(
    ss_sold_date_sk asc,
    ss_cdemo_sk asc,
    ss_store_sk asc,
    ss_item_sk asc
);
create index _dta_index_store_sales_6_1333579789__k1_k3_k10_k4_k8 on store_sales
(
    ss_sold_date_sk asc,
    ss_item_sk asc,
    ss_ticket_number asc,
    ss_customer_sk asc,
    ss_store_sk asc
);
create index _dta_index_store_sales_6_1333579789__k4 on store_sales
(
    ss_customer_sk asc
);
create index _dta_index_store_sales_6_1333579789__k1_k8 on store_sales
(
    ss_sold_date_sk asc,
    ss_store_sk asc
);
create index _dta_index_store_sales_6_1333579789__k3_k10_k4_k1_k8 on store_sales
(
    ss_item_sk asc,
    ss_ticket_number asc,
    ss_customer_sk asc,
    ss_sold_date_sk asc,
    ss_store_sk asc
);
create index _dta_index_store_sales_6_1333579789__k1_k3_k7 on store_sales
(
    ss_sold_date_sk asc,
    ss_item_sk asc,
    ss_addr_sk asc
);
create index _dta_index_store_sales_6_1333579789__k1_k7_k3 on store_sales
(
    ss_sold_date_sk asc,
    ss_addr_sk asc,
    ss_item_sk asc
);
create index _dta_index_store_sales_6_1333579789__k1_k3 on store_sales
(
    ss_sold_date_sk asc,
    ss_item_sk asc
);
create index _dta_index_store_sales_6_1333579789__k1_k4_k3_k10 on store_sales
(
    ss_sold_date_sk asc,
    ss_customer_sk asc,
    ss_item_sk asc,
    ss_ticket_number asc
);
create index _dta_index_store_sales_6_1333579789__k4_k1 on store_sales
(
    ss_customer_sk asc,
    ss_sold_date_sk asc
);
create index _dta_index_store_sales_6_1333579789__k3_k10_k4 on store_sales
(
    ss_item_sk asc,
    ss_ticket_number asc,
    ss_customer_sk asc
);
create index _dta_index_store_sales_6_1333579789__k10_k3 on store_sales
(
    ss_ticket_number asc,
    ss_item_sk asc
);

-- catalog_sales
-- renamed: original name was 74 chars
create index idx_cs_date_item_cdemo_cust on catalog_sales
(
    cs_sold_date_sk asc,
    cs_item_sk asc,
    cs_bill_cdemo_sk asc,
    cs_bill_customer_sk asc
);
-- renamed: original name was 73 chars
create index idx_cs_promo_hdemo_shipdate_cdemo_date_item on catalog_sales
(
    cs_promo_sk asc,
    cs_bill_hdemo_sk asc,
    cs_ship_date_sk asc,
    cs_bill_cdemo_sk asc,
    cs_sold_date_sk asc,
    cs_item_sk asc
);
create index _dta_index_catalog_sales_6_1301579675__k1_4_16 on catalog_sales
(
    cs_sold_date_sk asc
);
create index _dta_index_catalog_sales_6_1301579675__k3_k12_k14_k15 on catalog_sales
(
    cs_ship_date_sk asc,
    cs_call_center_sk asc,
    cs_ship_mode_sk asc,
    cs_warehouse_sk asc
);
create index _dta_index_catalog_sales_6_1301579675__k1_k16_k4 on catalog_sales
(
    cs_sold_date_sk asc,
    cs_item_sk asc,
    cs_bill_customer_sk asc
);
create index _dta_index_catalog_sales_6_1301579675__k3_1_12 on catalog_sales
(
    cs_ship_date_sk asc
);
create index _dta_index_catalog_sales_6_1301579675__k16_k4_k1 on catalog_sales
(
    cs_item_sk asc,
    cs_bill_customer_sk asc,
    cs_sold_date_sk asc
);
create index _dta_index_catalog_sales_6_1301579675__k16_k18 on catalog_sales
(
    cs_item_sk asc,
    cs_order_number asc
);
create index _dta_index_catalog_sales_6_1301579675__k1_k4 on catalog_sales
(
    cs_sold_date_sk asc,
    cs_bill_customer_sk asc
);

-- web_sales
create index _dta_index_web_sales_6_1269579561__k3_k18_k12_k14 on web_sales
(
    ws_ship_date_sk asc,
    ws_order_number asc,
    ws_ship_addr_sk asc,
    ws_web_site_sk asc
);
create index _dta_index_web_sales_6_1269579561__k1_k4_k5_18 on web_sales
(
    ws_sold_date_sk asc,
    ws_item_sk asc,
    ws_bill_customer_sk asc
);
create index _dta_index_web_sales_6_1269579561__k1 on web_sales
(
    ws_sold_date_sk asc
);
create index _dta_index_web_sales_6_1269579561__k18 on web_sales
(
    ws_order_number asc
);
create index _dta_index_web_sales_6_1269579561__k1_k5 on web_sales
(
    ws_sold_date_sk asc,
    ws_bill_customer_sk asc
);

-- store_returns
create index _dta_index_store_returns_6_1013578649__k1 on store_returns
(
    sr_returned_date_sk asc
);
create index _dta_index_store_returns_6_1013578649__k5 on store_returns
(
    sr_cdemo_sk asc
);

-- customer
create index _dta_index_customer_6_949578421__k9_k10 on customer
(
    c_first_name asc,
    c_last_name asc
);
create index _dta_index_customer_6_949578421__k1_k5 on customer
(
    c_customer_sk asc,
    c_current_addr_sk asc
);

-- item
create index _dta_index_item_6_853578079__k1 on item
(
    i_item_sk asc
);
create index _dta_index_item_6_853578079__k13_k11_k1 on item
(
    i_category asc,
    i_class asc,
    i_item_sk asc
);
create index _dta_index_item_6_853578079__k18 on item
(
    i_color asc
);
create index _dta_index_item_6_853578079__k2_k1 on item
(
    i_item_id asc,
    i_item_sk asc
);

-- date_dim
create index _dta_index_date_dim_6_661577395__k7_k4_k9_k1 on date_dim
(
    d_year asc,
    d_month_seq asc,
    d_moy asc,
    d_date_sk asc
);
create index _dta_index_date_dim_6_661577395__k7_k9_k1 on date_dim
(
    d_year asc,
    d_moy asc,
    d_date_sk asc
);
create index _dta_index_date_dim_6_661577395__k1_k7_k9 on date_dim
(
    d_date_sk asc,
    d_year asc,
    d_moy asc
);
create index _dta_index_date_dim_6_661577395__k7_k11_k1 on date_dim
(
    d_year asc,
    d_qoy asc,
    d_date_sk asc
);
create index _dta_index_date_dim_6_661577395__k9_k7_k1 on date_dim
(
    d_moy asc,
    d_year asc,
    d_date_sk asc
);
create index _dta_index_date_dim_6_661577395__k4 on date_dim
(
    d_month_seq asc
);
create index _dta_index_date_dim_6_661577395__k7_k1 on date_dim
(
    d_year asc,
    d_date_sk asc
);
create index _dta_index_date_dim_6_661577395__k7_k9 on date_dim
(
    d_year asc,
    d_moy asc
);
create index _dta_index_date_dim_6_661577395__k4_k3 on date_dim
(
    d_month_seq asc,
    d_date asc
);

-- store
create index _dta_index_store_6_885578193__k1 on store
(
    s_store_sk asc
);
create index _dta_index_store_6_885578193__k25_k1 on store
(
    s_state asc,
    s_store_sk asc
);

-- indexes for q19
create index _dta_index_store_sales_5_1333579789__k4_k8_k3_k1 on store_sales
(
    ss_customer_sk asc,
    ss_store_sk asc,
    ss_item_sk asc,
    ss_sold_date_sk asc
);
create index _dta_index_customer_5_949578421__k13_k5 on customer
(
    c_birth_month asc,
    c_current_addr_sk asc
);
