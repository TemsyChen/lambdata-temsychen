"""Functions to help engineer dataframes"""

import pandas as pd
from sklearn.model_selection import train_test_split

#check dataframe for nulls and return number of missing values
def null_count(df):
    print(df.isna().sum())

#respectively returns training pd.Dataframe and test pd.Dataframe
def train_split(df, frac):
  X_train, X_test = train_test_split(df, train_size=frac, random_state=37)
  return X_train, X_test


