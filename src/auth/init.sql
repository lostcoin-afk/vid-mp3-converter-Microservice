-- create user 'auth_user'@'localhost' identified by 'Aauth123';

-- create database auth;
-- grant all privileges on auth.* to 'auth_user'@'localhost';

-- use auth;

-- create table user(
--     id int not null AUTO_INCREMENT primary key,
--     email varchar(255) not null,
--     password varchar(255) not null
-- );

-- insert into user (email, password) values ('admin@gmail.com', 'admin');

CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'Aauth123';
CREATE DATABASE auth;
GRANT ALL PRIVILEGES ON auth.* TO 'auth_user'@'localhost';

USE auth;

CREATE TABLE user(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO user (email, password) VALUES ('admin@gmail.com', 'admin');


-- #check db fro username and pasqword