
# coding: utf-8

# # Converting Dataset into data frame

# In[4]:


#to see graph in juypter notebook
get_ipython().run_line_magic('matplotlib', 'inline')

#imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns #works with matplot library
from sklearn import linear_model
from scipy import stats
from scipy.stats import norm




# read csv in a data frame
#and extracting dependent and independent variables
df=pd.read_csv("Desktop/juypter/house_data.csv", sep=",")
df
X=df.iloc[:,:-1].values
Y=df.iloc[:, 2].values
df.head()


# In[10]:


df.columns


# In[22]:


df.head(3)


# In[23]:


df. tail(2)


# In[8]:


df.info()


# In[9]:


str(df)


# In[10]:


df.shape


# In[11]:


##only numeric columns
df.describe()


# In[25]:


sns.pairplot(df, x_vars='sqft_living', y_vars='price', kind='reg')


# In[23]:


#linear regression for single variable
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.xlabel('grade')
plt.ylabel('price')
plt.scatter(df.grade, df.price)


# In[24]:


#data visualization  and building correlation matrix
sns.heatmap(df.corr())


# In[22]:


#splitting dataset into train set and test set
#from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state= 0)


# In[13]:


#fitting linear regression to the training set
#from sklearn.linear_model import LinearRegression
#regressor= LinearRegression()
#regressor.fit(X_train, y_train)

