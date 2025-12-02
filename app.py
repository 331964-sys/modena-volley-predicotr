from flask import Flask, render_template, request
import joblib
import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

app = Flask(__name__)

# Carico il modello
model = joblib.load("modena_model2.pkl")

# Le colonne che il modello si aspetta
FEATURES = [
    "SetNumber",
    "ActionPhase",
    "Modena_SetterZone",
    "BallType",
    "Combination",
    "AZone",
    "BZone"
]

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    prob = None

    if request.method == "POST":
        # Raccolgo i valori dal form HTML
        data = {}
        data["SetNumber"] = int(request.form.get("SetNumber"))
        data["ActionPhase"] = request.form.get("ActionPhase")
        data["Modena_SetterZone"] = int(request.form.get("Modena_SetterZone"))
        data["BallType"] = request.form.get("BallType")
        data["Combination"] = request.form.get("Combination")
        data["AZone"] = request.form.get("AZone")
        data["BZone"] = request.form.get("BZone")

        # Creo un DataFrame da inviare al modello
        df_input = pd.DataFrame([data], columns=FEATURES)

        # Predizione con il modello
        prob_point = model.predict_proba(df_input)[0, 1]
        pred_point = model.predict(df_input)[0]

        prediction = "PUNTO" if pred_point == 1 else "NON PUNTO"
        prob = round(prob_point * 100, 1)

    return render_template("index.html", prediction=prediction, prob=prob)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


								