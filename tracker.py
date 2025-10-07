#Name : Chavi Jaiswal
#date : 4th october, 2025 
#DAILY CALORIE TARCKER (CLI)
print("\nWelcome to the Daily Calorie Tracker!  ")
print("This program will help you to keep track of meals and calories.")

num_meals= int(input("\nHow many meals do you want to enter?:")) #asking how many meals they want to enter.

meals = [] #empty list 
calories = [] #empty list

#using for loop and f string 
for i in range(num_meals):
    meal_name = input(f"\nEnter meal {i+1} name :")
    calorie_amount = int(input(f"Enter calories for {meal_name}:"))
    meals.append(meal_name)
    calories.append(calorie_amount)
  
print("\nMeals list:", meals) #\n : moves the text to the next line when printed.
print("\nCalories list:", calories)

#calculating calorie 
total_calories = sum(calories)
average_calories = total_calories/ len(calories)


#Asking user to input their daily calorie limit.
daily_calorie_limit = int(input("\nEnter your daily calorie limit:"))

print(f"\nTotal calories consumed : {total_calories}")
print(f"Average calories per meal: {average_calories:.2f}")
print(f"Your daily limit: {daily_calorie_limit}")

#comparssion 
if total_calories>daily_calorie_limit:
    print("\nYou have esceeded your daily calorie limit ! try to eat within you calorie limit")
elif total_calories == daily_calorie_limit:
    print("\nYou have exaxctly reached your daily calorie limit!")
else:
    print("\nGreat job! You are within your calorie limit.")


print("\nCalorie Tracker Report")
print("Meal name\tCalories") #\t gap between columns 
print("-"* 30)

for i in range(len(meals)):
    print(f"{meals[i]}\t\t{calories[i]}")
print("-" * 30)
print(f"Total: \t\t{total_calories}")
print(f"Average:\t{average_calories:.2f}")

import datetime   # To add date and time to the file

# Ask the user if they want to save the report
save_option = input("\nDo you want to save this report to a file? (yes/no): ").lower()

if save_option == "yes":
    # Create a timestamp (current date and time)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Open (or create) a file named calorie_log.txt in 'append' mode
    with open("calorie_log.txt", "a") as file:
        file.write("\n--- Daily Calorie Tracker Session ---\n")
        file.write(f"Date: {timestamp}\n\n")
        file.write("Meal Name\tCalories\n")
        file.write("--------------------------------\n")
        
        # Write each meal and its calorie value
        for i in range(len(meals)):
            file.write(f"{meals[i]}\t\t{calories[i]}\n")

        # Write totals and averages
        file.write("--------------------------------\n")
        file.write(f"Total:\t\t{total_calories}\n")
        file.write(f"Average:\t{average_calories:.2f}\n")

        # Write limit status
        if total_calories > daily_calorie_limit:
            file.write("You exceeded your daily calorie limit!\n")
        else:
            file.write(" You are within your daily calorie limit!\n")

    # Confirmation message
    print("\nReport saved successfully to calorie_log.txt!")
else:
    print("\nReport not saved.")












