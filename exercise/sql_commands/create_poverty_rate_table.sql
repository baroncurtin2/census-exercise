-- joins all tables and adds new column for poverty rate

CREATE TABLE IF NOT EXISTS poverty_rates (
    id SERIAL UNIQUE,
    zip_code VARCHAR(5) NOT NULL,
    median_income INTEGER,
    population INTEGER,
    poverty_population INTEGER,
    poverty_rate DECIMAL,
    PRIMARY KEY(id),
    CONSTRAINT fk_zipcode
        FOREIGN KEY(zip_code)
        REFERENCES zipcodes(zip_code)
        ON DELETE CASCADE
)