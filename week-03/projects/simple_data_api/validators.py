from pydantic import BaseModel, Field, field_validator


class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str | None = Field(default="", max_length=500)
    price: float = Field(..., gt=0)

    @field_validator("name")
    def name_must_not_be_blank(cls, v):
        if not v.strip():
            raise ValueError("Name must not be blank")
        return v


class ItemUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=100)
    description: str | None = Field(None, max_length=500)
    price: float | None = Field(None, gt=0)

    @field_validator("name")
    def name_must_not_be_blank(cls, v):
        if v is not None and not v.strip():
            raise ValueError("Name must not be blank")
        return v
