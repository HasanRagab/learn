# Full SQL Guide (MySQL Focused)

## 📌 Introduction

SQL (Structured Query Language) is used to manage data in relational databases. MySQL is an open-source RDBMS known for its speed and ease of use.

---

## 🧱 MySQL Data Types

### Numeric Types

* `TINYINT`, `SMALLINT`, `MEDIUMINT`, `INT`/`INTEGER`, `BIGINT`
* `DECIMAL(p, s)`, `NUMERIC(p, s)` — exact
* `FLOAT(p)`, `DOUBLE` — approximate

### String Types

* `CHAR(n)`: Fixed-length
* `VARCHAR(n)`: Variable-length
* `TEXT`, `TINYTEXT`, `MEDIUMTEXT`, `LONGTEXT`
* `ENUM('val1', 'val2', ...)`
* `SET('a', 'b', 'c')`

### Date & Time Types

* `DATE`, `TIME`, `DATETIME`, `TIMESTAMP`, `YEAR`

---

## 📂 Database Commands

```sql
SHOW DATABASES;
CREATE DATABASE mydb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE mydb;
DROP DATABASE mydb;
SHOW TABLES;
DESCRIBE tablename;
```

---

## 📋 Table Commands

```sql
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) NOT NULL UNIQUE,
  email VARCHAR(100),
  age INT CHECK (age >= 0),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE users ADD COLUMN status ENUM('active', 'inactive') DEFAULT 'active';
ALTER TABLE users MODIFY age TINYINT UNSIGNED;
ALTER TABLE users DROP COLUMN status;
DROP TABLE users;
```

---

## 🚀 CRUD Operations

### INSERT

```sql
INSERT INTO users (username, email, age) VALUES ('Alice', 'alice@example.com', 30);
INSERT INTO users SET username='Bob', email='bob@example.com';
```

### SELECT

```sql
SELECT * FROM users;
SELECT username, age FROM users WHERE age > 20 ORDER BY age DESC;
SELECT COUNT(*) FROM users WHERE email IS NOT NULL;
```

### UPDATE & DELETE

```sql
UPDATE users SET age = age + 1 WHERE id = 1;
DELETE FROM users WHERE id = 10;
```

---

## 🔍 Filtering & Conditions

* `=`, `!=`, `<>`, `<`, `>`, `<=`, `>=`
* `IN`, `NOT IN`, `BETWEEN`, `LIKE`, `IS NULL`, `IS NOT NULL`
* `AND`, `OR`, `NOT`

```sql
SELECT * FROM users WHERE age BETWEEN 18 AND 30 AND email LIKE '%@gmail.com';
```

---

## 🔗 Joins in MySQL

```sql
SELECT u.username, o.total
FROM users u
JOIN orders o ON u.id = o.user_id;

SELECT u.username, o.total
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

SELECT u.username, o.total
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;

-- Simulating FULL OUTER JOIN using UNION
SELECT u.id, u.username, o.total
FROM users u LEFT JOIN orders o ON u.id = o.user_id
UNION
SELECT u.id, u.username, o.total
FROM users u RIGHT JOIN orders o ON u.id = o.user_id;
```

---

## 📊 Aggregate Functions

```sql
SELECT COUNT(*), AVG(age), MAX(age), MIN(age), SUM(age) FROM users;
SELECT age, COUNT(*) FROM users GROUP BY age HAVING COUNT(*) > 1;
```

---

## 🧩 Subqueries & Derived Tables

```sql
SELECT username FROM users WHERE id IN (SELECT user_id FROM orders WHERE total > 100);

SELECT u.username, order_stats.total
FROM users u
JOIN (SELECT user_id, SUM(total) AS total FROM orders GROUP BY user_id) AS order_stats
ON u.id = order_stats.user_id;
```

---

## 🛠 Indexes

```sql
CREATE INDEX idx_email ON users(email);
DROP INDEX idx_email ON users;
SHOW INDEX FROM users;
```

---

## 👁 Views

```sql
CREATE VIEW active_users AS SELECT * FROM users WHERE status = 'active';
DROP VIEW active_users;
```

---

## 🔐 Constraints

* `PRIMARY KEY`, `UNIQUE`, `NOT NULL`, `DEFAULT`, `AUTO_INCREMENT`
* `FOREIGN KEY (col) REFERENCES other_table(col)`

