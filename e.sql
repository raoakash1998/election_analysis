
SELECT ac_name
from 
(SELECT election_year,ac_name,COUNT(party) cnt
FROM bihar
WHERE percent_votes>10.00
GROUP BY election_year,ac_name)
where cnt>=3
group by ac_name
having COUNT(cnt) >=4;
