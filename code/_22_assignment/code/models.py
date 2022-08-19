from pydantic import BaseModel

class AddBody(BaseModel):
    name: str
    quantity:int

class UpdateBody(BaseModel):
    name: str
    quantity:int

class DeleteBody(BaseModel):
    name: str