# LAB 1 & Extra Challenges: SQL-lösningar

## LAB 1: Grundfrågor

**1. Show the first name and email of all customers. (10 rows)**
```sql
SELECT first_name, email
FROM customers;
2. Show all products in the Shoes category. (3 rows)

SQL
SELECT *
FROM products
WHERE category = 'Shoes';
3. Which customers live in Uppsala? (3 rows)

SQL
SELECT *
FROM customers
WHERE city = 'Uppsala';
4. Which product costs exactly 199 kr? (1 row)

SQL
SELECT *
FROM products
WHERE price = 199;
5. Show all products sorted by name, A to Z. (12 rows)

SQL
SELECT *
FROM products
ORDER BY name ASC;
6. Show all customers, the one who joined first at the top. (10 rows)

SQL
SELECT *
FROM customers
ORDER BY joined_date ASC;
7. Which products are sold out (stock is 0)? (2 rows)

SQL
SELECT *
FROM products
WHERE stock = 0;
8. Show the 3 newest customers. (3 rows)

SQL
SELECT *
FROM customers
ORDER BY joined_date DESC
LIMIT 3;
9. Show customers from Stockholm or Göteborg. Use IN. (4 rows)

SQL
SELECT *
FROM customers
WHERE city IN ('Stockholm', 'Göteborg');
10. Show product name and price, but call the columns product and price_sek. (12 rows)

SQL
SELECT name AS product, price AS price_sek
FROM products;
LAB 1: Bonusfrågor
Bonus 1: Show products that are Clothing or Shoes and cost more than 1000 kr. (3 rows)

Förklaring: AND har högre prioritet än OR i SQL. Utan parenteser utvärderas frågan som "Alla Shoes ELLER (Clothing som kostar > 1000)". Med parenteser blir villkoret "(Shoes eller Clothing) OCH kostar > 1000".

SQL
SELECT *
FROM products
WHERE (category = 'Shoes' OR category = 'Clothing')
  AND price > 1000;
Bonus 2: For every product in stock, show name, price, stock and the total value of the stock (price × stock) as stock_value. Highest value first. (10 rows)

SQL
SELECT name, price, stock, price * stock AS stock_value
FROM products
WHERE stock > 0
ORDER BY stock_value DESC;
Bonus 3: Which customers have a first name with exactly 4 letters? (4 rows)

SQL
SELECT *
FROM customers
WHERE first_name LIKE '____';
Bonus 4: Sort the products by price, cheapest first, and show only products number 6 to 10. (5 rows)

SQL
SELECT *
FROM products
ORDER BY price ASC
LIMIT 5 OFFSET 5;
Bonus 5: Show customers who joined before 2025 and don't live in Uppsala. Sort by city, and by last name within the same city. (4 rows)

SQL
SELECT *
FROM customers
WHERE city != 'Uppsala'
  AND joined_date < '2025-01-01'
ORDER BY city ASC, last_name ASC;
Extra Challenges
Level 1
Exercise 1: Show products that are not Accessories, are in stock, and have a space in their name. Sort by category, then by price from highest to lowest. (6 rows)

SQL
SELECT *
FROM products
WHERE name LIKE '% %'
  AND category != 'Accessories'
  AND stock > 0
ORDER BY category ASC, price DESC;
Exercise 2: Show customers who live in a city starting with S or M, plus customers with no city at all. (4 rows)

SQL
SELECT *
FROM customers
WHERE city LIKE 'S%'
   OR city LIKE 'M%'
   OR city IS NULL;
Exercise 3: Which Shoes product is the second most expensive? Show only that one. (1 row)

SQL
SELECT *
FROM products
WHERE category = 'Shoes'
ORDER BY price DESC
LIMIT 1 OFFSET 1;
Exercise 4: Of the customers who joined in 2024 or 2025, show the 3 who joined most recently. Solve it without BETWEEN and without >=. (3 rows)

SQL
SELECT *
FROM customers
WHERE joined_date > '2023-12-31'
  AND joined_date < '2026-01-01'
ORDER BY joined_date DESC
LIMIT 3;
Level 2
Exercise 5: Show each customer's full name in one column called full_name, sorted by last name. (10 rows)

SQL
SELECT first_name || ' ' || last_name AS full_name
FROM customers
ORDER BY last_name ASC;
Exercise 6: Give every product a price level: budget under 200 kr, mid from 200 to 799 kr, premium from 800 kr. (12 rows)

SQL
SELECT name, price,
  CASE 
    WHEN price < 200 THEN 'budget'
    WHEN price BETWEEN 200 AND 799 THEN 'mid'
    ELSE 'premium'
  END AS price_category
FROM products;
Exercise 7: Show every customer's first name and city, but write Unknown instead of NULL. (10 rows)

SQL
SELECT first_name, COALESCE(city, 'Unknown') AS city
FROM customers;
Exercise 8: Which customers joined in the first half of a year (January to June), whatever the year? (6 rows)

SQL
SELECT first_name, strftime('%m', joined_date) AS joined_month
FROM customers
WHERE strftime('%m', joined_date) BETWEEN '01' AND '06';
Exercise 9: Which product has the longest name? (1 row)

SQL
SELECT *
FROM products
ORDER BY LENGTH(name) DESC
LIMIT 1;
Exercise 10: Show each customer's email username: the part before the @. (10 rows)

SQL
SELECT SUBSTR(email, 1, INSTR(email, '@') - 1) AS emailname
FROM customers;
Level 3
Exercise 11: Which products cost more than the average price? (5 rows)

SQL
SELECT *
FROM products
WHERE price > (SELECT AVG(price) FROM products);
Exercise 12: Make a price list with one column ("Socks 3-pack costs 129 kr"). Only products in stock, cheapest first. CAST price as INT. (10 rows)

SQL
SELECT name || ' costs ' || CAST(price AS INT) || ' kr' AS description
FROM products
WHERE stock > 0
ORDER BY price ASC;
Exercise 13: How many customers live in each city? Biggest city first. (6 rows)

SQL
SELECT COUNT(*) AS [number of people in city], city
FROM customers
GROUP BY city
ORDER BY [number of people in city] DESC;