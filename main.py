from flask import Flask, render_template
import pandas as pd

# Initialize the Flask app
app = Flask("Website")

# Load weather station data
stations = pd.read_csv("data/Weather_API_data_A6/stations.txt", skiprows=17)[["STAID", "STANAME                                 "]]

@app.route("/")
def home():
    """Render the home page with a list of weather stations."""
    return render_template("home.html", data=stations.to_html())

@app.route("/api/v1/<station>/<date>")
def temp(station, date):
    """Fetch temperature data for a specific station and date."""
    name_id = 1000000 + int(station)
    df = pd.read_csv(f"data/Weather_API_data_A6/TG_STAID{str(name_id)[1:]}.txt", skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10  # Convert temperature to Celsius
    return {"station": station,
            "date": date,
            "temperature": temperature}

@app.route("/api/v1/<station>")
def all_data(station):
    """Fetch all temperature data for a specific station."""
    df = pd.read_csv(f"data/Weather_API_data_A6/TG_STAID{str(station).zfill(6)}.txt", skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")  # Convert data to a list of dictionaries
    return result

@app.route("/api/v1/yearly/<station>/<year>")
def all_data_yearly(station, year):
    """Fetch temperature data for a specific station and year."""
    df = pd.read_csv(f"data/Weather_API_data_A6/TG_STAID{str(station).zfill(6)}.txt", skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)  # Convert date column to string for filtering
    result = df.loc[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")  # Filter by year
    return result

# Run the Flask app in debug mode
app.run(debug=True)