-- create population table
-- contains population in a zipcode
CREATE TABLE IF NOT EXISTS population (
    id SERIAL UNIQUE,
    zip_code VARCHAR(5) NOT NULL,
    population INTEGER,
    PRIMARY KEY(id),
    CONSTRAINT fk_zipcode
        FOREIGN KEY(zip_code)
        REFERENCES zipcodes(zip_code)
        ON DELETE CASCADE
)