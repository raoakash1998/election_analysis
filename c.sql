CREATE TABLE a1 AS
SELECT election_year,party,sum(votes) votes
FROM bihar
where party!="Independent"
GROUP BY party,election_year;

CREATE TABLE one AS
SELect election_year,party,votes
FROM a1
WHERE election_year="2015";

CREATE TABLE two AS
SELect election_year,party,votes
FROM a1
WHERE election_year="2010";
CREATE TABLE three AS
SELect election_year,party,votes
FROM a1
WHERE election_year="2005-Feb";
CREATE TABLE four AS
SELect election_year,party,votes
FROM a1
WHERE election_year="2005-Oct";

CREATE TABLE onet AS SElECT election_year,party FROM one ORDER BY votes DESC LIMIT 8;
CREATE TABLE twot AS SElECT election_year,party FROM two ORDER BY votes DESC LIMIT 8;
CREATE TABLE threet AS SElECT election_year,party FROM three ORDER BY votes DESC LIMIT 8;
CREATE TABLE fourt AS SElECT election_year,party FROM four ORDER BY votes DESC LIMIT 8;
INSERT INTO twot SELECT * FROM onet;
INSERT INTO twot SELECT * FROM threet;
INSERT INTO twot SELECT * FROM fourt;
SELECT * FROM twot;
