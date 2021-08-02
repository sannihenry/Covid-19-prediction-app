#!/usr/bin/env python
# coding: utf-8

# In[1]:


##Dataset Link: https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data
import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv('data/Henry_computed2.csv')


# In[3]:


df


# In[4]:


### Independent and Dependent features
X=df.iloc[:,:-1]
y=df.iloc[:,-1]


# In[5]:


X.head()


# In[6]:


y.head(20)


# In[7]:


### Train Test Split
from sklearn.model_selection import train_test_split


# In[8]:


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)


# In[9]:


### Implement Random Forest classifier
from sklearn.ensemble import RandomForestClassifier
classifier=RandomForestClassifier()
classifier.fit(X_train,y_train)


# In[10]:


## Prediction
y_pred=classifier.predict(X_test)


# In[11]:


### Check Accuracy
from sklearn.metrics import accuracy_score
score=accuracy_score(y_test,y_pred)


# In[12]:


score


# In[13]:


### Create a Pickle file using serialization 
import pickle
pickle_out = open("classifier.pkl","wb")
pickle.dump(classifier, pickle_out)
pickle_out.close()


# In[14]:


import numpy as np


# In[15]:


classifier.predict([[1,2,3,4,1,12,34,44]])


# In[ ]:




