SELECT	C.brand_name as Brand, D.category_name as Category, B.model_year as Model_Year,
		ROUND (SUM (A.quantity * A.list_price * (1 - A.discount)), 0) total_sales_price
INTO	sale.sales_summary
FROM	sale.order_item A, product.product B, product.brand C, product.category D
WHERE	A.product_id = B.product_id
AND		B.brand_id = C.brand_id
AND		B.category_id = D.category_id
GROUP BY
		C.brand_name, D.category_name, B.model_year

--jane Destroyun manageri olduðu calýþanlar
 
select * from sale.staff
where manager_id = (select staff_id from sale.staff
                    where first_name='Jane'  and  last_name= 'Destrey')

--sub query ile yaptýk

--holbrok þehrinde oturan müþterilerin sipariþ tarihlerini listeleyin

select * from sale.orders
where customer_id in (

					select customer_id from sale.customer --nerede arayacaðýný bilmelidir
					where city='Holbrook')

SELECT	customer_id, order_id, order_date
FROM	SALE.orders
WHERE	customer_id IN (
						SELECT	customer_id
						FROM	SALE.customer
						WHERE	city = 'Holbrook'
						)

select * from sale.orders
where first_name='Abby'

select * from sale.orders
where customer_id  in (select * from sale.customer
						where first_name='Abby' order by customer_id)

SELECT B.first_name, B.last_name, A.order_date
FROM sale.orders A INNER JOIN sale.customer B on A.customer_id=B.customer_id
 WHERE A.order_date IN  (SELECT order_date  FROM sale.orders
 WHERE customer_id IN (SELECT customer_id FROM sale.customer WHERE first_name = 'Abby' and last_name= 'Parks'))