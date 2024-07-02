---
Title: "E-commerce Data Analysis Project using BigQuery"
Author: "Jaimin Babariya"
Date: "Tue 2 Jul 2024"
---

# E-commerce Data Analysis Project

## Overview

This project aims to analyze e-commerce sales data using Google BigQuery. The primary objectives include loading data into BigQuery, performing data analysis using SQL queries, and utilizing analytical functions to derive meaningful insights from the data.

## Project Structure

The project is structured into several key components:

1. **Data Loading**:
   - Create a BigQuery dataset and tables (`orders`, `customers`, `products`).
   - Load data into BigQuery from CSV files stored in Google Cloud Storage.

2. **Data Analysis**:
   - Perform various data analysis tasks using SQL queries:
     - Calculate total sales by product.
     - Analyze customer signup trends over time.
     - Rank products by sales performance.
     - Calculate running totals of daily sales.
     - Determine customer purchase frequency quartiles.

3. **Technologies Used**:
   - Google BigQuery for data storage and analysis.
   - Google Cloud Storage for storing CSV data files.
   - SQL for querying and analyzing data.
   - Python for generating fake CSV data files.

## Setup Instructions

### Prerequisites

Before running the project, ensure you have:

- A Google Cloud Platform account with BigQuery enabled.
- CSV files containing e-commerce data stored in Google Cloud Storage.

### Setup

1. **Create BigQuery Dataset and Tables**:
   - Create a new dataset named `ecommerce_data` in BigQuery.
   - Create tables `orders`, `customers`, and `products` within the `ecommerce_data` dataset.

2. **Load Data into BigQuery**:
   - Use the BigQuery web UI or `bq` command-line tool to load CSV files from Google Cloud Storage into respective tables (`orders`, `customers`, `products`).

### Running Queries

1. **Run SQL Queries**:
   - Copy SQL queries provided in the project README to BigQuery console or API.
   - Execute queries to perform data analysis tasks as outlined in the project overview.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

