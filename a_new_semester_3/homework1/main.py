from flask import Flask, render_template

app = Flask(__name__)

user_name = "Kostya"

dishes = [
    {'dish': 'pizza', 'price': 80},
    {'dish': 'burger', 'price': 95},
    {'dish': 'borch', 'price': 70},
    {'dish': 'cheese', 'price': 100},
]

@app.route("/")
def hi():
    return f"Hi in pizzeria Fazbers\nYou're welcome"

@app.route("/menu/")
def results():
    context = {
        "title": "menu",
        "dishes": dishes,

    }
    return render_template("menu.html", **context)
if __name__ == '__main__':
    app.run(debug=True)