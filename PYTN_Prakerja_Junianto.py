#!/usr/bin/env python
# coding: utf-8

# In[26]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from scipy import stats
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
 
dataset = pd.read_csv(r"E:/heart.csv") 
dataset.info() 
dataset.describe() 
dataset = pd.get_dummies(dataset, columns = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']) 
standardScaler = StandardScaler() 
columns_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak'] 


# In[ ]:





# 

# In[25]:


dataset.describe()


# In[ ]:




