import pandas as pd

def analyze_and_clean_csv(csv_path, save_cleaned=True):
    # Load data
    df = pd.read_csv(csv_path)

    numerical_cols = ["Age", "Salary", "Performance_Score"]
    categorical_cols = ["Gender", "Experience", "Department", "Hired", "Location"]

    mode_safe = ["Gender", "Department", "Location"]
    unknown_safe = ["Experience", "Hired"]
    print(
    f"Experience range: {df['Experience'].value_counts()}"
                                     )

    IMBALANCE_THRESHOLD = 0.75

    print("\n📌 Missing & Present Summary")
    summary = pd.DataFrame({
        "present_count": df.notna().sum(),
        "missing_count": df.isna().sum(),
        "missing_percent": (df.isna().sum() / len(df)) * 100
    })
    print(summary)

    print("\n📌 Categorical Class Imbalance Report")
    for col in categorical_cols:
        dist = df[col].value_counts(normalize=True, dropna=False)
        max_ratio = dist.max()
        status = "IMBALANCED ⚠️" if max_ratio >= IMBALANCE_THRESHOLD else "OK"
        print(f"{col}: max_class_ratio={round(max_ratio,3)} → {status}")

    # ---------- IMPUTATION ----------
    # Numerical → median
    for col in numerical_cols:
        df[col] = df[col].fillna(df[col].median())

    # Categorical → mode
    for col in mode_safe:
        df[col] = df[col].fillna(df[col].mode()[0])

    # Categorical → Unknown
    for col in unknown_safe:
        df[col] = df[col].fillna("Unknown")

    print("\n✅ Missing values after imputation")
    print(df.isna().sum())

    # if save_cleaned:
    #     output_path = csv_path.replace(".csv", "_cleaned.csv")
    #     df.to_csv(output_path, index=False)
    #     print(f"\n💾 Cleaned file saved at: {output_path}")

    return df

df_cleaned = analyze_and_clean_csv("data/raw/employment_dataset.csv")
