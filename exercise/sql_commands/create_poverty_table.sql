-- create poverty table
-- contains population below poverty line

CREATE TABLE IF NOT EXISTS poverty (
    id SERIAL UNIQUE,
    zip_code VARCHAR(5) NOT NULL,
    population INTEGER,
    PRIMARY KEY(id),
    CONSTRAINT fk_zipcode
        FOREIGN KEY(zip_code)
        REFERENCES zipcodes(zip_code)
        ON DELETE CASCADE
)