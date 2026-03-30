
select min(i_item_id) as min_i_item_id,
        min(ca_country) as min_ca_country,
        min(ca_state) as min_ca_state,
        min(ca_county) as min_ca_county,
        min(cs_quantity) as min_cs_quantity,
        min(cs_list_price) as min_cs_list_price,
        min(cs_coupon_amt) as min_cs_coupon_amt,
        min(cs_sales_price) as min_cs_sales_price,
        min(cs_net_profit) as min_cs_net_profit,
        min(c_birth_year) as min_c_birth_year,
        min(cd_dep_count) as min_cd_dep_count
 from catalog_sales, customer_demographics, customer, customer_address, date_dim, item
 where cs_sold_date_sk = d_date_sk and
       cs_item_sk = i_item_sk and
       cs_bill_cdemo_sk = cd_demo_sk and
       cs_bill_customer_sk = c_customer_sk and
       cd_gender = 'F' and
       cd_education_status = '2 yr Degree' and
       c_current_addr_sk = ca_address_sk and
       d_year = 2000 and
       c_birth_month = 3 and
       ca_state in ('GA', 'ME', 'NC')
       and cs_wholesale_cost BETWEEN 84 AND 89
       AND i_category = 'Books'
;


