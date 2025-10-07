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














