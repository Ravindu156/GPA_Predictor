import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import tkinter as tk
from tkinter import ttk

# Load the dataset
data = pd.read_csv('form_dataset.csv')
print(data.head())
print(data.info())

# Perform one-hot encoding for categorical variables if needed (though in this dataset, all categorical features are numeric)
# Train-test split
X = data[['GPA_Sem1', 'GPA_Sem2', 'Commutes_From_Home', 'Economic_Status', 'Part_Time_Job', 
          'Distance_to_Campus', 'Internet_Connection', 'Attendance', 'Social_Media_Time', 'Long_Term_Illness']]
y = data['GPA_Sem3']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Calculate accuracy or performance metric
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

# Define function to predict performance
def predict_performance():
    try:
        # Gather input data
        gpa1 = float(entry_gpa1.get())
        gpa2 = float(entry_gpa2.get())
        commutes_from_home = 1 if combobox_commutes_from_home.get() == 'Yes' else 0
        economic_status = combobox_economic_status.get()
        part_time_job = 1 if combobox_part_time_job.get() == 'Yes' else 0
        distance_to_campus = float(entry_distance_to_campus.get())
        internet_connection = 1 if combobox_internet_connection.get() == 'Good' else 0
        attendance = 1 if combobox_attendance.get() == 'High' else 0
        social_media_time = float(entry_social_media_time.get())
        long_term_illness = 1 if combobox_long_term_illness.get() == 'Yes' else 0

        # Convert categorical data to numerical
        economic_status = 1 if economic_status == 'Good' else (2 if economic_status == 'Medium' else 0)

        # Create feature array
        features = np.array([gpa1, gpa2, commutes_from_home, economic_status, part_time_job, 
                             distance_to_campus, internet_connection, attendance, social_media_time, long_term_illness]).reshape(1, -1)

        # Predict the GPA for the third semester
        prediction = model.predict(features)
        predicted_gpa = min(prediction[0], 4.0)  # Ensure predicted GPA does not exceed 4.0
        label_result.config(text=f'Predicted GPA for third semester: {predicted_gpa:.2f}', foreground='green')
    except ValueError:
        label_result.config(text='Please enter valid numeric values for GPA fields.', foreground='red')