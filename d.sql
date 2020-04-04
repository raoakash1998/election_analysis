SELECT party,ac_name,min(votes) min_votes
FROM (
SELECT election_year,party,ac_name,votes
FROM bihar
WHERE election_year!="2015" AND party IN (SELECT party from 
(SELect election_year,party,votes
FROM 
(SELECT election_year,party,sum(votes) votes
FROM bihar
where party!="Independent"
GROUP BY party,election_year)
WHERE election_year="2015") ORDER BY votes DESC LIMIT 8)
)
GROUP BY party,ac_name;
