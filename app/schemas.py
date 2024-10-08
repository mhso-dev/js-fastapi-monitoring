from pydantic import BaseModel, Field

feature_names = [
    "fixed_acidity",
    "volatile_acidity",
    "citric_acid",
    "residual_sugar",
    "chlorides",
    "free_sulfur_dioxide",
    "total_sulfur_dioxide",
    "density",
    "ph",
    "sulphates",
    "alcohol_pct_vol",
]

## ge : greater than or equal / le : less than or equal

# Feature
class Wine(BaseModel):
    fixed_acidity: float = Field(
        ..., ge=0, description="grams per cubic decimeter of tartaric acid"
    )
    volatile_acidity: float = Field(
        ..., ge=0, description="grams per cubic decimeter of acetic acid"
    )
    citric_acid: float = Field(..., ge=0, description="grams per cubic decimeter of citric acid")
    residual_sugar: float = Field(
        ..., ge=0, description="grams per cubic decimeter of residual sugar"
    )
    chlorides: float = Field(..., ge=0, description="grams per cubic decimeter of sodium chloride")
    free_sulfur_dioxide: float = Field(
        ..., ge=0, description="milligrams per cubic decimeter of free sulfur dioxide"
    )
    total_sulfur_dioxide: float = Field(
        ..., ge=0, description="milligrams per cubic decimeter of total sulfur dioxide"
    )
    density: float = Field(..., ge=0, description="grams per cubic meter")
    ph: float = Field(..., ge=0, lt=14, description="measure of the acidity or basicity")
    sulphates: float = Field(
        ..., ge=0, description="grams per cubic decimeter of potassium sulphate"
    )
    alcohol_pct_vol: float = Field(..., ge=0, le=100, description="alcohol percent by volume")


# Target
class Rating(BaseModel):
    quality: float = Field(
        ...,
        ge=0,
        le=10,
        description="wine quality grade ranging from 0 (very bad) to 10 (excellent)",
    )