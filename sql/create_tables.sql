-- create_tables.sql

USE DataProcessingDB;

-- Create CUST_MSTR table
CREATE TABLE CUST_MSTR (
    ID INT PRIMARY KEY,
    Name NVARCHAR(100),
    Date DATE
);

-- Create master_child table
CREATE TABLE master_child (
    ID INT PRIMARY KEY,
    Name NVARCHAR(100),
    Date DATE,
    DateKey INT
);

-- Create H_ECOM_Orders table
CREATE TABLE H_ECOM_Orders (
    OrderID INT PRIMARY KEY,
    ProductName NVARCHAR(100),
    Quantity INT,
    Price DECIMAL(18, 2)
);
