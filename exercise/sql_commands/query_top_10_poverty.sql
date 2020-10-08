SELECT		*
FROM		poverty_rates
WHERE		median_income > 0
ORDER BY	poverty_rate DESC
LIMIT 10