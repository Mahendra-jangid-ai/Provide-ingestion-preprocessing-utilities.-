from sklearn.impute import SimpleImputer

def handle_missing(df, num_cols, cat_cols):
    df[cat_cols] = df[cat_cols].replace({
        "M": "Male",
        "F": "Female",
        "Y": "Yes",
        "N": "No"
    })

    df[num_cols] = SimpleImputer(strategy="mean").fit_transform(df[num_cols])
    df[cat_cols] = SimpleImputer(strategy="most_frequent").fit_transform(df[cat_cols])

    return df