```sql
CREATE TABLE orders (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT,
  total DECIMAL(10, 2),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

---

## 🔄 Transactions

```sql
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;

-- To cancel changes:
ROLLBACK;
```

---

## 🧠 Stored Procedures (MySQL)

```sql
DELIMITER //
CREATE PROCEDURE GetAdults()
BEGIN
  SELECT * FROM users WHERE age >= 18;
END;
//
DELIMITER ;

CALL GetAdults();
```

---

## 🔔 Triggers

```sql
DELIMITER //
CREATE TRIGGER set_created_at BEFORE INSERT ON users
FOR EACH ROW BEGIN
  SET NEW.created_at = NOW();
END;
//
DELIMITER ;
```

---

## 🧬 Migrations

* **What Are Migrations?** Migrations are version-controlled changes to the database schema.
* **Why Use Them?** They allow safe, consistent schema updates across environments.

### Manual Example

```sql
-- Migration: Add phone_number to users
ALTER TABLE users ADD COLUMN phone_number VARCHAR(15);

-- Rollback
ALTER TABLE users DROP COLUMN phone_number;
```

### Tools for Migrations

* **MySQL Workbench** — provides GUI for schema changes
* **Liquibase** — XML/SQL-based migration versioning
* **Flyway** — Java-based tool for version-controlled migrations
* **Prisma**, **TypeORM**, **Alembic** — migration tools for app frameworks

---

## 📦 Import/Export

```bash
# Export SQL dump
mysqldump -u root -p mydb > mydb.sql

# Import SQL dump
mysql -u root -p mydb < mydb.sql

# Export to CSV
mysql -u root -p -e "SELECT * FROM users INTO OUTFILE '/tmp/users.csv' FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';" mydb

# Import from CSV (ensure secure-file-priv allows it)
LOAD DATA INFILE '/tmp/users.csv' INTO TABLE users FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';

# Export to JSON (via MySQL Shell)
mysqlsh --uri root@localhost --sql -e "SELECT * FROM users" --result-format=json > users.json
```

---

## 🧰 MySQL Admin Tips

```sql
SHOW PROCESSLIST;
SHOW VARIABLES LIKE 'max_connections';
SHOW STATUS LIKE 'Threads%';
```

```bash
# Start MySQL Server
sudo systemctl start mysql

# Secure MySQL Installation
sudo mysql_secure_installation
```

---

## 🔐 MySQL User & Access Management

```sql
-- Create user
CREATE USER 'hasan'@'localhost' IDENTIFIED BY 'securepassword';

-- Grant privileges
GRANT ALL PRIVILEGES ON mydb.* TO 'hasan'@'localhost';
FLUSH PRIVILEGES;

-- Show users
SELECT user, host FROM mysql.user;

-- Change password
ALTER USER 'hasan'@'localhost' IDENTIFIED BY 'newpassword';

-- Revoke access
REVOKE ALL PRIVILEGES ON mydb.* FROM 'hasan'@'localhost';
DROP USER 'hasan'@'localhost';

-- View user privileges
SHOW GRANTS FOR 'hasan'@'localhost';

-- Create user with specific permissions
GRANT SELECT, INSERT, UPDATE ON mydb.* TO 'readonly_user'@'localhost' IDENTIFIED BY 'readonlypass';

-- Set password policy (MySQL 5.7+)
SHOW VARIABLES LIKE 'validate_password%';
```

---

## 🔄 Common Table Expressions (CTEs)

CTEs provide a way to write more readable and maintainable complex queries by creating named temporary result sets that exist only during query execution.

```sql
-- Basic CTE syntax
WITH employee_salaries AS (
  SELECT department_id, AVG(salary) AS avg_salary
  FROM employees
  GROUP BY department_id
)
SELECT d.name, es.avg_salary
FROM departments d
JOIN employee_salaries es ON d.id = es.department_id;

-- Multiple CTEs
WITH 
  top_customers AS (
    SELECT customer_id, SUM(total) AS total_spent
    FROM orders
    GROUP BY customer_id
    ORDER BY total_spent DESC
    LIMIT 10
  ),
  customer_details AS (
    SELECT id, name, email 
    FROM customers
    WHERE status = 'active'
  )
SELECT cd.name, cd.email, tc.total_spent
FROM top_customers tc
JOIN customer_details cd ON tc.customer_id = cd.id;

