DROP DATABASE IF EXISTS `online retail store`;
CREATE DATABASE `online retail store`;
USE `online retail store`;
SET NAMES 'utf8mb4';
SET character_set_client = 'utf8mb4';
CREATE TABLE `Admin` (
`username` varchar(50) NOT NULL,
`password` varchar(20) NOT NULL
);
INSERT INTO `Admin` (`username`, `password`) VALUES ('VipulMishra', '22596');
INSERT INTO `Admin` (`username`, `password`) VALUES ('NamitJain', '22315');
INSERT INTO `Admin` (`username`, `password`) VALUES ('PrajilBhagat', '22359');
INSERT INTO `Admin` (`username`, `password`) VALUES ('AyushSinghal', '22127');
CREATE TABLE `Category` (
`categoryID` INT NOT NULL AUTO_INCREMENT,
`category_name` varchar(50) NOT NULL,
`category_discount` DOUBLE DEFAULT 0,
PRIMARY KEY(`categoryID`),
CONSTRAINT `Category_chk_1` CHECK ((`category_discount` >= 0 AND `category_discount` < 100))
);
INSERT INTO `Category` (`category_name`, `category_discount`) VALUES ('Fresh Fruits', 5);
INSERT INTO `Category` (`category_name`, `category_discount`) VALUES ('Vegetables', 5);
INSERT INTO `Category` (`category_name`, `category_discount`) VALUES ('Dairy & Eggs', 10);
INSERT INTO `Category` (`category_name`, `category_discount`) VALUES ('Meat & Seafood', 15);
INSERT INTO `Category` (`category_name`, `category_discount`) VALUES ('Bakery', 5);
INSERT INTO `Category` (`category_name`, `category_discount`) VALUES ('Frozen Foods', 10);
INSERT INTO `Category` (`category_name`, `category_discount`) VALUES ('Pantry Staples', 2);
INSERT INTO `Category` (`category_name`, `category_discount`) VALUES ('Canned Goods', 3);
INSERT INTO `Category` (`category_name`, `category_discount`) VALUES ('Snacks & Sweets', 8);
INSERT INTO `Category` (`category_name`, `category_discount`) VALUES ('Beverages', 10);
INSERT INTO `Category` (`category_name`, `category_discount`) VALUES ('Alcoholic Beverages', 20);
INSERT INTO `Category` (`category_name`, `category_discount`) VALUES ('Health & Wellness', 15);
INSERT INTO `Category` (`category_name`, `category_discount`) VALUES ('Baby Products', 10);
INSERT INTO `Category` (`category_name`, `category_discount`) VALUES ('Pet Supplies', 5);
INSERT INTO `Category` (`category_name`, `category_discount`) VALUES ('Household Essentials', 10);
INSERT INTO `Category` (`category_name`, `category_discount`) VALUES ('Personal Care', 12);
INSERT INTO `Category` (`category_name`, `category_discount`) VALUES ('Organic Products', 10);
INSERT INTO `Category` (`category_name`, `category_discount`) VALUES ('International Foods', 15);
INSERT INTO `Category` (`category_name`, `category_discount`) VALUES ('Spices & Seasonings', 7);
INSERT INTO `Category` (`category_name`, `category_discount`) VALUES ('Tea & Coffee', 10);
CREATE TABLE `Warehouse` (
`WarehouseID` INT NOT NULL,
`Manager` varchar(50) NOT NULL,
`phone_number` char(10) NOT NULL,
`house_number` varchar(10) NOT NULL,
`street_name` varchar(100) DEFAULT NULL,
`city` varchar(100) NOT NULL,
`zone` varchar(100) NOT NULL,
`pincode` char(6) NOT NULL,
PRIMARY KEY(`WarehouseID`)
);
INSERT INTO `Warehouse` VALUES ('1', 'Vipul', '8929224366', 'HN407', 'SouthEx', 'Delhi', 'South', '110049');
INSERT INTO `Warehouse` VALUES ('2', 'Namit', '7417489800', 'HN202', 'PunjabiBagh', 'Delhi', 'West', '110026');
INSERT INTO `Warehouse` VALUES ('3', 'Prajil', '7320061608', 'HN120', 'Shahdara', 'Delhi', 'East', '110002');
INSERT INTO `Warehouse` VALUES ('4', 'Ayush', '8249282346', 'HN24', 'KamlaNagar', 'Delhi', 'North', '110007');
INSERT INTO `Warehouse` VALUES ('5', 'Karan', '9968482891', 'HN60', 'KarolBagh', 'Delhi', 'Central', '110005');
CREATE TABLE `Customer` (
`username` varchar(50) NOT NULL,
`password` varchar(20) NOT NULL,
`first_name` varchar(100) NOT NULL,
`last_name` varchar(100) NOT NULL,
`phone_number` char(10) NOT NULL,
`house_number` varchar(10) NOT NULL,
`street_name` varchar(100) DEFAULT NULL,
`city` varchar(100) NOT NULL,
`zone` varchar(100) NOT NULL,
`pincode` char(6) NOT NULL,
PRIMARY KEY(`username`)
);
INSERT INTO `Customer` VALUES ('rajPatel', 'raj2024Pass', 'Raj', 'Patel', '9876543210', '15', 'Lotus Colony', 'Delhi',
'North', '110001');
INSERT INTO `Customer` VALUES ('priyaKumar', 'priyaK123', 'Priya', 'Kumar', '8765432109', '22', 'Gulmohar Lane',
'Delhi', 'North', '110001');
INSERT INTO `Customer` VALUES ('amitShah', 'amitS456', 'Amit', 'Shah', '7654321098', '48', 'Mango Avenue',
'Delhi', 'West', '110001');
INSERT INTO `Customer` VALUES ('sunitaRao', 'sunitaR789', 'Sunita', 'Rao', '6543210987', '37', 'Palm Street', 'Delhi',
'South', '110001');
INSERT INTO `Customer` VALUES ('vijayDeshmukh', 'vijayD2024', 'Vijay', 'Deshmukh', '5432109876', '29', 'Peepal
Drive', 'Delhi', 'West', '110001');
INSERT INTO `Customer` VALUES ('anitaSingh', 'anitaS321', 'Anita', 'Singh', '4321098765', '11', 'Banyan Road',
'Delhi', 'North', '110001');
INSERT INTO `Customer` VALUES ('manojKumar', 'manojK654', 'Manoj', 'Kumar', '3210987654', '55', 'Cypress Lane',
'Delhi', 'South', '110001');
INSERT INTO `Customer` VALUES ('deepaMalik', 'deepaM987', 'Deepa', 'Malik', '2109876543', '42', 'Bamboo
Crescent', 'Delhi', 'East', '110001');
INSERT INTO `Customer` VALUES ('rohitSharma', 'rohitS2024', 'Rohit', 'Sharma', '1098765432', '78', 'Teakwood
Terrace', 'Delhi', 'North', '110001');
INSERT INTO `Customer` VALUES ('meenaIyer', 'meenaI321', 'Meena', 'Iyer', '0987654321', '66', 'Sandalwood Blvd',
'Delhi', 'South', '110001');
INSERT INTO `Customer` VALUES ('akashVerma', 'akashV654', 'Akash', 'Verma', '1234509876', '24', 'Maple Street',
'Delhi', 'Central', '110001');
INSERT INTO `Customer` VALUES ('nehaJain', 'nehaJ987', 'Neha', 'Jain', '2345610987', '33', 'Olive Avenue', 'Delhi',
'Central', '110001');
INSERT INTO `Customer` VALUES ('sureshReddy', 'sureshR2024', 'Suresh', 'Reddy', '3456721098', '90', 'Pine Path',
'Delhi', 'South', '110001');
INSERT INTO `Customer` VALUES ('gitaMishra', 'gitaM321', 'Gita', 'Mishra', '4567832109', '18', 'Rose Valley', 'Delhi',
'East', '110001');
INSERT INTO `Customer` VALUES ('vivekNair', 'vivekN654', 'Vivek', 'Nair', '5678943210', '27', 'Lotus Pond', 'Delhi',
'South', '110001');
INSERT INTO `Customer` VALUES ('raniDas', 'raniD987', 'Rani', 'Das', '6789054321', '99', 'Jasmine Garden', 'Delhi',
'East', '110001');
INSERT INTO `Customer` VALUES ('kunalShaw', 'kunalS2024', 'Kunal', 'Shaw', '7890165432', '3', 'Tulip Corner',
'Delhi', 'East', '110001');
INSERT INTO `Customer` VALUES ('soniaChopra', 'soniaC321', 'Sonia', 'Chopra', '8901276543', '12', 'Fern Road',
'Delhi', 'North', '110001');
INSERT INTO `Customer` VALUES ('arjunMehta', 'arjunM654', 'Arjun', 'Mehta', '9012387654', '45', 'Orchid Avenue',
'Delhi', 'North', '110001');
INSERT INTO `Customer` VALUES ('tanviPrasad', 'tanviP987', 'Tanvi', 'Prasad', '0123498765', '56', 'Willow Lane',
'Delhi', 'North', '110001');
CREATE TABLE `Product` (
`productID` INT NOT NULL AUTO_INCREMENT,
`categoryID` INT NOT NULL,
`name` varchar(50) DEFAULT NULL,
`quantity_in_stock` INT DEFAULT 0,
`price` DOUBLE DEFAULT 0,
`discount` DOUBLE DEFAULT 0,
`storage_type` varchar(50) NOT NULL,
`rating` INT DEFAULT NULL,
`description` varchar(100) DEFAULT NULL,
PRIMARY KEY(`productID`),
CONSTRAINT `Product_ibfk_1` FOREIGN KEY (`categoryID`) REFERENCES `Category` (`categoryID`) ON
UPDATE CASCADE,
CONSTRAINT `Product_chk_1` CHECK (`quantity_in_stock` >= 0),
CONSTRAINT `Product_chk_2` CHECK (`discount` >= 0 AND `discount` < 100),
CONSTRAINT `Product_chk_3` CHECK (`rating` IS NULL OR (`rating` >= 1 AND `rating` <= 5))
);
INSERT INTO `Product` (categoryID, name, quantity_in_stock, price, discount, storage_type, rating, description)
VALUES (1, 'Whole Wheat Bread', 100, 40, 10, 'Ambient', 4, 'Healthy whole grain bread');
INSERT INTO `Product` (categoryID, name, quantity_in_stock, price, discount, storage_type, rating, description)
VALUES (2, 'Organic Brown Eggs', 200, 60, 5, 'Refrigerated', 5, 'Farm fresh organic eggs');
INSERT INTO `Product` (categoryID, name, quantity_in_stock, price, discount, storage_type, rating, description)
VALUES (1, 'Almond Milk', 150, 120, 0, 'Refrigerated', 4, 'Lactose-free milk alternative');
INSERT INTO `Product` (categoryID, name, quantity_in_stock, price, discount, storage_type, rating, description)
VALUES (4, 'Quinoa', 75, 200, 15, 'Ambient', 4, 'High-protein, gluten-free');
INSERT INTO `Product` (categoryID, name, quantity_in_stock, price, discount, storage_type, rating, description)
VALUES (4, 'Broccoli', 50, 30, 0, 'Fresh', 5, 'Rich in vitamins K and C');
INSERT INTO `Product` (categoryID, name, quantity_in_stock, price, discount, storage_type, rating, description)
VALUES (6, 'Gala Apples', 100, 90, 10, 'Fresh', 5, 'Crisp and very sweet');
INSERT INTO `Product` (categoryID, name, quantity_in_stock, price, discount, storage_type, rating, description)
VALUES (9, 'Organic Chicken Breast', 80, 220, 5, 'Frozen', 4, 'Free-range organic chicken');
INSERT INTO `Product` (categoryID, name, quantity_in_stock, price, discount, storage_type, rating, description)
VALUES (8, 'Basmati Rice', 200, 110, 0, 'Ambient', 4, 'Long grain aromatic rice');
INSERT INTO `Product` (categoryID, name, quantity_in_stock, price, discount, storage_type, rating, description)
VALUES (9, 'Extra Virgin Olive Oil', 60, 250, 20, 'Ambient', 5, 'Perfect for salad dressings');
INSERT INTO `Product` (categoryID, name, quantity_in_stock, price, discount, storage_type, rating, description)
VALUES (1, 'Dark Chocolate', 150, 100, 15, 'Ambient', 5, '70% cocoa, rich in antioxidants');
INSERT INTO `Product` (categoryID, name, quantity_in_stock, price, discount, storage_type, rating, description)
VALUES (11, 'Greek Yogurt', 100, 80, 5, 'Refrigerated', 4, 'Rich in protein');
INSERT INTO `Product` (categoryID, name, quantity_in_stock, price, discount, storage_type, rating, description)
VALUES (12, 'Almonds', 120, 150, 10, 'Ambient', 5, 'High in healthy fats');
INSERT INTO `Product` (categoryID, name, quantity_in_stock, price, discount, storage_type, rating, description)
VALUES (10, 'Spinach', 100, 40, 0, 'Fresh', 5, 'Loaded with nutrients');
INSERT INTO `Product` (categoryID, name, quantity_in_stock, price, discount, storage_type, rating, description)
VALUES (14, 'Sweet Potatoes', 80, 35, 0, 'Fresh', 4, 'Rich in fiber, vitamins, and minerals');
INSERT INTO `Product` (categoryID, name, quantity_in_stock, price, discount, storage_type, rating, description)
VALUES (15, 'Salmon Fillets', 70, 300, 5, 'Frozen', 4, 'Rich in Omega-3 fatty acids');
INSERT INTO `Product` (categoryID, name, quantity_in_stock, price, discount, storage_type, rating, description)
VALUES (16, 'Cauliflower', 90, 25, 0, 'Fresh', 4, 'Can be used in various dishes');
INSERT INTO `Product` (categoryID, name, quantity_in_stock, price, discount, storage_type, rating, description)
VALUES (17, 'Peanut Butter', 110, 150, 10, 'Ambient', 4, 'No added sugar');
INSERT INTO `Product` (categoryID, name, quantity_in_stock, price, discount, storage_type, rating, description)
VALUES (18, 'Whole Chicken', 50, 250, 10, 'Frozen', 3, 'Perfect for roasting');
INSERT INTO `Product` (categoryID, name, quantity_in_stock, price, discount, storage_type, rating, description)
VALUES (19, 'Mixed Nuts', 200, 400, 20, 'Ambient', 5, 'Ideal for snacking');
INSERT INTO `Product` (categoryID, name, quantity_in_stock, price, discount, storage_type, rating, description)
VALUES (20, 'Blueberries', 60, 150, 5, 'Fresh', 5, 'High in antioxidants');
CREATE TABLE `Inventory` (
`productID` INT NOT NULL,
`quantity` INT DEFAULT 0,
`storage_type` varchar(50) NOT NULL,
`WarehouseID` INT NOT NULL,
PRIMARY KEY(`productID`, `storage_type`),
CONSTRAINT `Inventory_ibfk_1` FOREIGN KEY (`productID`) REFERENCES `Product` (`productID`) ON UPDATE
CASCADE,
CONSTRAINT `Inventory_ibfk_2` FOREIGN KEY (`WarehouseID`) REFERENCES `Warehouse` (`WarehouseID`)
ON UPDATE CASCADE,
CONSTRAINT `Inventory_chk_1` CHECK (`quantity` >= 0)
);
INSERT INTO `Inventory` (productID, quantity, storage_type, WarehouseID) VALUES (1, 100, 'Ambient', 1);
INSERT INTO `Inventory` (productID, quantity, storage_type, WarehouseID) VALUES (2, 200, 'Refrigerated', 2);
INSERT INTO `Inventory` (productID, quantity, storage_type, WarehouseID) VALUES (3, 150, 'Refrigerated', 3);
INSERT INTO `Inventory` (productID, quantity, storage_type, WarehouseID) VALUES (4, 75, 'Ambient', 4);
INSERT INTO `Inventory` (productID, quantity, storage_type, WarehouseID) VALUES (5, 50, 'Fresh', 5);
INSERT INTO `Inventory` (productID, quantity, storage_type, WarehouseID) VALUES (6, 100, 'Fresh', 1);
INSERT INTO `Inventory` (productID, quantity, storage_type, WarehouseID) VALUES (7, 80, 'Frozen', 2);
INSERT INTO `Inventory` (productID, quantity, storage_type, WarehouseID) VALUES (8, 200, 'Ambient', 3);
INSERT INTO `Inventory` (productID, quantity, storage_type, WarehouseID) VALUES (9, 60, 'Ambient', 4);
INSERT INTO `Inventory` (productID, quantity, storage_type, WarehouseID) VALUES (10, 150, 'Ambient', 5);
INSERT INTO `Inventory` (productID, quantity, storage_type, WarehouseID) VALUES (11, 100, 'Refrigerated', 1);
INSERT INTO `Inventory` (productID, quantity, storage_type, WarehouseID) VALUES (12, 120, 'Ambient', 2);
INSERT INTO `Inventory` (productID, quantity, storage_type, WarehouseID) VALUES (13, 100, 'Fresh', 3);
INSERT INTO `Inventory` (productID, quantity, storage_type, WarehouseID) VALUES (14, 80, 'Fresh', 4);
INSERT INTO `Inventory` (productID, quantity, storage_type, WarehouseID) VALUES (15, 70, 'Frozen', 5);
INSERT INTO `Inventory` (productID, quantity, storage_type, WarehouseID) VALUES (16, 90, 'Fresh', 1);
INSERT INTO `Inventory` (productID, quantity, storage_type, WarehouseID) VALUES (17, 110, 'Ambient', 2);
INSERT INTO `Inventory` (productID, quantity, storage_type, WarehouseID) VALUES (18, 50, 'Frozen', 3);
INSERT INTO `Inventory` (productID, quantity, storage_type, WarehouseID) VALUES (19, 200, 'Ambient', 4);
INSERT INTO `Inventory` (productID, quantity, storage_type, WarehouseID) VALUES (20, 60, 'Fresh', 5);
CREATE TABLE `Cart` (
    `CartID` INT AUTO_INCREMENT NOT NULL,
    `billing_amount` DECIMAL(9,2) NOT NULL,
    `productID` INT DEFAULT 1,
    `quantity` INT NOT NULL,
    `username` VARCHAR(30) NOT NULL,
    PRIMARY KEY (`CartID`,`productID`),
    CONSTRAINT `Cart_ibfk_1` FOREIGN KEY (`productID`) REFERENCES `Product` (`productID`) ON UPDATE CASCADE,
    CONSTRAINT `Cart_ibfk_2` FOREIGN KEY (`username`) REFERENCES `Customer` (`username`) ON UPDATE CASCADE,
    CONSTRAINT `Cart_chk_3` CHECK (`quantity` >= 0)
);
INSERT INTO `Cart` (CartID, billing_amount, productID, quantity, username) VALUES
(1, 120.00, 1, 2, 'rajPatel'),
(2, 180.50, 2, 1, 'priyaKumar'),
(3, 75.00, 3, 3, 'amitShah'),
(4, 240.00, 4, 4, 'sunitaRao'),
(5, 300.00, 5, 5, 'vijayDeshmukh'),
(6, 450.00, 6, 1, 'anitaSingh'),
(1, 80.00, 7, 2, 'rajPatel'),
(8, 90.00, 8, 1, 'deepaMalik'),
(9, 200.00, 9, 2, 'rohitSharma'),
(1, 110.00, 10, 1, 'rajPatel'),
(11, 250.00, 11, 3, 'akashVerma'),
(12, 160.00, 12, 2, 'nehaJain'),
(13, 190.00, 13, 1, 'sureshReddy'),
(5, 85.00, 14, 1, 'vijayDeshmukh'),
(15, 125.00, 15, 5, 'vivekNair'),
(16, 140.00, 16, 2, 'raniDas'),
(5, 220.00, 17, 4, 'vijayDeshmukh'),
(18, 175.00, 18, 3, 'soniaChopra'),
(19, 260.00, 19, 2, 'arjunMehta'),
(19, 300.00, 20, 6, 'arjunMehta');
-- Make sure Cart is created before Order
CREATE TABLE `Order` (
`orderID` INT NOT NULL AUTO_INCREMENT,
`username` varchar(50) NOT NULL,
`status` varchar(20) NOT NULL,
`order_amount` decimal(9,2) NOT NULL,
`discount` DOUBLE DEFAULT 0,
`date_order_placed` datetime DEFAULT NULL,
PRIMARY KEY(`orderID`),
CONSTRAINT `Order_ibfk_1` FOREIGN KEY (`username`) REFERENCES `Customer` (`username`) ON UPDATE
CASCADE
);
INSERT INTO `Order` (username, status, order_amount, discount, date_order_placed) VALUES
('rajPatel', 'Processing', 150.00, 0, '2024-02-10 10:00:00'),
('priyaKumar', 'Shipped', 200.00, 5, '2024-02-11 11:30:00'),
('amitShah', 'Delivered', 300.00, 10, '2024-02-12 14:45:00'),
('sunitaRao', 'Cancelled', 50.00, 0, '2024-02-13 16:00:00'),
('vijayDeshmukh', 'Processing', 75.00, 0, '2024-02-14 09:20:00'),
('anitaSingh', 'Shipped', 220.00, 15, '2024-02-15 08:15:00'),
('rajPatel', 'Delivered', 180.00, 0, '2024-02-16 12:10:00'),
('deepaMalik', 'Cancelled', 90.00, 5, '2024-02-17 13:50:00'),
('rohitSharma', 'Processing', 160.00, 0, '2024-02-18 15:30:00'),
('rajPatel', 'Shipped', 250.00, 10, '2024-02-19 17:00:00'),
('akashVerma', 'Delivered', 100.00, 0, '2024-02-20 18:20:00'),
('nehaJain', 'Cancelled', 110.00, 5, '2024-02-21 19:45:00'),
('sureshReddy', 'Processing', 120.00, 0, '2024-02-22 20:00:00'),
('vijayDeshmukh', 'Shipped', 130.00, 10, '2024-02-23 21:15:00'),
('vivekNair', 'Delivered', 140.00, 0, '2024-02-24 22:30:00'),
('raniDas', 'Cancelled', 160.00, 5, '2024-02-25 23:45:00'),
('vijayDeshmukh', 'Processing', 170.00, 0, '2024-02-26 10:50:00'),
('soniaChopra', 'Shipped', 180.00, 15, '2024-02-27 11:55:00'),
('arjunMehta', 'Delivered', 190.00, 0, '2024-02-28 12:00:00'),
('arjunMehta', 'Cancelled', 200.00, 10, '2024-03-01 13:05:00');
CREATE TABLE `NGO` (
`ngoID` INT NOT NULL AUTO_INCREMENT,
`name` VARCHAR(50) NOT NULL,
`registration_number` INT NOT NULL,
`username` VARCHAR(50) NOT NULL,
`funds_raised` DECIMAL(9,2) NOT NULL,
PRIMARY KEY (`ngoID`)
);
INSERT INTO `NGO` (`name`, `registration_number`, `username`, `funds_raised`) VALUES
('Green Revolution', 20001, 'rajPatel', 50000.00),
('Digital Literacy', 20002, 'priyaKumar', 32000.00),
('Animal Rescue', 20003, 'amitShah', 28000.00),
('River Cleanup', 20004, 'sunitaRao', 15000.00),
('Youth Sports', 20005, 'vijayDeshmukh', 22000.00),
('Art for All', 20006, 'anitaSingh', 26000.00),
('Urban Farming', 20007, 'manojKumar', 31000.00),
('Senior Support', 20008, 'deepaMalik', 18000.00),
('Renewable Schools', 20009, 'rohitSharma', 47000.00),
('Food Security', 20010, 'meenaIyer', 34000.00),
('Water for Life', 20011, 'akashVerma', 21000.00),
('Health for All', 20012, 'nehaJain', 44000.00),
('Affordable Housing', 20013, 'sureshReddy', 39000.00),
('Cultural Exchange', 20014, 'gitaMishra', 17000.00),
('Tech for Good', 20015, 'vivekNair', 29000.00),
('Literacy Program', 20016, 'raniDas', 37000.00),
('Community Gardens', 20017, 'kunalShaw', 33000.00),
('Empowerment Workshops', 20018, 'soniaChopra', 25000.00),
('Climate Awareness', 20019, 'arjunMehta', 41000.00),
('Mental Health Support', 20020, 'tanviPrasad', 36000.00);
CREATE TABLE `Billing` (
`billingID` INT NOT NULL AUTO_INCREMENT,
`payment_mode` VARCHAR(50) NOT NULL,
`bill_amount` DECIMAL(9,2) NOT NULL,
`amount_donated` DECIMAL(9,2) NOT NULL,
`orderID` INT NOT NULL,
`ngoID` INT NOT NULL,
PRIMARY KEY (`billingID`),
FOREIGN KEY (`orderID`) REFERENCES `Order` (`orderID`) ON UPDATE CASCADE,
FOREIGN KEY (`ngoID`) REFERENCES `NGO` (`ngoID`) ON UPDATE CASCADE
);
INSERT INTO `Billing` (`payment_mode`, `bill_amount`, `amount_donated`, `orderID`, `ngoId`) VALUES
('Credit Card', 1500.00, 50.00, 1, 1),
('Debit Card', 750.00, 0.00, 2, 2),
('Net Banking', 1250.00, 25.00, 3, 3),
('UPI', 500.00, 5.00, 4, 4),
('Cash on Delivery', 950.00, 0.00, 5, 5),
('Credit Card', 1600.00, 100.00, 6, 6),
('Debit Card', 800.00, 0.00, 7, 7),
('Net Banking', 1350.00, 30.00, 8, 8),
('UPI', 600.00, 10.00, 9, 9),
('Cash on Delivery', 1050.00, 0.00, 10, 10),
('Credit Card', 1700.00, 150.00, 11, 11),
('Debit Card', 850.00, 0.00, 12, 12),
('Net Banking', 1450.00, 35.00, 13, 13),
('UPI', 700.00, 15.00, 14, 14),
('Cash on Delivery', 1150.00, 0.00, 15, 15),
('Credit Card', 1800.00, 200.00, 16, 16),
('Debit Card', 900.00, 0.00, 17, 17),
('Net Banking', 1550.00, 40.00, 18, 18),
('UPI', 800.00, 20.00, 19, 19),
('Cash on Delivery', 1250.00, 0.00, 20, 20);
CREATE TABLE `Distributor` (
`distributorID` INT NOT NULL ,
`password` VARCHAR(20) NOT NULL,
`productID` INT NOT NULL,
`phone_number` CHAR(10) NOT NULL,
`email_address` VARCHAR(50) NOT NULL,
`commission` DECIMAL(9,2) NOT NULL,
`house_number` VARCHAR(10) NOT NULL,
`street_name` VARCHAR(100) DEFAULT NULL,
`city` VARCHAR(100) NOT NULL,
`pincode` CHAR(6) NOT NULL,
PRIMARY KEY (`distributorID`,`productID`),
FOREIGN KEY (`productID`) REFERENCES `Product` (`productID`) ON UPDATE CASCADE
);
INSERT INTO `Distributor` (`distributorID`,`password`, `productID`, `phone_number`, `email_address`, `commission`,
`house_number`, `street_name`, `city`, `pincode`) VALUES
('1','pwd12345', 1, '1234567890', 'dist1@example.com', 5.00, '10A', 'Oak Street', 'Mumbai', '400001'),
('2','pwd23456', 2, '2345678901', 'dist2@example.com', 7.00, '20B', 'Maple Street', 'Delhi', '110001'),
('1','pwd12345', 3, '1234567890', 'dist1@example.com', 5.00, '10A', 'Oak Street', 'Mumbai', '400001'),
('4','pwd45678', 4, '4567890123', 'dist4@example.com', 6.00, '40D', 'Cedar Street', 'Hyderabad', '500001'),
('5','pwd56789', 5, '5678901234', 'dist5@example.com', 8.50, '50E', 'Elm Street', 'Ahmedabad', '380001'),
('6','pwd67890', 1, '6789012345', 'dist6@example.com', 3.75, '60F', 'Birch Street', 'Chennai', '600001'),
('7','pwd78901', 2, '7890123456', 'dist7@example.com', 9.00, '70G', 'Willow Street', 'Kolkata', '700001'),
('8','pwd89012', 3, '8901234567', 'dist8@example.com', 2.50, '80H', 'Ash Street', 'Surat', '395007'),
('9','pwd90123', 4, '9012345678', 'dist9@example.com', 10.00, '90I', 'Beech Street', 'Pune', '411001'),
('10','pwd01234', 5, '0123456789', 'dist10@example.com', 4.25, '100J', 'Oak Street', 'Jaipur', '302001'),
('11','pwd12345', 1, '1234509876', 'dist11@example.com', 5.75, '110K', 'Maple Street', 'Lucknow', '226001'),
('12','pwd23456', 2, '2345609875', 'dist12@example.com', 7.25, '120L', 'Pine Street', 'Kanpur', '208001'),
('13','pwd34567', 3, '3456709874', 'dist13@example.com', 8.75, '130M', 'Cedar Street', 'Nagpur', '440001'),
('14','pwd45678', 4, '4567809873', 'dist14@example.com', 6.50, '140N', 'Elm Street', 'Indore', '452001'),
('15','pwd56789', 5, '5678909872', 'dist15@example.com', 9.25, '150O', 'Birch Street', 'Thane', '400601'),
('16','pwd67890', 1, '6789019871', 'dist16@example.com', 3.25, '160P', 'Willow Street', 'Bhopal', '462001'),
('17','pwd78901', 2, '7890129870', 'dist17@example.com', 2.75, '170Q', 'Ash Street', 'Visakhapatnam', '530001'),
('18','pwd89012', 3, '8901239879', 'dist18@example.com', 10.50, '180R', 'Beech Street', 'Patna', '800001'),
('19','pwd90123', 4, '9012349878', 'dist19@example.com', 11.00, '190S', 'Oak Street', 'Vadodara', '390001'),
('3','pwd01234', 5, '0123459877', 'dist03@example.com', 12.00, '200T', 'Maple Street', 'Ghaziabad', '201001');
CREATE TABLE `DeliveryPartner` (
`deliveryID` INT NOT NULL AUTO_INCREMENT,
`password` VARCHAR(20) NOT NULL,
`first_name` VARCHAR(100) NOT NULL,
`last_name` VARCHAR(100) NOT NULL,
`phone_number` CHAR(10) NOT NULL,
`vehicle_number` VARCHAR(10) NOT NULL,
`status` VARCHAR(20) DEFAULT 'Free',
`orderID` INT,
`pickup_house_number` VARCHAR(10) NOT NULL,
`pickup_street_name` VARCHAR(100) DEFAULT NULL,
`pickup_city` VARCHAR(100) NOT NULL,
`pickup_pincode` CHAR(6) NOT NULL,
`expected_arrival_time` DATETIME DEFAULT NULL,
`delivery_house_number` VARCHAR(10) NOT NULL,
`delivery_street_name` VARCHAR(100) DEFAULT NULL,
`delivery_city` VARCHAR(100) NOT NULL,
`delivery_pincode` CHAR(6) NOT NULL,
`deliveries_completed` INT DEFAULT 0,
`rating` INT DEFAULT NULL,
`salary` DECIMAL(9,2) NOT NULL,
PRIMARY KEY (`deliveryID`),
FOREIGN KEY (`orderID`) REFERENCES `Order` (`orderID`) ON UPDATE CASCADE
);
INSERT INTO `DeliveryPartner` (
`password`,
`first_name`,
`last_name`,
`phone_number`,
`vehicle_number`,
`status`,
`orderID`,
`pickup_house_number`,
`pickup_street_name`,
`pickup_city`,
`pickup_pincode`,
`expected_arrival_time`,
`delivery_house_number`,
`delivery_street_name`,
`delivery_city`,
`delivery_pincode`,
`deliveries_completed`,
`rating`,
`salary`
) VALUES
('pwd45678', 'Aakash', 'Sharma', '9833345678', 'UP14BN7564', 'Occupied', 1, '67', 'Indirapuram', 'Delhi', '110006',
DATE_ADD(NOW(), INTERVAL 30 MINUTE), '101', 'Vaishali', 'Delhi', '110005', 175, 5, 22000.00),
('pwd13579', 'Ankita', 'Roy', '9700013579', 'WB26Y2436', 'Free', NULL, '10', 'Salt Lake', 'Delhi', '110019', NULL, '27',
'New Town', 'Delhi', '110020', 220, 5, 20000.00),
('pwd67890', 'Vivek', 'Jain', '9855567890', 'KA01MN5678', 'Occupied', 2, '32', 'Jayanagar', 'Delhi', '110010',
DATE_ADD(NOW(), INTERVAL 30 MINUTE), '76', 'BTM Layout', 'Delhi', '110009', 180, 4, 22500.00),
('pwd35791', 'Neha', 'Bhatt', '9722235791', 'UK07CA1234', 'Free', NULL, '97', 'Rajpur Road', 'Delhi', '110023', NULL,
'43', 'Ballupur', 'Delhi', '110024', 245, 3, 21200.00),
('pwd89012', 'Karan', 'Patel', '9877789012', 'GJ01JK2345', 'Occupied', 3, '29', 'Satellite', 'Delhi', '110014',
DATE_ADD(NOW(), INTERVAL 30 MINUTE), '143', 'Maninagar', 'Delhi', '110013', 190, 5, 22000.00),
('pwd57913', 'Monika', 'Singhal', '9744457913', 'HR26DK8332', 'Free', NULL, '22', 'DLF Phase 3', 'Delhi', '110027',
NULL, '34', 'Sector 56', 'Delhi', '110028', 170, 4, 20800.00),
('pwd01234', 'Pranav', 'Mishra', '9899901234', 'MH04JK6789', 'Occupied', 4, '88', 'Vashi', 'Delhi', '110018',
DATE_ADD(NOW(), INTERVAL 30 MINUTE), '77', 'Kharghar', 'Delhi', '110017', 230, 5, 23000.00),
('pwd24680', 'Rohit', 'Verma', '9711124680', 'UP32HG8564', 'Free', NULL, '84', 'Hazratganj', 'Delhi', '110022', NULL,
'59', 'Gomti Nagar', 'Delhi', '110021', 195, 4, 20700.00),
('pwd46802', 'Saurabh', 'Nayak', '9733346802', 'OR05AC4567', 'Occupied', 5, '115', 'Sahid Nagar', 'Delhi', '110026',
DATE_ADD(NOW(), INTERVAL 30 MINUTE), '68', 'Khandagiri', 'Delhi', '110025', 180, 5, 21900.00),
('pwd68024', 'Aryan', 'Dutta', '9755568024', 'WB76E4098', 'Free', NULL, '31', 'Behala', 'Delhi', '110030', NULL, '85',
'Thakurpukur', 'Delhi', '110029', 225, 4, 22300.00);


-- INSERT INTO `Order` (username, status, order_amount, discount, date_order_placed) VALUES
-- ('rajPatel', 'Processing', 150.00, 0, '2024-02-10 10:00:00');

-- INSERT INTO `Billing` (`payment_mode`, `bill_amount`, `amount_donated`, `orderID`, `ngoId`) VALUES
-- ('Credit Card', 1500.00, 1000, 1, 1)