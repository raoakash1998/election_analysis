SELECT ac_name
FROM(SELECT ac_name,COUNT(DISTINCT party) cnt2
FROM (
SELECT election_year,ac_name,party
FROM bihar
WHERE position=1)
GROUP BY ac_name) cur2
WHERE cur2.cnt2=1;
