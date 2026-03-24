-- Phone Book Database Schema
CREATE TABLE IF NOT EXISTS Contacts (
    Name            VARCHAR(225) NOT NULL,
    PhoneNumber     VARCHAR(50) NOT NULL UNIQUE,
    City            VARCHAR(255),
    State           VARCHAR(10),
    Address         VARCHAR(255),
    PRIMARY KEY (PhoneNumber)
);
