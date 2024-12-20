from flask import Flask, render_template

app = Flask("Website")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def temp(station, date):
    #df = pandas.read_csv("")
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": temperature}


app.run(debug=True)

