CREATE DATABASE SmartGarbage;
USE SmartGarbage;

CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(60),
    phone_no VARCHAR(15),
    password VARCHAR(60) NOT NULL,
    address VARCHAR(100)
);
ALTER TABLE users MODIFY id INT AUTO_INCREMENT;


CREATE TABLE collector (
    id INT PRIMARY KEY,
    name VARCHAR(60),
    phone_no VARCHAR(15),
    password VARCHAR(60) NOT NULL,
    vehicle_no VARCHAR(20),
    area VARCHAR(100),
    isActive BOOLEAN DEFAULT TRUE,
    total_collected INT DEFAULT 0,
    createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    lastActive DATETIME NULL
);



CREATE TABLE report (
    id VARCHAR(24) PRIMARY KEY,
    userId VARCHAR(24),
    userName VARCHAR(100),
    userPhone VARCHAR(20),
    userAddress VARCHAR(255),
    photoUrl VARCHAR(255),
    description VARCHAR(255),
    status VARCHAR(50),
    priority VARCHAR(50),
    createdAt DATETIME,
    assignedAt DATETIME,
    collectorId VARCHAR(24),
    collectorName VARCHAR(100),
    collectedAt DATETIME,
    location JSON
);



