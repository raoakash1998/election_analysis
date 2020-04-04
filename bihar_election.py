#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sqlite3


# In[2]:


bihar_election=pd.read_csv("Bihar_Election_Results.csv")


# In[3]:


bihar_election.columns=['Election_Year','Position','Name','Votes','Percent_Votes','Party','AC_name','AC_no']
bihar_election;


# In[4]:


for i, row_value in bihar_election['Percent_Votes'].iteritems():
    row_value = str(row_value)
    row_value = row_value.replace('%','')
    bihar_election.at[i,'Percent_Votes']= row_value


# In[5]:


for columns in list(bihar_election.columns.values):
    bihar_election[columns] = pd.to_numeric(bihar_election[columns],errors='ignore')


# In[6]:


con = sqlite3.connect('bihar.db')
c = con.cursor()
bihar_election.to_sql('bihar',con,if_exists='append', index=False)
cursorObj = con.cursor()


# In[7]:


from IPython.display import Markdown, display
def printmd(string):
    display(Markdown(string))
#printmd('**bold**')


# In[8]:


#printmd("**('Election_Year','Position','Name','Votes','Percent_Votes','Party','AC_name','AC_no')**")
# def scriptexecution(filename):
 #   with open(filename, 'r') as s:
  #      sql_script = s.read()
   #     cursorObj.execute(sql_script)
    #s.closed
 
#scriptexecution('a.sql')
#A
cursorObj.execute('CREATE TABLE my AS SELECT election_year,party,sum(votes) votes FROM bihar where party!="Independent" GROUP BY party,election_year;')
cursorObj.execute('SELECT election_year,party,votes FROM my AS t where votes = (SELECT max(votes) FROM my WHERE t.election_year=election_year);')
rows = cursorObj.fetchall()
printmd("**('Election_Year ',' Party ',' Votes')**")
for row in rows:
    print(row)

cursorObj.execute('DROP TABLE my;')


# In[9]:


#B
cursorObj.execute('SELECT ac_name FROM( SELECT ac_name,COUNT(DISTINCT party) cnt FROM( SELECT election_year,ac_name,party FROM bihar where position=1) GROUP BY ac_name) WHERE cnt=4;')

rows = cursorObj.fetchall()
printmd("**('Election_Year ',' Party ')**")
for row in rows:
    print(row)


# In[10]:


#C
cursorObj.execute('CREATE TABLE a1 AS SELECT election_year,party,sum(votes) votes FROM bihar where party!="Independent" GROUP BY party,election_year;')
cursorObj.execute('CREATE TABLE one AS SELect election_year,party,votes FROM a1 WHERE election_year="2015";')
cursorObj.execute('CREATE TABLE two AS SELect election_year,party,votes FROM a1 WHERE election_year="2010";')
cursorObj.execute('CREATE TABLE three AS SELect election_year,party,votes FROM a1 WHERE election_year="2005-Feb";')
cursorObj.execute('CREATE TABLE four AS SELect election_year,party,votes FROM a1 WHERE election_year="2005-Oct";')
cursorObj.execute('CREATE TABLE onet AS SElECT election_year,party FROM one ORDER BY votes DESC LIMIT 8;')
cursorObj.execute('CREATE TABLE twot AS SElECT election_year,party FROM two ORDER BY votes DESC LIMIT 8;')
cursorObj.execute('CREATE TABLE threet AS SElECT election_year,party FROM three ORDER BY votes DESC LIMIT 8;')
cursorObj.execute('CREATE TABLE fourt AS SElECT election_year,party FROM four ORDER BY votes DESC LIMIT 8;')
cursorObj.execute('INSERT INTO twot SELECT * FROM onet;')
cursorObj.execute('INSERT INTO twot SELECT * FROM threet;')
cursorObj.execute('INSERT INTO twot SELECT * FROM fourt;')
cursorObj.execute('SELECT * FROM twot;')
rows = cursorObj.fetchall()
printmd("**('Election_Year ',' Party ')**")
for row in rows:
    print(row)
    
cursorObj.execute("DROP TABLE a1;")
cursorObj.execute('DROP TABLE one;')
cursorObj.execute('DROP TABLE two;')
cursorObj.execute('DROP TABLE three;')
cursorObj.execute('DROP TABLE four;')
cursorObj.execute('DROP TABLE onet;')
cursorObj.execute('DROP TABLE twot;')
cursorObj.execute('DROP TABLE threet;')
cursorObj.execute('DROP TABLE fourt;')


# In[11]:


