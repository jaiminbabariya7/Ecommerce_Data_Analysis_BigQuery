SELECT
  p.product_id,
  p.product_name,
  SUM(o.quantity * o.price) AS total_sales
FROM
  ecommerce_dataset.orders o
JOIN
  ecommerce_dataset.products p
ON
  o.product_id = p.product_id
GROUP BY
  p.product_id, p.product_name
ORDER BY
  total_sales DESC;
