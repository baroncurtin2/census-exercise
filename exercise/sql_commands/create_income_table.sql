-- create income table
-- contains median household income in a zipcode
CREATE TABLE IF NOT EXISTS income (
    id SERIAL UNIQUE,
    zip_code VARCHAR(5) NOT NULL,
    median_income INTEGER,
    PRIMARY KEY(id),
    CONSTRAINT fk_zipcode
        FOREIGN KEY(zip_code)
        REFERENCES zipcodes(zip_code)
        ON DELETE CASCADE
)