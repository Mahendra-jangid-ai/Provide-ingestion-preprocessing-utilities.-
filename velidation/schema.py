import pandera as pa
from pandera.typing import Series


class HRRawSchema(pa.SchemaModel):

    Age: Series[float] = pa.Field(gt=18, nullable=True)

    Salary: Series[float] = pa.Field(gt=0, nullable=True)

    Experience: Series[str] = pa.Field(
        nullable=True,
        regex=r"^\d+\s+years$"
    )

    Performance_Score: Series[int] = pa.Field(
        ge=1, le=10, nullable=True
    )

    Gender: Series[str] = pa.Field(
        nullable=True,
        isin=["Male", "Female", "M", "F"]
    )

    Department: Series[str] = pa.Field(
        nullable=True,
        isin=["HR", "Sales", "Engineering", "Marketing"]
    )

    Hired: Series[str] = pa.Field(
        nullable=True,
        isin=["Yes", "No", "Y", "N"]
    )

    Hiring_Date: Series[str]

    Location: Series[str]

    class Config:
        strict = True
