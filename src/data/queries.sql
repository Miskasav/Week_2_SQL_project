-- SELECT * FROM public."Customers";

-- SELECT COUNT(*) AS "Total orders" FROM public."Orders"; -- Total number of orders

-- SELECT SUM(price_at_purchase * quantity) AS "Total sales" FROM public."Order_Items"; -- Total sales (sum of price_at_purchase * quantity from Order_Items)

-- SELECT COUNT(*) AS "Count of products with low stock" FROM public."Products" WHERE stock_quantity < 10; -- Count of products with low stock (e.g., stock_quantity < 10)

-- SELECT AVG(quantity * price_at_purchase) AS "Average order value", order_id FROM public."Order_Items" GROUP BY order_id ORDER BY "Average order value" DESC; -- Average order value

-- SELECT  SUM(quantity * price_at_purchase) AS "Total sales per category", category FROM public."Order_Items", public."Products" GROUP BY category;  -- Total sales per category

SELECT COUNT(OI.order_id) AS "Orders", SUM(price_at_purchase * quantity) AS "Total sales", DATE_TRUNC('month', order_date) AS "Order month" 
FROM public."Order_Items" AS OI, public."Orders" AS O 
GROUP BY order_date 
ORDER BY order_date; -- Monthly breakdown of the number of orders and total sales