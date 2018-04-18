
# coding: utf-8

# # K-means
# I use ___scikit-learn___, which privide *kmeans* for us

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# use numpy to load the .txt file<br>
# you can just check the ___samples.txt___ file

# In[2]:


data = np.loadtxt('samples.txt')

data = data[:,1:] 
#remove first column


# In[3]:


pred = KMeans(2)
# init the KMean, which has 2 clusters

y = pred.fit_predict(data)
# fit the data in the 'pred' object


# # visualize the result
# If you can't understand the code,<br>
# don't mind,it really dosen't matter, it's just a trick

# In[6]:


plt.figure(figsize=(12,8))
plt.subplot(121)
plt.scatter(data[:,0],data[:,1])
plt.title("Before")
# visualize the data 

plt.subplot(122)
plt.scatter(data[:,0],data[:,1], c=y)
# visualize the result 
plt.scatter(pred.cluster_centers_[:,0],pred.cluster_centers_[:,1],marker='x')
plt.annotate("cluster center1",xy=(pred.cluster_centers_[0,0],pred.cluster_centers_[0,1]),
            xytext=(pred.cluster_centers_[0,0]+.3,pred.cluster_centers_[0,1]+.3),
            arrowprops=dict(facecolor='black',arrowstyle="->"))
plt.annotate("cluster center2",xy=(pred.cluster_centers_[1,0],pred.cluster_centers_[1,1]),
            xytext=(pred.cluster_centers_[1,0]+.3,pred.cluster_centers_[1,1]+.3),
            arrowprops=dict(facecolor='black',arrowstyle="->"))
# 
plt.title("After")
plt.show()
