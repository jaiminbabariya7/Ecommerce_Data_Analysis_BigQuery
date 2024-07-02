SELECT
  order_date,
  SUM(quantity * price) AS daily_sales,
  ROW_NUMBER() OVER (ORDER BY order_date) AS row_num
FROM
  ecommerce_dataset.orders
GROUP BY
  order_date
ORDER BY
  order_date;
