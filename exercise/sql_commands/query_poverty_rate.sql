INSERT INTO poverty_rates (zip_code, median_income, population, poverty_population, poverty_rate)
SELECT      i.zip_code,
            i.median_income,
            p.population,
            pv.population AS poverty_population,
            CAST(pv.population AS DECIMAL) / CAST((CASE WHEN p.population = 0 THEN 1 ELSE p.population END) AS DECIMAL)
                AS poverty_rate
FROM        income i
INNER JOIN  population p
            ON i.zip_code = p.zip_code
INNER JOIN  poverty pv
            ON i.zip_code = pv.zip_code