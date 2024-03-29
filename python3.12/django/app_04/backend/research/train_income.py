import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
import json

# load data
data_frame = pd.read_csv(
    "https://raw.githubusercontent.com/pplonski/datasets-for-start/master/adult/data.csv",
    skipinitialspace=True,
)
x_cols = [col for col in data_frame.columns if col != "income"]

# set input matrix and target column
X = data_frame[x_cols]
y = data_frame["income"]

# show first row data
data_frame.head()

# train / test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1234
)

# missing
train_mode = dict(X_test.mode().iloc[0])
X_train = X_train.fillna(train_mode)

# debug
print(train_mode)

# converter
encoders = {}
for column in [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]:
    categorial_convert = LabelEncoder()
    X_train[column] = categorial_convert.fit_transform(X_train[column])
    encoders[column] = categorial_convert

# train
rf = RandomForestClassifier(n_estimators=100)
rf = rf.fit(X_train, y_train)

# extra trees
extra = ExtraTreesClassifier(n_estimators=100)
extra = extra.fit(X_train, y_train)

# save
joblib.dump(train_mode, "./train_mode.joblib", compress=True)
joblib.dump(encoders, "./encoders.joblib", compress=True)
joblib.dump(rf, "./random_forest.joblib", compress=True)
joblib.dump(extra, "./extra.joblib", compress=True)
