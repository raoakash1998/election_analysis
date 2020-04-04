SELECT ac_name
FROM(
	SELECT ac_name,COUNT(DISTINCT party) cnt
	FROM(
  		SELECT election_year,ac_name,party
		FROM bihar
		where position=1)
	GROUP BY ac_name)
WHERE cnt=4;
