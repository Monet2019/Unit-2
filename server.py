from flask import Flask, render_template, url_for, redirect

from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cupcakes")
def all_cupcakes():
    cupcakes = get_cupcakes("cupcakes.csv")
    print(cupcakes)
    return render_template("cupcakes.html", cupcakes=cupcakes)

@app.route("/individual-cupcake")
def individual_cupcake():
    return render_template("individual-cupcake.html")

@app.route("/order")
def order():
    cupcakes = get_cupcakes("orders.csv")
    total = 0
    for cupcake in cupcakes:
        total += float(cupcake["price"])
    return render_template("order.html", cupcakes=cupcakes, total=total)

@app.route("/add-cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)

    if cupcake: 
        add_cupcake_dictionary("orders.csv", cupcake)
        return redirect(url_for("home"))
    else:
        return "Cupcake Not Found"

if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 8000, host = "localhost")