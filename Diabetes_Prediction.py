import pandas as pd
import numpy as np

# Generate sample data
np.random.seed(0)
data = {
    'Age': np.random.randint(21, 60, size=100),
    'BMI': np.random.uniform(18, 40, size=100),
    'BloodPressure': np.random.randint(60, 90, size=100),
    'Glucose': np.random.randint(70, 200, size=100),
    'Insulin': np.random.randint(0, 300, size=100),
    'SkinThickness': np.random.randint(20, 50, size=100),
    'DiabetesPedigreeFunction': np.random.uniform(0.1, 2.5, size=100),
    'Outcome': np.random.randint(0, 2, size=100)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('Diabetes_Prediction.csv', index=False)

print("CSV file 'Diabetes_Prediction.csv' created successfully.")
