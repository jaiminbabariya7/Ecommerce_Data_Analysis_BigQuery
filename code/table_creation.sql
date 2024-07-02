CREATE TABLE ecommerce_dataset.orders (
  order_id STRING,
  customer_id STRING,
  product_id STRING,
  order_date DATE,
  quantity INT64,
  price NUMERIC
);

CREATE TABLE ecommerce_dataset.customers (
  customer_id STRING,
  customer_name STRING,
  customer_email STRING,
  signup_date DATE
);

CREATE TABLE ecommerce_dataset.products (
  product_id STRING,
  product_name STRING,
  category STRING,
  quantity INT64,
  price NUMERIC
);