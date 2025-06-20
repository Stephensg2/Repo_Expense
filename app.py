# app.py
from flask import Flask, render_template, redirect, url_for, request
from db import SessionLocal, Expense

app = Flask(__name__)

@app.route('/')
def home():
    session = SessionLocal()
    items = session.query(Expense).all()
    total = sum(item.value for item in items)
    names = [item.name for item in items]
    values = [item.value for item in items]
    session.close()
    return render_template("index.html", items=items, total=total, names=names, values=values)

@app.route('/addexpense', methods=['POST'])
def add_item():
    session = SessionLocal()
    selected_name = request.form.get("name")
    new_name = request.form.get("new_name")
    amount = float(request.form.get("amount", 0))

    name_to_use = new_name if selected_name == "__new__" else selected_name
    expense = session.query(Expense).filter_by(name=name_to_use).first()

    if expense:
        expense.value += amount
    else:
        expense = Expense(name=name_to_use, value=amount)
        session.add(expense)

    session.commit()
    session.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    print('test')