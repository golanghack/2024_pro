import json
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import requests

# loading
df = pd.read_csv(
    "https://raw.githubusercontent.com/pplonski/datasets-for-start/master/adult/data.csv",
    skipinitialspace=True,
)
x_cols = [col for col in df.columns if col != "income"]
# set
X = df[x_cols]
y = df["income"]
# show
df.head()

# data splitting
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1234
)

# AB
for i in range(100):
    input_data = dict(X_test.iloc[i])
    target = y_test.iloc[i]
    r = requests.post(
        "http://127.0.0.1:8000/api/v1/income_classifier/predict?status=ab_testing",
        input_data,
    )
    response = r.json()
    # feedback
    # requests.put(f'http://127.0.0.1:8000/api/v1/mlrequests/{response["request_id"]}', {'feedback': target})
    # print(response)
