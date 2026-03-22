from fastapi import FastAPI
from db import get_connection
from models import Expense

app = FastAPI()


@app.get("/")
def home():
    return {"message": "API is running"}


@app.get("/expense")
def get_expense():
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("SELECT * FROM expense")
    rows=cur.fetchall()

    cur.close()
    conn.close()

    return [
        {"id":r[0,"Name":r[1],"amount":r[2]]}
        for r in rows
    ]

@app.post("/expense")
def add_expense(name:str,amount:float):
    conn=get_connection()
    cur=conn.cursor()
    cur.execute(
        "INSERT INTO expense (name,amount) VALUES (%s,%s)",
        (name,amount)
    )
    conn.commit()

    conn.close()
    cur.close()
    return{"message":"Expense Added"}

@app.delete("/expense/{exp_id}")
def delete_expense(exp_id:int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM expense WHERE id=%s",(exp_id,)
    )
    conn.commit()
    cur.close()
    conn.close()

    if cur.rowcount==0:
        return {"error": "No record found"}
    else:
        return{"message":"Deleted"}
    
@app.put("/expence/{exp_id}")
def update_expence(exp_id:int,name:str,amount:float):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE expense SET name=%s, amount=%s WHERE id=%s",(name,amount,exp_id)
    )

    conn.commit()

    cur.close()
    conn.close()


    if cur.rowcount==0:
        return{"error": "No record found"}
    else:
        return{"message":"Updted"}