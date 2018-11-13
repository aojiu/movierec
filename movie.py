from lightfm import LightFM
from lightfm.datasets import fetch_movielens
import numpy as np
import pandas as pd
#train model then predict score with model using test data
# df = pd.read_table(fetch_movielens)
data = fetch_movielens(min_rating = 4.0)
print(data["train"])
# model = LightFM(loss = "warp")
# model.fit(data["train"], epochs = 30, num_threads = 2)
# def sample_recommandation(model, data, user_ids):
#     n_users, n_items = data["train".shape]
#     for user_id in user_ids:
#         know_positives =data["item_labels"]
# u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
# users = pd.read_csv('ml-100k//u.user', sep='|', names=u_cols,
#                     encoding='latin-1')
#
# r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
# ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols,
#                       encoding='latin-1')
#
# m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
# movies = pd.read_csv('ml-100k/u.item', sep='|', names=m_cols, usecols=range(5),
#                      encoding='latin-1')
#
# movie_ratings = pd.merge(movies, ratings)
# lens = pd.merge(movie_ratings, users)