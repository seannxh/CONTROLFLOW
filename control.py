# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():

    letter = input("Enter a single letter (a-z or A-Z): ")
    if len(letter) != 1 or not letter.isalpha():
        print("Invalid input. Please enter a single alphabetical letter.")
        return
    
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

    if letter in vowels:
        print(f'The letter {letter} is a vowel')
    else:
        print(f'The letter is not a vowel')
# Call the function
check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    voting_age = 18
    
    try:
        age = int(input("Please enter your age: "))
        
        if age < 0:
            print("Invalid input. Age cannot be negative.")
        else:
            if age >= voting_age:
                print("You are eligible to vote.")
            else:
                print("You are not eligible to vote yet.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    try:
        # Prompt the user to enter a dog's age
        dog_age = float(input("Input a dog's age: "))
        
        # Validate the input to ensure it's a positive number
        if dog_age < 0:
            print("Invalid input. Age cannot be negative.")
            return
        
        # Calculate the dog's age in dog years
        if dog_age <= 2:
            dog_years = dog_age * 10
        else:
            dog_years = (2 * 10) + ((dog_age - 2) * 7)
        
        # Print the result
        print(f"The dog's age in dog years is {dog_years:.1f}.")
    except ValueError:
        # Handle invalid input gracefully
        print("Invalid input. Please enter a valid number.")

# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Prompt the user for weather conditions
    is_cold = input("Is it cold? (yes/no): ").strip().lower()
    is_raining = input("Is it raining? (yes/no): ").strip().lower()
    
    # Validate the input
    if is_cold not in ['yes', 'no'] or is_raining not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'.")
        return
    
    # Determine clothing advice based on the conditions
    if is_cold == 'yes' and is_raining == 'yes':
        print("Wear a waterproof coat.")
    elif is_cold == 'yes' and is_raining == 'no':
        print("Wear a warm coat.")
    elif is_cold == 'no' and is_raining == 'yes':
        print("Carry an umbrella.")
    elif is_cold == 'no' and is_raining == 'no':
        print("Wear light clothing.")

# Call the function
weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Define a mapping for months and their corresponding seasons
    months = {
        "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
        "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
    }
    
    try:
        # Prompt the user to enter the month
        month_input = input("Enter the month of the year (Jan - Dec): ").strip().capitalize()
        if month_input not in months:
            print("Invalid input. Please enter a valid month abbreviation (e.g., Jan, Feb, etc.).")
            return
        
        # Prompt the user to enter the day
        day = int(input("Enter the day of the month: "))
        if day < 1 or day > 31:
            print("Invalid input. Day must be between 1 and 31.")
            return
        
        # Map the month to a number
        month = months[month_input]
        
        # Determine the season
        if (month == 12 and day >= 21) or (1 <= month <= 2) or (month == 3 and day <= 19):
            season = "Winter"
        elif (month == 3 and day >= 20) or (4 <= month <= 5) or (month == 6 and day <= 20):
            season = "Spring"
        elif (month == 6 and day >= 21) or (7 <= month <= 8) or (month == 9 and day <= 21):
            season = "Summer"
        elif (month == 9 and day >= 22) or (10 <= month <= 11) or (month == 12 and day <= 20):
            season = "Fall"
        else:
            print("Invalid date range.")
            return
        
        # Print the result
        print(f"{month_input} {day} is in {season}.")
    
    except ValueError:
        print("Invalid input. Please enter a valid number for the day.")

determine_season()


