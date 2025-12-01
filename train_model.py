import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset (you must replace path with your file)
df = pd.read_csv("phishing_dataset.csv")

X = df.drop("label", axis=1)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf = RandomForestClassifier(n_estimators=200, max_depth=20, random_state=42)
rf.fit(X_train, y_train)

print("Training Complete!")
print("Accuracy:", rf.score(X_test, y_test))

joblib.dump(rf, "model/rf_model.pkl")
