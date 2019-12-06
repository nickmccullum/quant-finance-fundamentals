CREATE VIEW total_revenue_per_customer AS
SELECT customers.first_name, customers.last_name, SUM(items.price) FROM customers
INNER JOIN purchases ON customers.id = purchases.customers_id
INNER JOIN items ON purchases.item_id = items.id
GROUP BY customers.id;
