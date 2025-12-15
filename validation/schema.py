import pandera as pa
from pandera import Column, DataFrameSchema, Check

HRSchema = DataFrameSchema(
    {
        "Age": Column(float, Check.gt(18), nullable=True),
        "Salary": Column(float, Check.gt(0), nullable=True),
        "Experience": Column(str, Check.str_matches(r"^\d+\s+years$"), nullable=True),
        "Performance_Score": Column(int, Check.between(1, 10), nullable=True),
        "Gender": Column(str, Check.isin(["Male", "Female", "M", "F"]), nullable=True),
        "Department": Column(
            str,
            Check.isin(["HR", "Sales", "Engineering", "Marketing"]),
            nullable=True,
        ),
        "Hired": Column(str, Check.isin(["Yes", "No", "Y", "N"]), nullable=True),
        # "Hiring_Date": Column(str),
        "Location": Column(str),
    },
    strict=True,
)
