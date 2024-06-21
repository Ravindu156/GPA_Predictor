# GPA Predictor with Machine Learning (*Random Forest*)

This project is a GPA Predictor application built using Python, Tkinter, and a Random Forest Regressor. The application predicts a student's GPA for the third semester based on various personal and academic factors.

## Features

- Input fields for GPA of the first two semesters and other influencing factors.
- Uses a trained Random Forest Regressor model to predict the GPA.
- GUI built with Tkinter for easy user interaction.

## Requirements

- Python 3.x
- pandas
- numpy
- scikit-learn
- tkinter (comes pre-installed with Python)

## Installation

1. Clone the repository to your local machine:

```sh
https://github.com/Ravindu156/GPA_Predictor.git
cd MachineLearning For Project
```

2. Install the required libraries:

```sh
pip install pandas numpy scikit-learn
```

3. Ensure you have Python 3.x installed on your system. If not, download and install it from [python.org](https://www.python.org/).

4. Place the dataset file form_dataset.csv in the root directory of the project.

## Usage

1. Navigate to the directory where the repository was cloned.

2. Run the main.py file to start the application:

```sh
python main.py
```

3. Enter the required information in the provided fields and click on the "Predict" button to get the predicted GPA for the third semester.

## Input Fields

- *GPA of Semester 1*: Enter the GPA of the first semester.
- *GPA of Semester 2*: Enter the GPA of the second semester.
- *Commutes From Home*: Select "Yes" or "No".
- *Economic Status*: Select "Greater than Rs.50000" or "Less than Rs.50000".
- *Part-Time Job*: Select "Yes" or "No".
- *Distance to Campus (km)*: Enter the distance to the campus in kilometers.
- *Internet Connection*: Select "Good" or "Bad".
- *Attendance*: Select "Greater than 50%" or "Less than 50%".
- *Time Spent on Social Media Per Week (hours)*: Enter the number of hours spent on social media per week.
- *Long-Term Illness*: Select "Yes" or "No".

## Prediction Model

The GPA prediction is based on a Random Forest Regressor model trained on a dataset of student GPAs and influencing factors.

### Model Training

The dataset form_dataset.csv is used to train the model. The dataset is split into training and testing sets, and a Random Forest Regressor is trained on the training data. The model's performance is evaluated using Mean Squared Error (MSE).

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load the dataset
data = pd.read_csv('form_dataset.csv')

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
```

### Prediction Function

The function `predict_performance` gathers user inputs, preprocesses them, and uses the trained model to predict the GPA for the third semester. The predicted GPA is displayed in the GUI.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements or new features.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

For any questions or suggestions, please open an issue on the GitHub repository or contact the project maintainer.

---
