import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

import os  # To handle directories

# Get the absolute path to the root of the project
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create the 'model' directory if it doesn't exist
model_dir = os.path.join(base_dir, 'model')
dataset_path = os.path.join(base_dir, 'heart_disease_dataset.csv')

os.makedirs(model_dir, exist_ok=True)


# Load the dataset
df = pd.read_csv(dataset_path)

# Preprocessing
X = df.drop('target', axis=1)  # Feature columns
y = df['target']  # Target column (heart disease: 1 = presence, 0 = absence)

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a classifier (Random Forest)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

# Save the model using joblib
model_path = os.path.join(model_dir, 'heart_model.joblib')

# Save the model using joblib
joblib.dump(model, model_path)

print("Model trained and saved successfully.")
