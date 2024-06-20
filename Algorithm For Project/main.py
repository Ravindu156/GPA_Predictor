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