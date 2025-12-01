import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns
import numpy as np
import joblib
import pandas as pd

model = joblib.load("model/rf_model.pkl")

# Replace with your test dataset
df = pd.read_csv("phishing_dataset.csv")

X = df.drop("label", axis=1)
y = df["label"]

y_pred = model.predict(X)

cm = confusion_matrix(y, y_pred)
sns.heatmap(cm, annot=True, cmap="Blues")
plt.title("Confusion Matrix")
plt.show()
