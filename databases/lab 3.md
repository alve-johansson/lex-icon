INSERT INTO customers(customer\_id, first\_name, last\_name, email, city, joined\_date)

VALUES (11, 'Alve', 'Johansson', 'alvejohansson@pm.me', 'Götebäst', '2026-10-07')



SELECT \* FROM customers;



INSERT INTO products(name, category, price, stock)

VALUES ('Scarf', 'Accessories', 229, 15), ('Gloves', 'Accessories', 199, 20)



SELECT \* FROM products;



INSERT INTO orders(customer\_id, order\_date, status)

VALUES (7, '2026-10-07', 'new');



INSERT INTO order\_items(order\_id, product\_id, quantity, unit\_price)

VALUES (16, 10, 2, 199);



INSERT INTO order\_items(order\_id, product\_id, quantity, unit\_price)

VALUES (16, 10, 0, 199);

\-- Result: CHECK constraint failed: quantity > 0



UPDATE orders 

SET status = 'shipped' 

WHERE order\_id = 12;



SELECT \* FROM orders;



UPDATE products

SET stock = 50 

WHERE product\_id = 5;



SELECT \* FROM products;



UPDATE products

SET price = price \* 1.1

WHERE category = 'Accessories';



SELECT \* FROM products;



SELECT \* FROM orders;



DELETE FROM orders WHERE status = 'cancelled';

\-- Result: FOREIGN KEY constraint failed



DELETE FROM order\_items

WHERE order\_id IN (

&#x20;   SELECT order\_id 

&#x20;   FROM orders 

&#x20;   WHERE status = 'cancelled'

);



DELETE FROM orders

WHERE status = 'cancelled';



SELECT \* FROM orders; 

SELECT \* FROM order\_items;



SELECT COUNT (\*) FROM orders;





Exercise 10

Look at this table: student | phone\_numbers | course1 | course2 | course3. List every problem you

can find.



Unclear what student is denoting: an index id? a name? phone\_numbers is actually written in pluralis and if that is the case many, that's bad design, otherwise it should be phone\_number. course1/2/3 is bad design what if course4? curriculum or something like that. maybe semester.





Exercise 11

In order\_sheet, which normal form does the products column break? How would you fix it?

order\_no should probably be defined as primary key. all the customer info: email, city should be in another table. products should probably be another table: which kind, how many, etc. and total does not require a row as it can be easily calculated. customer should be forgein key. email in customer should be unique.
BREAKS 1NF.



CREATE TABLE order\_sheet (  order\_no INTEGER,  customer TEXT,  email    TEXT,  city     TEXT,  products TEXT,  total    REAL);



Exercise 12

A table has: order\_id | customer\_id | customer\_email | order\_date. Which column is in the wrong

place? Why? BREAKS 3NF

customer\_email should be in customer table where the customer ID is primary key.



Exercise 13

Music school (in pairs): '**Student**s take lessons from **teacher**s. A **lesson** has a date, time, room and

instrument. One teacher can teach many **instrument**s.' Underline the things.



Exercise 14
STUDENT N:N LESSON N:1 TEACHER

LESSON N:1 INSTRUMENT N:N TEACHER



Exercise 15

Draw the ER diagram for the music school.



Exercise 16

Write the CREATE TABLE statements for the music school in a new file music.db.

Database: create a new file. Click New Database, name it music.db, and click Cancel in the 'Edit

table definition' window. Don't create these tables in webshop.db

