import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv('dataset/Crop_recommendation.csv')

# Features (inputs)
X = df[['temperature', 'rainfall', 'humidity', 'ph']]

# Target (output)
y = df['label']   # crop name

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Save model
pickle.dump(model, open('model.pkl', 'wb'))

print("✅ Model trained and saved!")