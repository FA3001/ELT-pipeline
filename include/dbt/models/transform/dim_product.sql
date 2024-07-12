-- Create the dimension table
SELECT DISTINCT
    {{ dbt_utils.generate_surrogate_key(['stockcode', 'description', 'price']) }} as product_id,
    stockcode AS stock_code,
    description AS description,
    price AS price
FROM sales
WHERE stockcode IS NOT NULL
AND price > 0