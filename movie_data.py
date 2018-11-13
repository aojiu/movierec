
# coding: utf-8

# In[14]:


from lightfm.datasets import fetch_movielens
from lightfm import LightFM


# In[59]:


import numpy as np
import pandas as pd
import scipy.sparse


# In[60]:


u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('D://xiewy//nyu//cs//ML//movierec//ml-100k//u.user', sep='|', names=u_cols,
                    encoding='latin-1')

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('D://xiewy//nyu//cs//ML//movierec//ml-100k//u.data', sep='\t', names=r_cols,
                      encoding='latin-1')

m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', "imdb url", "unknown", "Action", "Adventure", "Animation"
              "Childrens","Comedy", "Crime","Documentary", "Drama","Fantasy",
              "Film-Noir","Horror", "Musical","Mystery","Romance","Sci-Fi",
              "Thriller", "War","Western"]
movies = pd.read_csv('D://xiewy//nyu//cs//ML//movierec//ml-100k//u.item', sep='|', names=m_cols, usecols = range(23),
                     encoding='latin-1')

movie_ratings = pd.merge(movies, ratings)

movie_users = pd.merge(users, movie_ratings)
# lens = pd.merge(movie_ratings, users)
# movie_ratings.head()
movie_users.head()
movie_users.shape
data = fetch_movielens()
type(data["train"])
print(data["train"])
scipy.sparse.csr_matrix(df.values)


# In[5]:


movie_users.head()


# In[6]:


movie_users = movie_users[movie_users.rating >= 4]


# In[7]:


movie_users.head()


# In[8]:


movie_users.drop(columns = "video_release_date")


# In[9]:


movie_train = movie_users.iloc[0:44300,:]


# In[10]:


movie_test = movie_users.iloc[44300:,:]


# In[11]:


movie_train.shape


# In[44]:


movie_test.shape


# In[56]:


model = LightFM(loss = "warp")                
model.fit(movie_train, epochs = 30, num_threads = 2)


# In[50]:


def rec(model, movie_test, users):
    for user in users:
        user_data = movie_test[movie_test["user_id"]==  user]
        user_data.sort_values(by = "rating", ascending = False)
        print("The favourite filmes are:")
        print(user_data.head(3))
        
        print("The recommanded films by the model are:")
        


# In[54]:


user_data = movie_train.loc[movie_train["user_id"] ==1]
x = user_data.sort_values(by = "rating", ascending = False)
x.head()


# In[27]:


print(user_data.head())


# In[1]:




