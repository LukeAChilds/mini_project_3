CREATE TABLE product (
    name TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL,
    code TEXT PRIMARY KEY
);
CREATE INDEX code_index ON product(code);
