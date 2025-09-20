from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained ML model (saved with joblib)
model = joblib.load("model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    values = {}  # store form inputs

    if request.method == "POST":
        try:
            # Get input values from form
            values["temp"] = float(request.form["temp"])
            values["rh"] = float(request.form["rh"])
            values["wind"] = float(request.form["wind"])
            values["rain"] = float(request.form["rain"])
            values["ffmc"] = float(request.form["ffmc"])
            values["dmc"] = float(request.form["dmc"])
            values["dc"] = float(request.form["dc"])
            values["isi"] = float(request.form["isi"])
            values["bui"] = float(request.form["bui"])

            # Prepare data for model (match training order)
            data = np.array([[
                values["temp"],  # Temperature
                values["rh"],    # RH
                values["wind"],  # Ws
                values["rain"],  # Rain
                values["ffmc"],  # FFMC
                values["dmc"],   # DMC
                values["dc"],    # DC
                values["isi"],   # ISI
                values["bui"]    # BUI
            ]])

            # Predict
            prediction_raw = model.predict(data)[0]
            prob_fire = 1 / (1 + np.exp(-prediction_raw))
            print(prob_fire)
            if prob_fire >= 1:  # threshold you choose
                prediction = "🔥High Risk of Fire"
            else:
                prediction = "✅Low Risk of Fire"

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template("index.html", prediction=prediction, values=values)

if __name__ == "__main__":
    app.run(debug=True)
