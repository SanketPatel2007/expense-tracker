import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="1st",
    user="postgres",
    password="Sanket",
    port="5432"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS expense (
    id SERIAL PRIMARY KEY,
    name VARCHAR(40),
    amount FLOAT
)
""")
conn.commit()

def add_expense():
    name=input("Enter expense name:")

    try:
        amount=float(input("Enter the amount:"))
    except ValueError:
        print("Amount is invalid. try again")
        return
    
    cur.execute(
        "INSERT INTO expense (name, amount) VALUES (%s,%s)",
        (name,amount)
    )

    conn.commit()

def display():

    cur.execute("SELECT * FROM expense")
    rows=cur.fetchall()

    if not rows:
        print("no data is found\n")
        return

    else:
        for row in rows:
            print(f"ID: {row[0]} | {row[1]} - ₹{row[2]}")

def total_expense():
    cur.execute("SELECT SUM(amount) FROM expense")
    total=cur.fetchone()[0]
    print("Total:",total,"\n")


def delete_expense():
    display()
    try:
        exp_id=int(input("Enter ID to delete"))
    except ValueError:
        print("Invalid ID\n")
        return()
    
    cur.execute("DELETE FROM expense WHERE id=%s",(exp_id,))
    conn.commit()

    if cur.rowcount==0:
        print("No record found\n")
    else:
        print("Deleted Successfully\n")

def update_expense():
    display()
    try:
        exp_id=int(input("Enter ID to update:"))
    except ValueError:
        print("Invalid ID\n")

    name=input("Enter the name: ")
    
    try:
        amount=float(input("Enter new amount:"))
    except ValueError:
        print("Invalid amount\n")
        return()

    cur.execute(
        "UPDATE expense SET name=%s, amount=%s where id=%s",
        (name,amount,exp_id)
    )

    conn.commit()

    if cur.rowcount==0:
        print("No record found\n")
    else:
        print("Updated Successfully\n")

while True:
    a=int(input("1.add 2.Display 3.total 4.update 5.Delete 6.Exit\n"))
    match a:
        case 1:
            add_expense()
        case 2:
            display()
        case 3:
            total_expense()
        case 4:
            update_expense()
        case 5:
            delete_expense()
        case 6:
            break
        case _:
            print("Enter valid input")


cur.close()
conn.close()

    
