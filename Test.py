from Agent import Action, Agent
from datetime import datetime
from enum import Enum, IntEnum

year = int(input("Enter the current year (in digits, yyyy): "))
month = int(input("Enter the month (in digits, mm): "))
day = int(input("Enter the day (in digits, dd): "))
hour = int(input("Enter the hour: "))
minute = int(input("Enter the minute: "))
second = int(input("Enter the second: "))
#print("\n 1 = Breakfast \n 2 = Lunch \n 3 = Dinner \n 4 = Sleep \n 5 = Gym \n 6 = Class \n 7 = Church \n 8 = TV \n 9 = River \n")
actionInt = int(input("Enter a digit between 1 and 9 for each corresponding action: "))
testAgent = Agent(Action(actionInt))

d1 = datetime(year = 2020, month = 2, day = 25, hour = 15, minute = 55, second = 59)
print("  ")

print("My schedule for the day is exactly at : " + str(d1))
print(testAgent.perform_action())