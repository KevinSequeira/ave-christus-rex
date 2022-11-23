
WITH RECURSIVE
-- Define a CTE to hold the recursive output
rDateDimensionMinute (CalendarDateInterval)
AS
    (
        -- The anchor of the recursion is the start date of the date dimension
        SELECT DATE('2022-11-01')
        UNION ALL
        -- The recursive query increments the time interval by the desired amount
        -- This can be any time increment (monthly, daily, hours, minutes)
        SELECT DATE(CalendarDateInterval, '+24 hour') FROM rDateDimensionMinute
        -- Set the number of recursions
        -- Functionally, this is the number of periods in the date dimension
        LIMIT 100000
    )
-- Output the result set to the permanent table
SELECT CalendarDateInterval,
	CASE
		CAST (STRFTIME('%w', CalendarDateInterval) as integer) + 1
		WHEN 1 THEN 'sunday'
		WHEN 2 THEN 'monday'
		WHEN 3 THEN 'tuesday'
		WHEN 4 THEN 'wednesday'
		WHEN 5 THEN 'thursday'
		WHEN 6 THEN 'friday'
		ELSE 'saturday'
		END AS Weekday
FROM rDateDimensionMinute