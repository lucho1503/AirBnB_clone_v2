-- this script prepare a new server MYSQL

CREATE DATABASE IF NOT EXISTS hbnb_test_db
       CHARSET utf8mb4
       COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
