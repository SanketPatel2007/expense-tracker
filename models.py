from pydantic import BaseModel

class Expense(BaseModel):
    name:str
    amount:float

class ExpenseResponse(BaseModel):
    id: int
    name: str
    amount: float