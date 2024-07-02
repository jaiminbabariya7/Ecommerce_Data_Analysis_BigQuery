WITH customer_purchase_counts AS (
  SELECT
    customer_id,
    COUNT(order_id) AS purchase_count
  FROM
    ecommerce_dataset.orders
  GROUP BY
    customer_id
)

SELECT
  customer_id,
  purchase_count,
  NTILE(4) OVER (ORDER BY purchase_count DESC) AS purchase_quartile
FROM
  customer_purchase_counts
ORDER BY
  purchase_quartile, purchase_count DESC;
