#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("casestudy.csv")


# In[3]:


#df


# In[4]:


df_2015=df[df['year']==2015]


# In[5]:


df_2016=df[df['year']==2016]


# In[6]:


df_2017=df[df['year']==2017]


# In[62]:


df_2015.shape


# In[8]:


#for 2015

#total revenue of current year

df_2015['net_revenue'].sum()


# In[9]:


#for 2016
#total revenue of current year

df_2016['net_revenue'].sum()


# In[10]:


#for 2017

#total revenue of current year

df_2017['net_revenue'].sum()


# In[11]:


df_2016


# In[12]:


#new customer revenue will be same as total revenue for 2015 year


# In[13]:


#new customer revenue for 2016
import numpy as np
new_cust_2016=df_2016[~df_2016['customer_email'].isin(df_2015['customer_email'])]
new_cust_2016['net_revenue'].sum()


# In[65]:


#new customer revenue for 2017
new_cust_2017=df_2017[~df_2017['customer_email'].isin(df_2016['customer_email'])]
new_cust_2017['net_revenue'].sum()


# In[15]:


#existing customer growth for 2015 will be same as net_revenue

Revenue of existing customers for current year – Revenue of existing customers from the previous year

# In[63]:


#existing customer growth for 2016
old_cust_in_2016=df_2016[~df_2016['customer_email'].isin(new_cust_2016['customer_email'])]


new=new_cust_2016.net_revenue.sum()

df_2016.net_revenue.sum()-new


# In[17]:


#existing customer growth for 2017


# In[64]:


old_cust_in_2017=df_2017[~df_2017['customer_email'].isin(new_cust_2017['customer_email'])]


new=new_cust_2017.net_revenue.sum()

df_2017.net_revenue.sum()-new


# In[19]:


#revenue lost 


# In[20]:


#revenue lost attriion in 2016
x=df_2015[~df_2015['customer_email'].isin(old_cust_in_2016['customer_email'])]
df_2015[~df_2015['customer_email'].isin(old_cust_in_2016['customer_email'])].net_revenue.sum()


# In[21]:


x.shape[0]


# In[22]:


#revenue lost attriion in 2017
y=df_2016[~df_2016['customer_email'].isin(old_cust_in_2017['customer_email'])]
df_2016[~df_2016['customer_email'].isin(old_cust_in_2017['customer_email'])].net_revenue.sum()


# In[ ]:





# In[ ]:





# In[23]:


#existing customer revenue current year and prior year


# In[24]:


df_2015.net_revenue.sum()


# In[25]:


df_2016.net_revenue.sum()


# In[26]:


df_2017.net_revenue.sum()


# In[ ]:





# In[27]:


#total customers


# In[28]:


df_2015.shape[0]


# In[29]:


df_2016.shape[0]


# In[30]:


df_2017.shape[0]


# In[ ]:





# In[31]:


#new customers 


# In[32]:


new_cust_2016.shape[0]


# In[33]:


new_cust_2017.shape[0]


# In[ ]:





# In[34]:


#lost customers


# In[35]:


x.shape[0] #in 2016


# In[36]:


y.shape[0] #in 2017


# In[ ]:





# In[37]:


p=df_2016[df_2016['customer_email'].isin(df_2015['customer_email'])]


# In[38]:


q=df_2017[df_2017['customer_email'].isin(df_2016['customer_email'])]


# In[39]:


df_merged = pd.merge(p, q, how='inner',left_on="customer_email",right_on="customer_email")


# In[40]:


df_merged.shape[0]


# In[41]:


df_2015.shape[0]


# In[49]:


231294-6162


# In[42]:


import matplotlib.pyplot as plt
labels = 'Yes','No'
sizes = [6162,225132]
explode = (0.1,0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=180)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Customers who are present from 2015 to 2017")
plt.show()


# In[ ]:





# In[43]:


#how many customers came back after leaving company
#ex. 2015 ma hoi, 2016 ma no hoi and 2017 ma pa6a ayva hooi


# In[44]:


b=new_cust_2017[new_cust_2017['customer_email'].isin(df_2015['customer_email'])]
b.shape[0]

who came back=766
who didnt=170944
# In[61]:


import matplotlib.pyplot as plt
data = [766, 170944]
label = ['Came back', 'didnt']

plt.pie(data, labels=label, autopct='%1.1f%%', explode=[0.1,0], shadow=True, startangle=180)
plt.title('Customers who came back to company in 2017')
plt.axis('equal')
plt.show()


# In[ ]:





# In[46]:


b.net_revenue.sum()


# In[47]:


df_2017.net_revenue.sum()


# In[ ]:




