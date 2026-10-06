CREATE TABLE pets (
 pet_id INTEGER PRIMARY KEY,
 name TEXT,
 species TEXT,
 age  INTEGER
);

INSERT INTO pets VALUES(1,'Bella', 'dog', 3);
SELECT * FROM pets;

INSERT INTO pets VALUES(2, NULL, 'cat', -5);


ALTER TABLE pets ADD COLUMN owner TEXT;
SELECT * FROM pets;

DROP TABLE pets;

CREATE TABLE pets(
 pet_id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT NOT NULL,
 species TEXT NOT NULL,
 age  INTEGER CHECK (age >= 0),
 vaccinated INTEGER DEFAULT 0
);


INSERT INTO pets (pet_id, name, species, age)
VALUES(2, 'Misse', 'cat', 3)
SELECT * FROM pets;

DROP TABLE pets;
CREATE TABLE orders(
 order_id INTEGER PRIMARY KEY,
 customer_id INTEGER NOT NULL,
 order_date TEXT NOT NULL,
 status TEXT NOT NULL DEFAULT 'new'
   CHECK (status IN ('new','shipped','delivered','cancelled')),
 FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);
CREATE TABLE order_items(
 order_id INTEGER NOT NULL,
 product_id INTEGER NOT NULL,
 quantity INTEGER NOT NULL CHECK (quantity > 0),
 unit_price REAL NOT NULL,
 PRIMARY KEY (order_id, product_id),
 FOREIGN KEY (order_id)REFERENCES orders(order_id),
 FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO orders(order_id, customer_id, order_date)
VALUES(100, 999, '2026-10-01');

CREATE TABLE books (
  book_id int PRIMARY KEY,
  title NOT NULL,
  author,
  year int
);

DROP TABLE books;

CREATE TABLE books (
  book_id int PRIMARY KEY,
  title NOT NULL,
  author, -- forgot to add TEXT definition, no Error. Default type == ?
  year int CHECK (year > 1400)
);

ALTER TABLE books
ADD ISBN TEXT;

DROP TABLE books;

CREATE TABLE reviews (
  review_id INTEGER PRIMARY KEY, -- primary key as integer, column name review_id
  product_id INTEGER, -- FOREIGN key, definied as forgein later, integer
  rating INTEGER CHECK (rating >= 1 AND rating <= 5), -- rate as int, value beteween 1-5
  FOREIGN KEY (product_id) REFERENCES products(product_id) -- here the forgein key is pointing towards the other table
);

INSERT INTO reviews(review_id, product_id, rating)
VALUES(1, 11, 6);

INSERT INTO reviews(review_id, product_id, rating)
VALUES(1, 50, 3);

CREATE TABLE suppliers (
  supplier_id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  country TEXT DEFAULT 'Sweden',
  email TEXT
  );
  
INSERT INTO suppliers(supplier_id, name, email)
VALUES(1, "Grossisten AB", "erika@grossisten.se")

DROP TABLE suppliers;

INSERT INTO suppliers(supplier_id, name, email)
VALUES(2, "Nordic Textiles", "spanien@eu.eu")

INSERT INTO suppliers(supplier_id, name, email) --FAILS PGA. UNIQUE NOT ...name
VALUES(3, "Nordic Textiles", "porto@portugul.eu")

CREATE TABLE coupons (
  coupon_code TEXT PRIMARY KEY,
  discount_pct INTEGER CHECK (discount_pct BETWEEN 10 AND 90),
  valid_until INTEGER NOT NULL
  );
  
INSERT INTO coupons(coupon_code, discount_pct, valid_until)
VALUES("SUMMER20", 95, 2027)

INSERT INTO suppliers(name, email) --supplier_id just +1 if not supplied ;)
VALUES("Grossebergas Konfektyr", "gekas@eu.eu")

ALTER TABLE suppliers
RENAME COLUMN email to contact_email;

PRAGMA table_info(suppliers);

CREATE TABLE product_suppliers (
  supplier_id INTEGER,
  product_id INTEGER,
  price INTEGER CHECK (price > 0),
  PRIMARY KEY (supplier_id, product_id),
  FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO product_suppliers (product_id, supplier_id, price) 
VALUES (1, 99, 100);

CREATE TABLE campaigns (
  name TEXT PRIMARY KEY,
  start_date INT,
  end_date INT CHECK (end_date > start_date)
);

INSERT INTO campaigns (name, start_date, end_date)
VALUES ("cool Summer 20!", 20260101, 20251210);

CREATE TABLE product_sizes (
  product_size_id INTEGER PRIMARY KEY,
  product_id INTEGER,
  size TEXT CHECK (size IN ('S', 'M', 'L', 'XL')), 
  stock INTEGER DEFAULT 0 CHECK (stock >= 0),
  FOREIGN KEY (product_id) REFERENCES products(product_id),
  UNIQUE (product_id, size)
);

INSERT INTO product_sizes (product_size_id, product_id, size, stock)
VALUES (1, 1, "M", 200);

INSERT INTO product_sizes (product_size_id, product_id, size, stock)
VALUES (2, 1, "M", 200);

DROP TABLE product_sizes;

CREATE TABLE employees (
	employee_id INTEGER PRIMARY KEY,
	employees_manager INTEGER DEFAULT NULL,
	FOREIGN KEY (employees_manager) REFERENCES employees(employee_id)
);

INSERT INTO employees (employee_id)
VALUES (1);
	
INSERT INTO employees (employee_id, employees_manager)
VALUES (2, 1);
	
INSERT INTO employees (employee_id, employees_manager)
VALUES (3, 1);

CREATE TABLE teams(
	name TEXT UNIQUE PRIMARY KEY
);

CREATE TABLE players(
	player_id INTEGER PRIMARY KEY,
	player_name TEXT,
	player_team TEXT,
	FOREIGN KEY (player_team) REFERENCES teams(name) ON DELETE CASCADE
);

DROP TABLE players;

INSERT INTO teams (name)
VALUES ('Miami Red Hawks');

INSERT INTO players (player_id, player_name, player_team)
VALUES (1, 'John Cena', 'Miami Red Hawks');

INSERT INTO players (player_id, player_name, player_team)
VALUES (2, 'Gilles Deleuze', 'Miami Red Hawks');

DROP TABLE teams;