#D    
cursorObj.execute('CREATE TABLE a1 AS SELECT election_year,party,sum(votes) votes FROM bihar where party!="Independent" GROUP BY party,election_year;')
cursorObj.execute('CREATE TABLE one AS SELect election_year,party,votes FROM a1 WHERE election_year="2015";')
cursorObj.execute('CREATE TABLE onet AS SELECT party FROM one ORDER BY votes DESC LIMIT 8;')
cursorObj.execute('SELECT party,ac_name,min(votes) min_votes FROM ( SELECT election_year,party,ac_name,votes FROM bihar WHERE election_year!="2015" AND party IN (SELECT party from onet) ) GROUP BY party,ac_name;')
rows = cursorObj.fetchall()
printmd("**(' Party ',' AC_name' ,' Votes')**")
for row in rows:
    print(row)

cursorObj.execute('DROP TABLE a1;')
cursorObj.execute('DROP TABLE one;')
cursorObj.execute('DROP TABLE onet;')


# In[12]:


#E    
cursorObj.execute('CREATE TABLE temm as SELECT election_year,ac_name,COUNT(party) cnt FROM bihar WHERE percent_votes>10.00 GROUP BY election_year,ac_name;')
cursorObj.execute('SELECT ac_name from temm where cnt>=3 group by ac_name having COUNT(cnt) >=4;')
rows = cursorObj.fetchall()
printmd("**(' AC_name')**")
for row in rows:
    print(row)

cursorObj.execute('DROP TABLE temm;')


# In[13]:


#F   
cursorObj.execute('CREATE TABLE cur AS SELECT election_year,ac_name,party FROM bihar WHERE position=1;')
cursorObj.execute('SELECT ac_name FROM(SELECT ac_name,COUNT(DISTINCT party) cnt2 FROM cur GROUP BY ac_name) cur2 WHERE cur2.cnt2=1;')
rows = cursorObj.fetchall()
printmd("**(' AC_name')**")
for row in rows:
    print(row)

cursorObj.execute('DROP TABLE cur;')


# In[14]:


#G
cursorObj.execute('CREATE TABLE var AS SELECT election_year,ac_name,percent_votes FROM bihar WHERE position=1;')
cursorObj.execute('CREATE TABLE var2 AS SELECT election_year,ac_name,percent_votes FROM bihar WHERE position=2;')
cursorObj.execute('SELECT var3.ac_name FROM(SELECT var.election_year,var.ac_name, abs(var.percent_votes - var2.percent_votes) diff FROM var,var2 WHERE var.election_year=var2.election_year AND var.ac_name = var2.ac_name) var3 where var3.diff<10.00 ;')

rows = cursorObj.fetchall()
printmd("**(' AC_name')**")
for row in rows:
    print(row)
    
cursorObj.execute('DROP TABLE var;')
cursorObj.execute('DROP TABLE var2;')


# In[15]:


#H
cursorObj.execute('CREATE TABLE a1 AS SELECT election_year,party,sum(votes) votes FROM bihar where party!="Independent" GROUP BY party,election_year;')
cursorObj.execute('CREATE TABLE one AS SELect election_year,party,votes FROM a1 WHERE election_year="2005-Feb";')
cursorObj.execute('CREATE TABLE onet AS SELECT party FROM one ORDER BY votes DESC LIMIT 8;')
cursorObj.execute('CREATE TABLE first AS SELECT ac_name,party,votes FROM bihar WHERE election_year = "2005-Feb" AND party in ( SELECT party FROM onet);')
cursorObj.execute('CREATE TABLE second AS SELECT ac_name,party,votes FROM bihar WHERE election_year = "2005-Oct" AND party in ( SELECT party FROM onet);')
cursorObj.execute('CREATE TABLE third AS SELECT ac_name,party,votes FROM bihar WHERE election_year = "2010" AND party in ( SELECT party FROM onet);')
cursorObj.execute('CREATE TABLE fourth AS SELECT ac_name,party,votes FROM bihar WHERE election_year = "2015" AND party in ( SELECT party FROM onet); ')
cursorObj.execute('CREATE TABLE second2 AS SELECT second.ac_name,second.party,second.votes FROM first,second WHERE first.ac_name=second.ac_name AND first.party = second.party AND first.votes<second.votes ;')
cursorObj.execute('CREATE TABLE third2 AS SELECT third.ac_name,third.party,third.votes FROM second2,third WHERE second2.ac_name=third.ac_name AND second2.party = third.party AND second2.votes<third.votes ;')
cursorObj.execute('SELECT fourth.party,fourth.ac_name FROM third2,fourth WHERE third2.ac_name=fourth.ac_name AND third2.party = fourth.party AND third2.votes<fourth.votes ;')

