from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
from feature_extraction import extract_features
import os

app = Flask(__name__)
CORS(app)

# Load trained model
model_path = "model/rf_model.pkl"
rf_model = joblib.load(model_path) if os.path.exists(model_path) else None

expected_columns = [
    "url_length", "dot_count", "slash_count", "subdomain_count",
    "suspicious_keyword", "special_char_count", "digit_count",
    "url_encoding_count", "has_ip", "is_shortened", "repeated_char_count",
    "https_present", "has_at_symbol"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        url = data.get("url")

        if not url:
            return jsonify({"error": "URL not provided"}), 400

        # Feature extraction
        features = extract_features(url)
        features_df = pd.DataFrame([features]).reindex(columns=expected_columns, fill_value=0)

        result = rf_model.predict(features_df)[0]
        proba = rf_model.predict_proba(features_df)[0]

        return jsonify({
            "url": url,
            "result": "Fake" if result == 1 else "Legit",
            "probability": {"Legit": float(proba[0]), "Fake": float(proba[1])}
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
