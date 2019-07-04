
# coding: utf-8

# # Converting Dataset into data frame

# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')

#imports
import numpy as np



# read csv in a data frame
df=pd.read_csv("Desktop/juypter/house_data.csv", sep=",")
df


# In[23]:


df.columns


# # Feature Columns

# In[10]:


df.head(3)


# In[11]:


df. tail(2)


# In[13]:


str(df)

