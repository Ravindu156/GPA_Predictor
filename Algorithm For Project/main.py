import tkinter as tk
from tkinter import ttk, messagebox

# Define the prediction function
def predict_gpa(gpa1, gpa2, commute, eco_status, part_time, distance, internet, attendance, social_media, illness):
    w0 = 2.5
    w1 = 0.25
    w2 = 0.25
    w3 = 0.1
    w4 = 0.1
    w5 = -0.1
    w6 = -0.05
    w7 = 0.1 
    w8 = 0.2
    w9 = -0.05
    w10 = -0.2

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
    
    # Clamp the predicted GPA to be between 0.0 and 4.0
    predicted_gpa = max(0.0, min(4.0, predicted_gpa))
    
    return predicted_gpa
    # Function to handle prediction and display result
def handle_predict():
    try:
        gpa1 = float(gpa1_entry.get())
        gpa2 = float(gpa2_entry.get())
        commute = int(commute_var.get())
        eco_status = int(eco_status_var.get())
        part_time = int(part_time_var.get())
        distance = float(distance_entry.get())
        internet = int(internet_var.get())
        attendance = int(attendance_var.get())
        social_media = float(social_media_entry.get())
        illness = int(illness_var.get())

        result = predict_gpa(gpa1, gpa2, commute, eco_status, part_time, distance, internet, attendance, social_media, illness)
        messagebox.showinfo("Predicted GPA", f"The predicted GPA for the next semester is: {result:.2f}")
    except ValueError as e:
        messagebox.showerror("Input Error", "Please enter valid values for all fields.")

# Set up the main application window
root = tk.Tk()
root.title("GPA Predictor")
root.geometry("600x450")

# Define and place labels and entries
tk.Label(root, text="GPA of Semester 1:").grid(row=0, column=0, padx=10, pady=5)
gpa1_entry = tk.Entry(root)
gpa1_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="GPA of Semester 2:").grid(row=1, column=0, padx=10, pady=5)
gpa2_entry = tk.Entry(root)
gpa2_entry.grid(row=1, column=1, padx=10, pady=5)

commute_var = tk.IntVar()
tk.Label(root, text="Are you coming to university from home?").grid(row=2, column=0, padx=10, pady=5)
ttk.Radiobutton(root, text="Yes", variable=commute_var, value=1).grid(row=2, column=1, padx=10, pady=5)
ttk.Radiobutton(root, text="No", variable=commute_var, value=0).grid(row=2, column=2, padx=10, pady=5)

eco_status_var = tk.IntVar()
tk.Label(root, text="Economic Status:").grid(row=3, column=0, padx=10, pady=5)
ttk.Radiobutton(root, text="Less than Rs.50000", variable=eco_status_var, value=0).grid(row=3, column=1, padx=10, pady=5)
ttk.Radiobutton(root, text="Greater than Rs.50000", variable=eco_status_var, value=1).grid(row=3, column=2, padx=10, pady=5)


part_time_var = tk.IntVar()
tk.Label(root, text="Part-time Job:").grid(row=4, column=0, padx=10, pady=5)
ttk.Radiobutton(root, text="No", variable=part_time_var, value=1).grid(row=4, column=1, padx=10, pady=5)
ttk.Radiobutton(root, text="Yes", variable=part_time_var, value=0).grid(row=4, column=2, padx=10, pady=5)

tk.Label(root, text="Distance to Campus (km):").grid(row=5, column=0, padx=10, pady=5)
distance_entry = tk.Entry(root)
distance_entry.grid(row=5, column=1, padx=10, pady=5)

internet_var = tk.IntVar()
tk.Label(root, text="Internet Quality:").grid(row=6, column=0, padx=10, pady=5)
ttk.Radiobutton(root, text="Bad", variable=internet_var, value=0).grid(row=6, column=1, padx=10, pady=5)
ttk.Radiobutton(root, text="Good", variable=internet_var, value=1).grid(row=6, column=2, padx=10, pady=5)

attendance_var = tk.IntVar()
tk.Label(root, text="Attendance:").grid(row=7, column=0, padx=10, pady=5)
ttk.Radiobutton(root, text="Less than 50%", variable=attendance_var, value=0).grid(row=7, column=1, padx=10, pady=5)
ttk.Radiobutton(root, text="Greater than 50%", variable=attendance_var, value=1).grid(row=7, column=2, padx=10, pady=5)

tk.Label(root, text="Social Media Time Per Week(hours):").grid(row=8, column=0, padx=10, pady=5)
social_media_entry = tk.Entry(root)
social_media_entry.grid(row=8, column=1, padx=10, pady=5)

illness_var = tk.IntVar()
tk.Label(root, text="Do you have long term illness?").grid(row=9, column=0, padx=10, pady=5)
ttk.Radiobutton(root, text="No", variable=illness_var, value=0).grid(row=9, column=1, padx=10, pady=5)
ttk.Radiobutton(root, text="Yes", variable=illness_var, value=1).grid(row=9, column=2, padx=10, pady=5)

# Predict button
predict_button = tk.Button(root, text="Predict GPA", command=handle_predict)
predict_button.grid(row=10, column=0, columnspan=3, pady=20)

# Run the main event loop
root.mainloop()
