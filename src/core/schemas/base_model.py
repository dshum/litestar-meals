from pydantic import BaseModel


class AppBaseModel(BaseModel):
    class Config:
        from_attributes = True
