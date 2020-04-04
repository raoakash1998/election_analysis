CREATE TABLE var AS
SELECT election_year,ac_name,percent_votes
FROM bihar
WHERE position=1;

CREATE TABLE var2 AS
SELECT election_year,ac_name,percent_votes
FROM bihar
WHERE position=2;

SELECT var3.ac_name
FROM(SELECT var.election_year,var.ac_name, abs(var.percent_votes - var2.percent_votes) diff
FROM var,var2
WHERE var.election_year=var2.election_year AND var.ac_name = var2.ac_name) var3
where var3.diff<10.00 ;
