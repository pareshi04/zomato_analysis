#!/usr/bin/env python
# coding: utf-8

# # zomato data analysis

# In[23]:


# IMPORTING LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[24]:


df=pd.read_csv('zomato.csv',encoding='latin-1')


# In[25]:


df.head()


# In[26]:


df.columns
#name of columns


# In[27]:


df.info()
#to check null and datatype


# In[28]:


df.describe()
#statics


# In[29]:


df.shape
#no. of rows and columns


# # in data analysis what all things we do1.missing values 2.eda about numerical values 3.eda about categorical value 4.finding relationship between features
# 

# In[30]:


#to check null values
df.isnull().sum()


# In[31]:


# it is another technique to know which one has null value
[features for features in df.columns if df[features].isnull().sum()>0]


# In[32]:


# heat_map
#we are not able to see 9 as 9551 rows are their
sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[33]:


# another dataset that has country 
df_country=pd.read_excel('Country-Code.xlsx')
df_country.head()


# In[34]:


print("column names for domato dataframe")
print(df.columns)
print("**************************************")
print("column names for country dataframe")
print(df_country.columns)


# In[35]:


# to combine both the dataframe we can merge them using a common column
#the code for this is similar to that of mysql
final_df=pd.merge(df,df_country,on='Country Code',how='left')


# In[36]:


final_df.head()


# In[37]:


# to check datatypes
final_df.dtypes


# In[38]:


final_df.Country.value_counts()
#no. of records with respect to any column


# In[39]:


country_names=final_df.Country.value_counts().index


# In[40]:


country_names


# In[41]:


country_values=final_df.Country.value_counts().values


# In[42]:


country_values


# In[44]:


# to create a pie chart for top 3 countries and percentage
plt.pie(country_values[:3],labels=country_names[:3],autopct='%1.2f%%')


# observation:maximum transaction done is in india

# In[50]:


# it is used for grouping similar type of records together
final_df.groupby(['Aggregate rating','Rating color','Rating text']).size()


# In[48]:


final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index()


# In[53]:


ratings=final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating Count'})


# In[54]:


ratings


#  ## conclusion and observation
#  raitings:-
#     1)from 4.5to 4.9---->excellent
#     2)from 4.0 to 4.4---->very good
#     3)from 3.5 to 3.9---->good
#     and so on

# In[65]:


import matplotlib
matplotlib.rcParams["figure.figsize"]=(12,6)
sns.barplot(x="Aggregate rating",y="Rating Count",data=ratings)


# In[60]:


sns.barplot(x="Aggregate rating",y="Rating Count",hue='Rating color',data=ratings)


# In[67]:


#to map the colours
sns.barplot(x="Aggregate rating",y="Rating Count",palette=['white','red','orange','yellow','green','green'],data=ratings)


# In[70]:


## count plot
##on basis of colours
sns.countplot(x='Rating color',data=ratings,palette=['white','red','orange','yellow','green','green'])


# In[75]:


##countries name that has zero rating
final_df[final_df['Rating color']=='White'].groupby('Country').size().reset_index


# In[76]:


##another way
final_df.groupby(['Aggregate rating','Country']).size().reset_index().head(5)


# In[81]:


final_df.columns  


# In[80]:


#which currency is used by which country
final_df.groupby(['Currency','Country']).size().reset_index()


# In[82]:


##which countries do have online delivery
final_df.groupby(['Has Online delivery','Country']).size().reset_index()


# In[86]:


## create a pie chart for cities distribution
city_names=final_df.City.value_counts().index
city_values=final_df.City.value_counts().values
plt.pie(city_values[:4],labels=city_names[:4],autopct='%1.2f%%')


# In[87]:


## top 10 cuisines
Cuisines_names=final_df.Cuisines.value_counts().index
Cuisines_values=final_df.Cuisines.value_counts().values
plt.pie(Cuisines_values[:10],labels=Cuisines_names[:10],autopct='%1.2f%%')


# In[ ]:




