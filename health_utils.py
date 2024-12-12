def calculate_bmi(height, weight):
    """Calculate Body Mass Index (BMI) given height in meters and weight in kilograms."""
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive values.")
    return weight / (height ** 2)

def calculate_bmr(height, weight, age, gender):
    """Calculate Basal Metabolic Rate (BMR) using the Harris-Benedict equation."""
    if height <= 0 or weight <= 0 or age <= 0:
        raise ValueError("Height, weight, and age must be positive values.")

    if gender == 'male':
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == 'female':
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Gender must be 'male' or 'female'.")