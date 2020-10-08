-- thresholds taken from the below website
-- https://aspe.hhs.gov/poverty-guidelines

CREATE TABLE IF NOT EXISTS poverty_thresholds (
    id INTEGER UNIQUE PRIMARY KEY,
    household_size INTEGER NOT NULL,
    guideline INTEGER NOT NULL,
    state VARCHAR(10) NOT NULL
)