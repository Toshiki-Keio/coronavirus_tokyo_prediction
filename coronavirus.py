#!/usr/bin/env python
# coding: utf-8

# In[52]:
import japanize_matplotlib
import pandas as pd
import seaborn as sns
import numpy as np
import time
import urllib.request
import codecs
from sklearn.model_selection import train_test_split
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
corona_data=pd.read_excel('/Users/toshikifukui/Desktop/色んなやつ/東京_コロナ.xlsx',header=None)
corona_data


# In[64]:


corona_new1=corona_data.drop(0, axis=0)
corona_new1


# In[66]:


corona_new2=corona_new1.drop(1, axis=0)
corona_final=corona_new2.rename(columns={0:"日付", 1:"新規感染者数", 2:"感染者総数"})
corona_final


# In[67]:


corona_final['日付']


# In[68]:


import matplotlib.pyplot as plt
x=corona_final['日付']
y1=corona_final['新規感染者数']
y2=corona_final['感染者総数']
ax = plt.subplot()
plt.plot(x, y1)
plt.xlabel("Date")
plt.ylabel("New Confirmed Cases")
plt.title("New Confirmed Cases in Tokyo")
plt.annotate("←Lifted a State of Emergency(5/25)", xy=(0.55,0.2), xycoords='axes fraction', rotation="vertical", color = "r")
plt.show()
plt.clf()

# In[70]:


plt.plot(x,y2)
plt.title("Total Confirmed Cases in Tokyo")
plt.xlabel("Date")
plt.ylabel("Total Confirmed Cases")
#sns.set_style("darkgrid")
#sns.set_palette("Pastel1")
plt.annotate("←Lifted a State of Emergency(5/25)", xy=(0.55,0.2), xycoords='axes fraction', rotation="vertical", color = "r")
plt.show()
plt.clf()


# In[72]:


plt.bar(x,y1)
plt.xlabel("Date")
plt.ylabel("New Confirmed Cases")
plt.title("New Confirmed Cases in Tokyo")
plt.annotate("←Lifted a State of Emergency(5/25)", xy=(0.45,0.2), xycoords='axes fraction', rotation="vertical", color = "r")
#sns.set_style("darkgrid")
#sns.set_palette("Pastel2")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




