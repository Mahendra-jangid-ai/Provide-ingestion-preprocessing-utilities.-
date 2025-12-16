import pandera.pandas as pa
from pandera import Column, DataFrameSchema, Check

HRSchema = DataFrameSchema(
    {
        "Age": Column(float, Check.gt(18) and Check.lt(100), nullable=True),
        "Salary": Column(float, Check.gt(0), nullable=True),
        # "Experience": Column(str, Check.str_matches(r"^\d+\s+years$"), nullable=True),
        "Experience": Column(int, Check.gt(0) and Check.lt(82), nullable=True),
        "Performance_Score": Column(int, Check.between(1, 10), nullable=True),
        "Gender": Column(str, Check.isin(["Male", "Female", "M", "F"]), nullable=True),
        "Department": Column(
            str,
            Check.isin(["HR", "Sales", "Engineering", "Marketing",'Unknown']),
            nullable=True,
        ),
        "Hired": Column(str, Check.isin(["Yes", "No", "Y", "N"]), nullable=True),
        # "Hiring_Date": Column(str),
        "Location": Column(str),
    },
    strict=True,
)
