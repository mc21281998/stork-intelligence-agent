-- 本福特定律 (Benford's Law) SQL 检测示例
WITH FirstDigits AS (
    SELECT CAST(SUBSTR(CAST(revenue AS TEXT), 1, 1) AS INTEGER) AS first_digit
    FROM financial_statements
    WHERE revenue IS NOT NULL AND revenue > 0
),
DigitCounts AS (
    SELECT first_digit, COUNT(*) AS digit_count
    FROM FirstDigits GROUP BY first_digit
),
TotalCount AS (
    SELECT COUNT(*) as total FROM FirstDigits
)
SELECT
    dc.first_digit,
    dc.digit_count,
    ROUND(CAST(dc.digit_count AS REAL) * 100 / tc.total, 2) AS actual_percentage,
    CASE dc.first_digit
        WHEN 1 THEN 30.1 WHEN 2 THEN 17.6 WHEN 3 THEN 12.5 WHEN 4 THEN 9.7
        WHEN 5 THEN 7.9 WHEN 6 THEN 6.7 WHEN 7 THEN 5.8 WHEN 8 THEN 5.1
        WHEN 9 THEN 4.6 ELSE 0
    END AS benford_percentage
FROM DigitCounts dc, TotalCount tc
WHERE dc.first_digit BETWEEN 1 AND 9 ORDER BY dc.first_digit;
