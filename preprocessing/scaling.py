from sklearn.preprocessing import StandardScaler

def scale(df, cols):
    df[cols] = StandardScaler().fit_transform(df[cols])
    return df