rows = cursorObj.fetchall()
printmd("**(' Party ',' AC_name')**")
for row in rows:
    print(row)

cursorObj.execute('DROP TABLE a1;')
cursorObj.execute('DROP TABLE one;')
cursorObj.execute('DROP TABLE onet;')
cursorObj.execute('DROP TABLE first;')
cursorObj.execute('DROP TABLE second;')
cursorObj.execute('DROP TABLE third;')
cursorObj.execute('DROP TABLE fourth;')
cursorObj.execute('DROP TABLE second2;')
cursorObj.execute('DROP TABLE third2;')


# In[16]:


#I
cursorObj.execute('CREATE TABLE a1 AS SELECT election_year,party,sum(votes) votes FROM bihar where party!="Independent" GROUP BY party,election_year;')
cursorObj.execute('CREATE TABLE one AS SELect election_year,party,votes FROM a1 WHERE election_year="2005-Feb";')
cursorObj.execute('CREATE TABLE onet AS SELECT party FROM one ORDER BY votes DESC LIMIT 8;')
cursorObj.execute('CREATE TABLE first AS SELECT ac_name,party,votes FROM bihar WHERE election_year = "2005-Feb" AND party in ( SELECT party FROM onet);')
cursorObj.execute('CREATE TABLE second AS SELECT ac_name,party,votes FROM bihar WHERE election_year = "2005-Oct" AND party in ( SELECT party FROM onet);')
cursorObj.execute('CREATE TABLE third AS SELECT ac_name,party,votes FROM bihar WHERE election_year = "2010" AND party in ( SELECT party FROM onet);')
cursorObj.execute('CREATE TABLE fourth AS SELECT ac_name,party,votes FROM bihar WHERE election_year = "2015" AND party in ( SELECT party FROM onet);')
cursorObj.execute('CREATE TABLE second2 AS SELECT second.ac_name,second.party,second.votes FROM first,second WHERE first.ac_name=second.ac_name AND first.party = second.party AND first.votes>second.votes ; ')
cursorObj.execute('CREATE TABLE third2 AS SELECT third.ac_name,third.party,third.votes FROM second2,third WHERE second2.ac_name=third.ac_name AND second2.party = third.party AND second2.votes>third.votes ; ')
cursorObj.execute('SELECT fourth.party,fourth.ac_name FROM third2,fourth WHERE third2.ac_name=fourth.ac_name AND third2.party = fourth.party AND third2.votes>fourth.votes ;')

rows = cursorObj.fetchall()
printmd("**(' Party ',' AC_name')**")
for row in rows:
    print(row)

cursorObj.execute('DROP TABLE a1;')
cursorObj.execute('DROP TABLE one;')
cursorObj.execute('DROP TABLE onet;')
cursorObj.execute('DROP TABLE first;')
cursorObj.execute('DROP TABLE second;')
cursorObj.execute('DROP TABLE third;')
cursorObj.execute('DROP TABLE fourth;')
cursorObj.execute('DROP TABLE second2;')
cursorObj.execute('DROP TABLE third2;')


# In[17]:


#J
cursorObj.execute('CREATE TABLE my AS SELECT election_year,party,sum(votes) votes FROM bihar where party!="Independent" GROUP BY party,election_year;')
cursorObj.execute('CREATE TABLE state_winners as SELECT election_year,party FROM my AS t where votes = (SELECT max(votes) FROM my WHERE t.election_year=election_year);')
cursorObj.execute('CREATE TABLE ac_winners AS SELECT election_year,ac_name,party FROM bihar WHERE position=1;')
cursorObj.execute('CREATE table tot as SELECT ac_winners.election_year,ac_winners.ac_name FROM ac_winners,state_winners WHERE ac_winners.election_year=state_winners.election_year AND ac_winners.party=state_winners.party;')
cursorObj.execute('SELECT ac_name FROM tot GROUP BY ac_name having count(DISTINCT election_year)=4; ')

rows = cursorObj.fetchall()
printmd("**('AC_name ')**")
for row in rows:
    print(row)

cursorObj.execute('DROP TABLE my;')
cursorObj.execute('DROP TABLE state_winners;')
cursorObj.execute('DROP TABLE ac_winners;')
cursorObj.execute('DROP TABLE tot;')


# In[ ]:




