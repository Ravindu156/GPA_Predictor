# GPA Predictor
This project is a GPA Predictor application built using **Python and Tkinter**. The application allows users to input various factors that might influence a student's GPA and predicts the GPA for the next semester based on a simple **linear regression** model.
## Features
-	Input fields for GPA of the first two semesters.
-	Options to input personal and academic factors such as commute status, economic status, part-time job, distance to campus, internet quality, attendance, social media usage, and long-term illness.
-	A "Predict GPA" button that calculates and displays the predicted GPA based on the provided inputs.
## Requirements
-	Python 3.x
-	Tkinter (comes pre-installed with Python)
## Installation
1.	Clone the repository to your local machine:
```
https://github.com/Ravindu156/GPA_Predictor.git
cd Algorithm For Project
```
2.	Ensure you have Python 3.x installed on your system. If not, download and install it from [python.org]( https://www.python.org/).
3.	No additional libraries are required as Tkinter comes pre-installed with Python.
## Usage
1.	Navigate to the directory where the repository was cloned.
2.	Run the main.py file to start the application:
`python main.py`
3.	Enter the required information in the provided fields and click on the "Predict GPA" button to get the predicted GPA for the next semester.

## Input Fields
-	**GPA of Semester 1**: Enter the GPA of the first semester.
-	**GPA of Semester 2**: Enter the GPA of the second semester.
-	**Are you coming to university from home?**: Select "Yes" or "No".
-	**Economic Status**: Select "Less than Rs.50000" or "Greater than Rs.50000".
-	**Part-time Job**: Select "No" or "Yes".
-	**Distance to Campus (km)**: Enter the distance to the campus in kilometers.
-	**Internet Quality**: Select "Bad" or "Good".
-	**Attendance**: Select "Less than 50%" or "Greater than 50%".
-	**Social Media Time Per Week (hours)**: Enter the number of hours spent on social media per week.
-	**Do you have a long-term illness?**: Select "No" or "Yes".
## Prediction Model
The GPA prediction is based on a linear regression model with the following weights:
-	**w0 (Intercept)**: 2.5
-	**w1 (GPA of Semester 1)**: 0.25
-	**w2 (GPA of Semester 2)**: 0.25
-	**w3 (Commute Status)**: 0.1
-	**w4 (Economic Status)**: 0.1
-	**w5 (Part-time Job)**: -0.1
-	**w6 (Distance to Campus)**: -0.05
-	**w7 (Internet Quality)**: 0.1
-	**w8 (Attendance)**: 0.2
-	**w9 (Social Media Time)**: -0.05
-	**w10 (Long-term Illness)**: -0.2<br><br>
The predicted GPA is calculated using the formula:
```
predicted_gpa = (w0 + 
                 w1 * gpa1 + 
                 w2 * gpa2 + 
                 w3 * commute + 
                 w4 * eco_status + 
                 w5 * part_time + 
                 w6 * distance + 
                 w7 * internet + 
                 w8 * attendance + 
                 w9 * social_media + 
                 w10 * illness)
```
The predicted GPA is clamped to be between 0.0 and 4.0.
## Contributing
Contributions are welcome! Please open an issue or submit a pull request with any improvements or new features.
## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
## Contact
For any questions or suggestions, please open an issue on the GitHub repository or contact the project maintainer.
---

