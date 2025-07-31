

CREATE TABLE products (
    id INT PRIMARY KEY,
    cost DECIMAL(10,2),
    category VARCHAR(255),
    name VARCHAR(255),
    brand VARCHAR(255),
    retail_price DECIMAL(10,2),
    department VARCHAR(255),
    sku VARCHAR(255),
    
    distribution_center_id INT
);
DESCRIBE products;

SELECT * FROM products LIMIT 10;

-- Count of products
SELECT COUNT(*) FROM products;

-- Distinct categories
SELECT DISTINCT category FROM products;

-- Top 5 most expensive products
SELECT name, retail_price FROM products ORDER BY retail_price DESC LIMIT 5;


