CREATE VIEW non_luxury_items AS 
SELECT * FROM expensive_items WHERE price < 10000
WITH LOCAL CHECK OPTION;
