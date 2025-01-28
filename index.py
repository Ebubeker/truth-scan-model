import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np

train_df = pd.read_csv("Put da training data here with da path!!!!")

numeric_cols = train_df.select_dtypes(include=[np.number]).columns
categorical_cols = train_df.select_dtypes(exclude=[np.number]).columns

numeric_imputer = SimpleImputer(strategy='mean')
numeric_imputer.fit(train_df[numeric_cols])

categorical_imputer = SimpleImputer(strategy='most_frequent')
categorical_imputer.fit(train_df[categorical_cols])


def impute_missing_values(new_data_path):

    new_df = pd.read_csv(new_data_path)

    new_df_numeric = pd.DataFrame(numeric_imputer.transform(new_df[numeric_cols]), columns=numeric_cols)

    new_df_categorical = pd.DataFrame(categorical_imputer.transform(new_df[categorical_cols]), columns=categorical_cols)

    new_df_imputed = pd.concat([new_df_numeric, new_df_categorical], axis=1)

    other_cols = new_df.columns.difference(numeric_cols).difference(categorical_cols)
    new_df_imputed = pd.concat([new_df_imputed, new_df[other_cols]], axis=1)

    new_df_imputed = new_df_imputed[new_df.columns]

    return new_df_imputed


imputed_df = impute_missing_values("Put da missing value data ova here!!!")
imputed_df.to_csv('new_data_imputed.csv', index=False)