-- Recursive CTEs
WITH RECURSIVE subordinates AS (
  -- Anchor member
  SELECT id, name, manager_id
  FROM employees
  WHERE id = 1
  
  UNION ALL
  
  -- Recursive member
  SELECT e.id, e.name, e.manager_id
  FROM employees e
  JOIN subordinates s ON e.manager_id = s.id
)
SELECT * FROM subordinates;
```

---

## 📊 Window Functions

Window functions perform calculations across rows related to the current row, providing advanced analytics capabilities without requiring GROUP BY aggregation.

```sql
-- Basic window function syntax
SELECT 
  username,
  department,
  salary,
  AVG(salary) OVER() AS company_avg,
  AVG(salary) OVER(PARTITION BY department) AS dept_avg,
  salary - AVG(salary) OVER(PARTITION BY department) AS diff_from_dept_avg
FROM employees;

-- Ranking functions
SELECT 
  product_name,
  category,
  price,
  RANK() OVER(PARTITION BY category ORDER BY price DESC) AS price_rank,
  DENSE_RANK() OVER(PARTITION BY category ORDER BY price DESC) AS dense_price_rank,
  ROW_NUMBER() OVER(PARTITION BY category ORDER BY price DESC) AS row_num
FROM products;

-- Row navigation functions
SELECT 
  order_id,
  order_date,
  total,
  LAG(total, 1, 0) OVER(PARTITION BY customer_id ORDER BY order_date) AS previous_order_total,
  LEAD(total, 1, 0) OVER(PARTITION BY customer_id ORDER BY order_date) AS next_order_total
FROM orders;

