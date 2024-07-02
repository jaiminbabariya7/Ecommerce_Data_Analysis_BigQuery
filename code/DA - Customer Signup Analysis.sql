SELECT
  EXTRACT(YEAR FROM signup_date) AS signup_year,
  COUNT(customer_id) AS signup_count
FROM
  ecommerce_dataset.customers
GROUP BY
  signup_year
ORDER BY
  signup_year;
