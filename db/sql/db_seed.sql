/*
Dev DB Seeding Data

Seeding data for local development. 


Author: Matthew Sunner, 2022
*/

INSERT INTO users (first_name, last_name, user_name, email, user_pw)
VALUES
    -- Passwords in seeding data are not sufficient for proudction
    -- These passwords are not used in any production setting. They
    -- are only for seeding data to work in development.
    ('Matthew', 'Sunner', 'msunner', 'msunner@me.com', 'rootpw!'),
    ('Jane', 'Doe', 'jdoe', 'jdoe@me.com', 'rootpw33!');


INSERT INTO todos (title, task_description, due_date, priority)
VALUES
    ('Go get milk', 'run to the store and pick up milk', '', 'LOW'),
    ('Get birth certificate', '', '', 'MEDIUM'),
    ('Go on a walk', 'Check out the new nature trail', '', ''),
    ('Pick up the cat', 'Cat is at the vet. Get her.', '', 'HIGH');