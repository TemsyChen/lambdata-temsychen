"""Functions to help engineer dataframes"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

def null_count(df):
#check dataframe for nulls and return number of missing values

    print(df.isna().sum().sum())
  

def train_split(df, frac):
#respectively returns training pd.Dataframe and test pd.Dataframe

    X_train, X_test = train_test_split(df, train_size=frac, random_state=37)
  
    return X_train, X_test


def randomize(df, seed):
    df = shuffle(df, random_state=seed)

    return(df)


if __name__ == '__main__':
    print('hi temsy')
    df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data')
    print('Original df:\n', df.head())
    print('Null count:', null_count(df))
    print('Train test split:', train_split(df, .8))
    print('Randomize:', randomize(df, 37))