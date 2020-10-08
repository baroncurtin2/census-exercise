-- create zipcodes table
CREATE TABLE IF NOT EXISTS zipcodes (
    id SERIAL UNIQUE,
    zip_code VARCHAR(5) NOT NULL UNIQUE,
    PRIMARY KEY(id)
)