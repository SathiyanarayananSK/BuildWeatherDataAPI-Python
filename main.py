from flask import Flask, render_template
import pandas as pd

app = Flask("Website")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def temp(station, date):
    name_id = 1000000 + int(station)
    df = pd.read_csv(f"data/Weather_API_data_A6/TG_STAID{str(name_id)[1:]}.txt", skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze()/10
    return {"station": station,
            "date": date,
            "temperature": temperature}


app.run(debug=True)

