"""
Q1
SELECT 
	DISTINCT
	p.name,
	c.name
FROM
	professor p
LEFT JOIN
	schedule s
ON p.id = s.professor_id
LEFT JOIN
	course c
ON s.course_id = c.id
WHERE p.department_id <> c.department_id
"""


"""
Q2
SELECT ROUND(SUM(TIV_2012),2)
	FROM
	INSURANCE ins
	JOIN
		(
		SELECT DISTINCT 
			LAT,
			LON,
			TIV_2011
		FROM INSURANCE t1
		LEFT JOIN
			(
			SELECT 
				TIV_2011,
				COUNT(*)
			FROM INSURNACE
			GROUP BY TIV_2011
			HAVING COUNT(*) > 1
			) t2
		ON t1.TIV_2011 = t2.TIV_2011
		WHERE t2.TIV_2011 IS NOT NULL
		) filter
	ON ins.TIV_2011=filter.TIV_2011
	AND ins.LAT=filter.LAT
	AND ins.LON=filter.LON

"""


##long_distance_2.py
def longest_distance(test_list):
	largest_d = 0
	for i in test_list:		
		for j in test_list:
			if j > i and (j-i) > largest_d:
				largest_d = j-i
	return largest_d

test_list = [30, 41, 4, 15, 81, 71]
print(longest_distance(test_list))


"""
Q1 - 1, 2 , 3
Q2 - 2 
Q3 - 3 and 4 
Q4 - 321
""