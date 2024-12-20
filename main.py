from flask import Flask, render_template
import pandas as pd

app = Flask("Website")

stations = pd.read_csv("data/Weather_API_data_A6/stations.txt", skiprows=17)[["STAID", "STANAME                                 "]]


@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())

@app.route("/api/v1/<station>/<date>")
def temp(station, date):
    name_id = 1000000 + int(station)
    df = pd.read_csv(f"data/Weather_API_data_A6/TG_STAID{str(name_id)[1:]}.txt", skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze()/10
    return {"station": station,
            "date": date,
            "temperature": temperature}


@app.route("/api/v1/<station>")
def all_data(station):
    df = pd.read_csv(f"data/Weather_API_data_A6/TG_STAID{str(station).zfill(6)}.txt", skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")
    return result

@app.route("/api/v1/yearly/<station>/<year>")
def all_data_yearly(station, year):
    df = pd.read_csv(f"data/Weather_API_data_A6/TG_STAID{str(station).zfill(6)}.txt", skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df.loc[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result

app.run(debug=True)

