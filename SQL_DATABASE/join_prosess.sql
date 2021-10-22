

select TOP 10* from product.product A inner join product.category B on A.category_id=B.category_id
  

select Top 10* from sale.staff A
select Top 10* from sale.store B

select first_name,last_name,store_name from sale.staff A inner join sale.store B on A.store_id=B.store_id 

select  A.product_id,A.product_name,B.order_id 
from product.product A left join sale.order_item B 
on A.product_id = B.product_id
where order_id is null  

select A.product_id as product_id,A.product_name as product_name ,B.store_id,B.product_id 
from product.product A left join product.stock B on A.product_id=B.product_id
where A.product_id >310
order by A.product_id desc

select *--count(distinct B.staff_id)
from sale.staff B  
full outer join sale.orders A on A.staff_id=B.staff_id
order by A.order_id,B.manager_id

select count(staff_id) from sale.staff


select * from sale.staff A
LEFT JOIN sale.orders B on A.staff_id=B.staff_id left join sale.store C on C.store_id=B.store_id 


SELECT	C.brand_name as Brand, D.category_name as Category, B.model_year as Model_Year,
		ROUND (SUM (A.quantity * A.list_price * (1 - A.discount)), 0) total_sales_price
INTO	sale.sales_summary
FROM	sale.order_item A, product.product B, product.brand C, product.category D
WHERE	A.product_id = B.product_id
AND		B.brand_id = C.brand_id
AND		B.category_id = D.category_id
GROUP BY
		C.brand_name, D.category_name, B.model_year