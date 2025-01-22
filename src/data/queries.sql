-- Joins and Multi-table Queries
drop view if exists joins_orders;

create view joins_orders as
select ord.*, sum(oi.quantity * oi.price_at_purchase) as total
from (
    select o.order_id, o.order_date, o.order_status, o.customer_id, c.name
    from public."Orders" o
    join public."Customers" c
    on o.customer_id = c.customer_id
) ord
join public."Order_Items" oi
on ord.order_id = oi.order_id
group by ord.order_id, ord.order_date, ord.order_status, ord.customer_id, ord.name;

select jo.name as "Top customers", round(jo.total, 2) as "Total spent"
from joins_orders jo
ORDER BY jo.total DESC
LIMIT 5;

drop view if exists joins_suppliers;

create view joins_suppliers as
select s.supplier_id as "Supplier ID", s.name as "Supplier name", count(p) as "Number of products"
from public."Products" p
join public."Suppliers" s
on s.supplier_id = p.supplier_id
group by s.supplier_id
order by "Number of products" desc;