-- Running totals and moving averages
SELECT 
  order_date,
  total,
  SUM(total) OVER(ORDER BY order_date) AS running_total,
  AVG(total) OVER(ORDER BY order_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_avg_3days
FROM orders;

-- First_value and last_value
SELECT 
  department,
  employee_name,
  salary,
  FIRST_VALUE(employee_name) OVER(PARTITION BY department ORDER BY salary DESC) AS highest_paid_in_dept
FROM employees;
```

---

## 🧩 JSON Support

MySQL 5.7+ provides robust JSON support with specialized functions for storing, validating, and manipulating JSON data.

```sql
-- Creating tables with JSON columns
CREATE TABLE users_profile (
  id INT PRIMARY KEY,
  user_id INT,
  profile JSON,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Inserting JSON data
INSERT INTO users_profile (id, user_id, profile) VALUES 
(1, 101, '{"name": "Alice", "skills": ["SQL", "Python"], "address": {"city": "Seattle", "state": "WA"}}');

-- Extracting JSON values
SELECT 
  id, 
  JSON_EXTRACT(profile, '$.name') AS name,
  JSON_EXTRACT(profile, '$.skills[0]') AS primary_skill,
  JSON_EXTRACT(profile, '$.address.city') AS city
FROM users_profile;

-- Using the -> operator (shorthand for JSON_EXTRACT)
SELECT 
  id,
  profile->'$.name' AS name,
  profile->'$.address.city' AS city
FROM users_profile;

-- Using the ->> operator (unwraps the value from quotes)
SELECT 
  id,
  profile->>'$.name' AS name
FROM users_profile;

-- Modifying JSON data
UPDATE users_profile 
SET profile = JSON_SET(profile, 
  '$.age', 30, 
  '$.skills[2]', 'JavaScript'
)
WHERE id = 1;

-- Adding to JSON arrays
UPDATE users_profile
SET profile = JSON_ARRAY_APPEND(profile, '$.skills', 'Docker')
WHERE id = 1;

-- Removing from JSON
UPDATE users_profile
SET profile = JSON_REMOVE(profile, '$.address.state')
WHERE id = 1;

-- Searching within JSON data
SELECT * FROM users_profile
WHERE JSON_CONTAINS(profile->'$.skills', '"Python"');

-- Indexing JSON data (for better performance)
ALTER TABLE users_profile ADD COLUMN name VARCHAR(100) 
  GENERATED ALWAYS AS (profile->>'$.name') STORED;
  
CREATE INDEX idx_name ON users_profile(name);
```

---

## 🚀 Performance Optimization

Optimizing MySQL queries and database structure can dramatically improve application performance.

### EXPLAIN and Query Analysis

```sql
-- Basic EXPLAIN
EXPLAIN SELECT * FROM users WHERE email = 'user@example.com';

-- EXPLAIN FORMAT=JSON for more details
EXPLAIN FORMAT=JSON SELECT 
  u.username, 
  COUNT(o.id) AS order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id;

-- EXPLAIN ANALYZE to see actual execution times
EXPLAIN ANALYZE SELECT * FROM large_table WHERE non_indexed_column = 'value';
```

### Index Optimization

```sql
-- Creating the right indexes
CREATE INDEX idx_email ON users(email);

-- Compound indexes (order matters!)
CREATE INDEX idx_lastname_firstname ON customers(last_name, first_name);

-- Index for sorting
CREATE INDEX idx_created_at ON orders(created_at DESC);

-- Covering indexes
CREATE INDEX idx_username_email ON users(username, email);

-- Prefix indexes for long text fields
CREATE INDEX idx_title ON articles(title(50));

-- Finding unused indexes
SELECT * FROM sys.schema_unused_indexes;

-- Checking index usage
SELECT * FROM sys.schema_index_statistics ORDER BY rows_selected DESC;

-- Check for missing indexes
SELECT * FROM sys.statements_with_full_table_scans LIMIT 10;
```

### Query Optimization Techniques

```sql
-- Use specific columns instead of *
SELECT id, username FROM users; -- Better than SELECT * FROM users

-- Limit results when possible
SELECT * FROM large_table LIMIT 1000;

-- Join optimization
SELECT u.username, o.order_id 
FROM users u 
JOIN orders o ON u.id = o.user_id
WHERE u.status = 'active'; -- Filter the smaller table first

-- EXISTS vs IN (EXISTS often better for large tables)
SELECT * FROM customers c
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id);

-- UNION ALL instead of UNION when duplicates are acceptable
SELECT product_id FROM recent_products
UNION ALL 
SELECT product_id FROM featured_products;
```

### Database Configuration Optimization

```sql
-- Check current settings
SHOW VARIABLES LIKE 'innodb_buffer_pool_size';
SHOW VARIABLES LIKE 'max_connections';

-- Optimal settings depend on your hardware and workload
-- Example values below should be adjusted for your environment

-- Edit my.cnf or my.ini file
[mysqld]
# Memory usage
innodb_buffer_pool_size = 4G         # 50-80% of available RAM
innodb_log_file_size = 512M          # Larger for write-heavy workloads

# Query cache (consider disabling in MySQL 8.0+)
query_cache_type = 0                 # OFF in 8.0+
query_cache_size = 0                 # OFF in 8.0+

# Connection handling
max_connections = 200                # Depends on application needs
thread_cache_size = 16               # For busy servers

# Temporary tables
tmp_table_size = 64M
max_heap_table_size = 64M
```

---

## 🔍 MySQL 8.0 Specific Features

MySQL 8.0 introduced several key features that enhance functionality, performance, and security.

### Invisible Indexes

Test the impact of removing an index without actually dropping it:

```sql
-- Create an invisible index
CREATE INDEX idx_lastname ON customers(last_name) INVISIBLE;

-- Make an existing index invisible
ALTER TABLE customers ALTER INDEX idx_email INVISIBLE;

-- Make an invisible index visible again
ALTER TABLE customers ALTER INDEX idx_lastname VISIBLE;

-- See all indexes including invisible ones
SELECT table_name, index_name, is_visible 
FROM information_schema.statistics 
WHERE table_schema = 'mydb';
```

### Descending Indexes

Create indexes that support efficient descending order operations:

```sql
-- Create a descending index
CREATE INDEX idx_created_at_desc ON orders (created_at DESC);

-- Multi-column mixed order index
CREATE INDEX idx_dept_salary ON employees (
  department_id ASC,
  salary DESC
);
```

### Roles-Based Access Control

```sql
-- Create roles
CREATE ROLE 'app_developer', 'app_read', 'app_write';

-- Grant privileges to roles
GRANT SELECT ON mydb.* TO 'app_read';
GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.* TO 'app_write';
GRANT ALL PRIVILEGES ON mydb.* TO 'app_developer';

-- Create users and assign roles
CREATE USER 'dev1'@'localhost' IDENTIFIED BY 'dev1pass';
CREATE USER 'analyst1'@'localhost' IDENTIFIED BY 'analyst1pass';

-- Grant roles to users
GRANT 'app_developer' TO 'dev1'@'localhost';
GRANT 'app_read' TO 'analyst1'@'localhost';

-- Set default roles
SET DEFAULT ROLE 'app_developer' TO 'dev1'@'localhost';
SET DEFAULT ROLE 'app_read' TO 'analyst1'@'localhost';

-- User activates granted role
SET ROLE 'app_developer';

-- Show current roles
SELECT CURRENT_ROLE();

-- Revoke roles
REVOKE 'app_write' FROM 'analyst1'@'localhost';
```

### Data Dictionary

MySQL 8.0 moved from file-based metadata storage to a transactional data dictionary:

```sql
-- Query the data dictionary
SELECT * FROM information_schema.tables WHERE table_schema = 'mydb';
SELECT * FROM information_schema.columns WHERE table_schema = 'mydb' AND table_name = 'users';

-- Check for locked tables
SELECT * FROM performance_schema.metadata_locks;
```

### Window Functions

MySQL 8.0 added full support for window functions (as detailed in the previous section):

```sql
SELECT 
  product_name,
  price,
  category,
  AVG(price) OVER(PARTITION BY category) AS avg_category_price,
  price - AVG(price) OVER(PARTITION BY category) AS diff_from_avg,
  PERCENT_RANK() OVER(PARTITION BY category ORDER BY price) AS percentile
FROM products;
```

### Other Notable MySQL 8.0 Features

```sql
-- Common Table Expressions (CTE)
WITH OrderSummary AS (
  SELECT customer_id, COUNT(*) AS order_count
  FROM orders
  GROUP BY customer_id
)
SELECT c.name, COALESCE(os.order_count, 0) AS orders
FROM customers c
LEFT JOIN OrderSummary os ON c.id = os.customer_id;

-- CHECK constraints
CREATE TABLE products (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  price DECIMAL(10,2) CHECK (price > 0),
  stock INT CHECK (stock >= 0)
);

-- Default expression with functions
CREATE TABLE audit_logs (
  id INT AUTO_INCREMENT PRIMARY KEY,
  message TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  user_id INT,
  client_ip VARCHAR(45) DEFAULT (SUBSTRING_INDEX(USER(), '@', -1))
);
```

---

## 📁 Accessing MySQL

```bash
# Log in as root
mysql -u root -p

# Log in to a specific database
mysql -u root -p mydb

# Use socket connection
mysql -S /var/run/mysqld/mysqld.sock -u root -p

# Connect to remote MySQL server
mysql -h remote_ip -u username -p
```

---

## 🔧 MySQL CLI Usage Tips

```bash
# Run single query directly
mysql -u root -p -e "SHOW DATABASES;"

# Run multiple commands from a file
mysql -u root -p < script.sql

# Save query results to a file
mysql -u root -p -e "SELECT * FROM users;" mydb > output.txt

# Export query results as CSV
mysql -u root -p -e "SELECT * FROM users" mydb --batch --silent > output.csv

# Use MySQL Shell for JSON output
mysqlsh --uri root@localhost --sql -e "SELECT * FROM users" --result-format=json > output.json

# Get help on commands
mysql --help

# Check MySQL version
mysql --version

# Open MySQL client with pager
mysql -u root -p --pager=less

# Use prompt customization
mysql --prompt="\u@\h [\d]> " -u root -p
```

---

## ⚙️ Configuration Files

* Default config file: `/etc/mysql/my.cnf`

Example important parameters:

```ini
[mysqld]
bind-address = 127.0.0.1
max_connections = 200
sql_mode = STRICT_ALL_TABLES
```

Restart MySQL after changes:

```bash
sudo systemctl restart mysql
```

---

## 🧪 Backup & Recovery Strategies

* **Scheduled Backups**: Use `cron` + `mysqldump`
* **Binary Logs**: Enable `log_bin` in config for point-in-time recovery
* **Replication**: Set up master-slave for high availability

```bash
# Cron job example for daily backup at midnight
0 0 * * * /usr/bin/mysqldump -u root -p'yourpass' mydb > /backups/mydb_$(date +\%F).sql
```

---

## 📚 Resources

* [https://dev.mysql.com/doc/](https://dev.mysql.com/doc/)
* [https://www.mysqltutorial.org/](https://www.mysqltutorial.org/)
* [https://sqlzoo.net/](https://sqlzoo.net/)
* [https://w3schools.com/sql/](https://w3schools.com/sql/)

> ✨ TIP: Always backup your database before major changes using `mysqldump`.
