#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import Libraries
import pandas as pd
import sqlite3 as db


# In[2]:


conn = db.connect('sqlite.db')


# In[3]:


cn = conn.cursor()


# In[4]:


cn.execute("create table Movies(name varchar(50),lead_actor VARCHAR(50), lead_actress VARCHAR(50), year_of_release DATE, director_name VARCHAR(50))")


# In[5]:


cn.execute("SELECT name FROM sqlite_master WHERE type='table';")


# In[6]:


cn.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cn.fetchall())


# In[7]:


cn.execute("INSERT INTO Movies VALUES('Inception','Leonardo DiCaprio','Marion Cotillard','2010','Christopher Nolan')")
cn.execute("INSERT INTO Movies VALUES('Avatar','Sam Worthington','Zoe Saldaña','2009','James Cameron')")
cn.execute("INSERT INTO Movies VALUES('The Batman','Robert Pattinson','Zoë Kravitz','2022','Matt Reeves')")
cn.execute("INSERT INTO Movies VALUES('Spider-Man','Tobey Maguire','Kirsten Dunst','2002','Sam Raimi')")
cn.execute("INSERT INTO Movies VALUES('The Conjuring','Patrick Wilson','Vera Farmiga','2013','James Wan')")


# In[8]:


new_Movies = [('Dune','Timothée Chalamet', 'Zendaya', '2021', 'Denis Villeneuve')]
cn.executemany('INSERT INTO Movies VALUES(?,?,?,?,?)' , new_Movies)


# In[9]:


cn.execute("SELECT * FROM Movies;")
print(cn.fetchall())


# In[10]:


conn.commit()


# In[14]:


cn.close()
conn.close()


# In[16]:


conn = db.connect('sqlite.db')
df_Movies = pd.read_sql_query('SELECT * FROM Movies', conn)


# In[17]:


df_Movies


# In[19]:


conn = db.connect('sqlite.db')
df_Movies = pd.read_sql_query("SELECT * FROM Movies where lead_actor='Tobey Maguire'", conn)


# In[20]:


df_Movies


# In[21]:


conn.close()


# In[ ]:




