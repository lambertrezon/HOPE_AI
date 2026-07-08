CREATE DATABASE SET2CODING;
USE SET2CODING;

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    salary INT,
    department_id INT
);

-- Create Departments Table
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

-- Create Sales Table
CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    customer_id INT,
    amount DECIMAL(10,2),
    sale_date DATE
);

-- Create Products Table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    price INT
);

-- Create Orders Table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    order_date DATE,
    order_amount INT
);

INSERT INTO employees (employee_id, name, age, salary, department_id) VALUES
(1, 'John', 30, 60000, 101),
(2, 'Emily', 25, 48000, 102),
(3, 'Michael', 40, 75000, 103),
(4, 'Sara', 35, 56000, 101),
(5, 'David', 28, 49000, 102),
(6, 'Robert', 45, 90000, 103),
(7, 'Sophia', 29, 51000, 102);

INSERT INTO departments (department_id, department_name) VALUES
(101, 'HR'),
(102, 'Finance'),
(103, 'IT');

INSERT INTO sales (sale_id, product_id, customer_id, amount, sale_date) VALUES
(1, 1, 101, 4500.00, '2023-03-01'),
(2, 2, 102, 5500.00, '2023-03-02'),
(3, 3, 103, 7000.00, '2023-04-01'),
(4, 1, 104, 3000.00, '2023-04-02'),
(5, 2, 105, 6000.00, '2023-05-01');

INSERT INTO products (product_id, product_name, price) VALUES
(1, 'Laptop', 1000),
(2, 'Mobile', 500),
(3, 'Tablet', 300),
(4, 'Headphones', 100),
(5, 'Smartwatch', 200);

INSERT INTO orders (order_id, customer_name, order_date, order_amount) VALUES
(1, 'John', '2023-05-01', 500),
(2, 'Emily', '2023-05-02', 700),
(3, 'Michael', '2023-05-03', 1200),
(4, 'Sara', '2023-05-04', 450),
(5, 'David', '2023-05-05', 900),
(6, 'John', '2023-05-06', 600),
(7, 'Emily', '2023-05-07', 750);

-- Question 1: Find Employees with Highest Salary Per Department
SELECT a.department_id, b.department_name,max(a.salary)as high_sal
FROM employees a
JOIN  departments b
ON a.department_id = b.department_id
GROUP BY a.department_id;

-- Question 2: Calculate Monthly Sales Growth Percentage
-- Calculate the month-over-month sales growth percentage for each product using the sales table.
SELECT a.product_id, b.product_name,  IFNULL(((a.amount - c.amount) / c.amount * 100), 0) AS sales_growth_percentage
FROM sales a
JOIN products b
ON a.product_id = b.product_id
LEFT JOIN sales c
ON b.product_id = c.product_id 
AND MONTH(a.sale_date) = MONTH(c.sale_date) + 1;

-- Question 3: Identify Departments with Average Salary Greater Than Company Average
-- List department names where the average salary is greater than the company's average salary.
SELECT b.department_name,AVG(a.salary) as avg_sal
FROM employees a
JOIN departments b
ON a.department_id = b.department_id
GROUP BY b.department_id
HAVING avg_sal>(SELECT AVG(salary) FROM employees);

-- Question 4: Find Customers with Consecutive Purchases
-- Identify customers who made purchases on two or more consecutive days.
SELECT b.customer_name
FROM orders a
JOIN orders b ON a.customer_name = b.customer_name 
AND DATEDIFF(a.order_date, b.order_date) = 1;

-- Question 5: Detect Overlapping Orders
-- Find orders where two or more customers placed orders within the same hour, based on order_date and time.
SELECT a.order_id, a.customer_name
FROM orders a
JOIN orders b ON a.customer_name != b.customer_name 
AND ABS(TIMESTAMPDIFF(MINUTE, a.order_date, b.order_date)) <= 60;
