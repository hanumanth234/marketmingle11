create DATABASE IF NOT EXISTS ecom;
USE ecom;


CREATE TABLE person (
    pr_id INT PRIMARY KEY,
    age INT NOT NULL CHECK (age >= 18),
    ph_number VARCHAR(15) UNIQUE,
    email_id VARCHAR(90) NOT NULL,
    pr_name VARCHAR(50) NOT NULL
);

 
CREATE TABLE buyer (
    buyer_id INT PRIMARY KEY,
    gender VARCHAR(10) NOT NULL,
    address VARCHAR(89) NOT NULL,
    password VARCHAR(90) NOT NULL,
    pr_id INT,
    FOREIGN KEY (pr_id) REFERENCES person(pr_id)
);


CREATE TABLE product (
    prdct_id VARCHAR(90) PRIMARY KEY,
    brand_name VARCHAR(90) NOT NULL,
    prdct_name VARCHAR(90) NOT NULL,
    amount INT UNIQUE
);

CREATE TABLE seller (
    spr_id INT ,
    prdct_id VARCHAR(90) NOT NULL,
    FOREIGN KEY (prdct_id) REFERENCES product(prdct_id) ON DELETE CASCADE
);

-- Table: orders
CREATE TABLE orders (
    order_id VARCHAR(90) PRIMARY KEY,
    buyer_id INT,
    prdct_id VARCHAR(90),
    order_date DATE,
    order_amount INT,
    FOREIGN KEY (buyer_id) REFERENCES buyer(buyer_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY (prdct_id) REFERENCES product(prdct_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

-- Table: reviews
CREATE TABLE reviews (
    review_id INT PRIMARY KEY,
    prdct_id VARCHAR(90),
    rating FLOAT,
    description TEXT,
    FOREIGN KEY (prdct_id) REFERENCES product(prdct_id)
    ON DELETE CASCADE
);

-- Table: payment
CREATE TABLE payment (
    payment_id INT PRIMARY KEY,
    payment_date DATE,
    order_id VARCHAR(90),
    buyer_id INT,
    payment_method VARCHAR(89),
    amount INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (buyer_id) REFERENCES buyer(buyer_id)
);

CREATE TABLE category (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL
);

CREATE TABLE wishlist (
    wishlist_id INT PRIMARY KEY,
    buyer_id INT,
    prdct_id VARCHAR(90),
    FOREIGN KEY (buyer_id) REFERENCES buyer(buyer_id),
    FOREIGN KEY (prdct_id) REFERENCES product(prdct_id)
);

CREATE TABLE shipment (
    shipment_id INT PRIMARY KEY,
    order_id VARCHAR(90),
    shipment_date DATE,
    delivery_date DATE,
    status VARCHAR(50),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

ALTER TABLE product
ADD category_id INT,
ADD FOREIGN KEY (category_id) 
REFERENCES category(category_id);

INSERT INTO category 
(category_id, category_name) 
VALUES
(1, 'Electronics'),
(2, 'Groceries'),
(3, 'Clothing');



INSERT INTO person (pr_id, age, ph_number, email_id, pr_name) VALUES
(222, 19, '7903391548', 'nikhilkumar@gmail.com', 'nikhil kumar'),
(333, 21, '8745467665', 'sapavathhanumanth@gmail.com', 'hanumanth'),
(444, 54, '8964536376', 'sanjayramaswamy@gmail.com', 'sanjay'),
(111, 89, '9067365353', 'maheshpalli@gmail.com', 'mahesh'),
(555, 20, '8998753326', 'deepakjamlpur@gmail.com', 'deepakjamalpur');


INSERT INTO buyer (buyer_id, gender, address, password, pr_id) VALUES
(111, 'male', 'madhubani', 'nikhi__l123', 111),
(333, 'male', 'hyderabad', 'sanjay12@', 333),
(444, 'male', 'nalgonda', 'hanumanth123@', 444);



INSERT INTO product (prdct_id, brand_name, prdct_name, amount) VALUES
('AYRTHGBB' , 'DELL'   , 'laptop'    , 78900),
('RTRE456KL', 'MTR'    , 'MASALA'    , 100),
('RT4562BN' , 'I AND D', 'DOSABATTER', 500),
('567754TY' , 'VIVO'   , 'mobile'    , 71200),
('FRTT553'  , 'GOWRI'  , 'PEN'       , 740),
('DF663463' , 'RAMJAS' , 'PANCHA'    , 800),
('CB4154cA' , 'realmi' , 'mobile'    , 79900);

-- Insert data into seller
INSERT INTO seller 
(spr_id,prdct_id) VALUES
(222, 'AYRTHGBB'),
(555, 'RTRE456KL');

-- Insert data into orders
INSERT INTO orders (order_id, buyer_id, prdct_id, order_date, order_amount) VALUES
('AB575BN' , 111, 'AYRTHGBB' , '2024-09-14', 78900),
('BNHY5536', 444, 'RTRE456KL', '2024-01-10', 9999),
('UYTR564' , 111, 'RT4562BN' , '2024-01-12', 890),
('LKJH56' ,  111, '567754TY' , '2024-09-14', 5677);

-- Insert data into reviews
INSERT INTO reviews (review_id, prdct_id, rating, description) VALUES
(865, 'DF663463', 4.8, 'this good to the for the middle age people'),
(999, 'AYRTHGBB', 3.8, 'value for the money'),
(676, 'FRTT553', 2.8, 'highly not recommended to buy');

-- Insert data into payment
INSERT INTO payment (payment_id, payment_date, order_id, buyer_id, payment_method, amount)
VALUES
(45676235, '2024-09-14', 'AB575BN', 111, 'online', 78900),
(45674434, '2024-02-14', 'UYTR564', 111, 'online', 79009);




INSERT INTO wishlist (wishlist_id, buyer_id, prdct_id) VALUES
(1, 111, 'AYRTHGBB'),
(2, 333, '567754TY'),
(3, 111, 'RT4562BN');


INSERT INTO shipment (shipment_id, order_id, shipment_date, delivery_date, status) VALUES
(1, 'AB575BN', '2024-09-15', '2024-09-20', 'Delivered'),
(2, 'BNHY5536', '2024-01-11', '2024-01-15', 'In Transit'),
(3, 'UYTR564', '2024-01-13', '2024-01-18', 'Delivered');


UPDATE product 
SET category_id = 1
WHERE prdct_id IN ('AB4554AB', '567754TY');
UPDATE product 
SET category_id = 2 
WHERE prdct_id IN ('RTRE456KL', 'RT4562BN');
UPDATE product 
SET category_id = 3 
WHERE prdct_id IN ('FRTT553', 'DF663463');


SELECT * FROM person;
SELECT * FROM buyer;
SELECT * FROM seller;
SELECT * FROM payment;
SELECT * FROM product;
SELECT * FROM wishlist;
SELECT * FROM shipment;
SELECT * FROM reviews;
SELECT * FROM orders;


SELECT prdct_id FROM product WHERE prdct_id = 'AB4554AB';


SELECT * FROM PRODUCT;

SELECT prdct_id, SUM(order_amount) 
AS total_sales
FROM orders 
GROUP BY prdct_id;


SELECT prdct_id, COUNT(order_id) 
AS total_orders 
FROM orders GROUP BY prdct_id;



SELECT * FROM reviews 
WHERE prdct_id = 'AYRTHGBB';


SELECT prdct_id, AVG(rating) 
AS average_rating 
FROM reviews GROUP BY prdct_id;

SELECT * FROM shipment 
WHERE status = 'Delivered';


SELECT * FROM product 
WHERE prdct_id IN 
(SELECT prdct_id FROM seller WHERE spr_id = 222);


SELECT category_id, COUNT(prdct_id) 
AS total_products 
FROM product GROUP BY category_id;


SELECT buyer_id FROM 
wishlist WHERE prdct_id = 'AYRTHGBB';


SELECT buyer_id, SUM(amount) 
AS total_spent FROM payment GROUP BY buyer_id;


SELECT * FROM product 
WHERE prdct_id NOT IN (SELECT prdct_id FROM orders);


SELECT buyer_id, MAX(order_date) 
AS last_order_date FROM orders GROUP BY buyer_id;


SELECT * FROM product 
WHERE prdct_id IN (SELECT prdct_id FROM reviews WHERE rating < 3);
