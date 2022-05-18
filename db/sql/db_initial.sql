/*
Dev Database Schema and Table Initialization 

Author: Matthew Sunner, 2022
*/

DROP TABLE IF EXISTS todos
DROP TABLE IF EXISTS users


CREATE TABLE todos (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL, 
    task_description TEXT,
    due_date INTEGER, 
    priority TEXT
);


CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    user_name TEXT NOT NULL,
    email TEXT NOT NULL,
    user_pw TEXT NOT NULL
);