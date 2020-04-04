SELECT election_year,party,votes
FROM (SELECT election_year,party,sum(votes) votes
FROM bihar
where party!="Independent"
GROUP BY party,election_year) AS t
where votes = (SELECT max(votes) FROM (SELECT election_year,party,sum(votes) votes
FROM bihar
where party!="Independent"
GROUP BY party,election_year) WHERE t.election_year=election_year);
