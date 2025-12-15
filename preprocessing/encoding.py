from sklearn.preprocessing import LabelEncoder
import pandas as pd

def encode(df, cols):
    if "Hired" in cols:
        le = LabelEncoder()
        df["Hired"] = le.fit_transform(df["Hired"])
        cols = [c for c in cols if c != "Hired"]

    return pd.get_dummies(df, columns=cols, drop_first=True)
