CREATE DATABASE IF NOT EXISTS glasstest;

USE glasstest;

CREATE TABLE IF NOT EXISTS glass (
    id INT AUTO_INCREMENT PRIMARY KEY,
    result LONGBLOB
);
