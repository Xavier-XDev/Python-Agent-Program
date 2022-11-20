from datetime import datetime
from enum import Enum, IntEnum


Monday_data = {
    "0:00": "Sleep",
    "1:00": "Sleep",
    "2:00": "Sleep",
    "3:00": "Sleep",
    "4:00": "Sleep",
    "5:00": "Sleep",
    '6:00': 'Breakfast',
    '7:00': 'Gym',
    '8:00': 'Class',
    '9:00': 'Class',
    '10:00': 'Class',
    '11:00': 'Class',
    '12:00': 'Class',
    '13:00': 'Lunch',
    '14:00': 'Class',
    '15:00': 'Class',
    '16:00': 'Class',
    '17:00': 'Television',
    '18:00': 'Television',
    '19:00': 'Dinner',
    '20:00': 'Television',
    '21:00': 'Television',
    '22:00': 'Sleep',
    '23:00': 'Sleep',
    }

Tuesday_Data = {
    '0:00': 'Sleep',
    '1:00': 'Sleep',
    '2:00': 'Sleep',
    '3:00': 'Sleep',
    '4:00': 'Sleep',
    '5:00': 'Sleep',
    '6:00': 'Breakfast',
    '7:00': 'Class',
    '8:00': 'Class',
    '9:00': 'Class',
    '10:00': 'Class',
    '11:00': 'Class',
    '12:00': 'Class',
    '13:00': 'Lunch',
    '14:00': 'Class',
    '15:00': 'Class',
    '16:00': 'Class',
    '17:00': 'Television',
    '18:00': 'Television',
    '19:00': 'Dinner',
    '20:00': 'Television',
    '21:00': 'Television',
    '22:00': 'Sleep',
    '23:00': 'Sleep',
}

Wednesday_data = {
    "0:00": "Sleep",
    "1:00": "Sleep",
    "2:00": "Sleep",
    "3:00": "Sleep",
    "4:00": "Sleep",
    "5:00": "Sleep",
    '6:00': 'Breakfast',
    '7:00': 'Gym',
    '8:00': 'Class',
    '9:00': 'Class',
    '10:00': 'Class',
    '11:00': 'Class',
    '12:00': 'Class',
    '13:00': 'Lunch',
    '14:00': 'Class',
    '15:00': 'Class',
    '16:00': 'Class',
    '17:00': 'Television',
    '18:00': 'Television',
    '19:00': 'Dinner',
    '20:00': 'Television',
    '21:00': 'Television',
    '22:00': 'Sleep',
    '23:00': 'Sleep',
    }
Thursday_data = {
    '0:00': 'Sleep',
    '1:00': 'Sleep',
    '2:00': 'Sleep',
    '3:00': 'Sleep',
    '4:00': 'Sleep',
    '5:00': 'Sleep',
    '6:00': 'Breakfast',
    '7:00': 'Class',
    '8:00': 'Class',
    '9:00': 'Class',
    '10:00': 'Class',
    '11:00': 'Class',
    '12:00': 'Class',
    '13:00': 'Lunch',
    '14:00': 'Class',
    '15:00': 'Class',
    '16:00': 'Class',
    '17:00': 'Television',
    '18:00': 'Television',
    '19:00': 'Dinner',
    '20:00': 'Television',
    '21:00': 'Television',
    '22:00': 'Sleep',
    '23:00': 'Sleep',
}

Friday_data = {
    "0:00": "Sleep",
    "1:00": "Sleep",
    "2:00": "Sleep",
    "3:00": "Sleep",
    "4:00": "Sleep",
    "5:00": "Sleep",
    '6:00': 'Breakfast',
    '7:00': 'Gym',
    '8:00': 'Class',
    '9:00': 'Class',
    '10:00': 'Class',
    '11:00': 'Class',
    '12:00': 'Class',
    '13:00': 'Lunch',
    '14:00': 'Class',
    '15:00': 'Class',
    '16:00': 'Class',
    '17:00': 'Television',
    '18:00': 'Television',
    '19:00': 'Dinner',
    '20:00': 'Television',
    '21:00': 'Television',
    '22:00': 'Sleep',
    '23:00': 'Sleep',
    }
Saturday_data = {
    "0:00": "Sleep",
    "1:00": "Sleep",
    "2:00": "Sleep",
    "3:00": "Sleep",
    "4:00": "Sleep",
    "5:00": "Sleep",
    '6:00': "Sleep",
    '7:00': "Sleep",
    '8:00': "Sleep",
    '9:00': 'Breakfast',
    '10:00': 'River',
    '11:00': 'River',
    '12:00': 'River',
    '13:00': 'River',
    '14:00': 'Lunch',
    '15:00': 'River',
    '16:00': 'River',
    '17:00': 'River',
    '18:00': 'River',
    '19:00': 'Dinner',
    '20:00': 'Television',
    '21:00': 'Television',
    '22:00': 'Sleep',
    '23:00': 'Sleep',
    }
Sunday_data = {
    "0:00": "Sleep",
    "1:00": "Sleep",
    "2:00": "Sleep",
    "3:00": "Sleep",
    "4:00": "Sleep",
    "5:00": "Sleep",
    '6:00': "Sleep",
    '7:00': "Sleep",
    '8:00': "Sleep",
    '9:00': 'Breakfast',
    '10:00': 'Church',
    '11:00': 'River',
    '12:00': 'River',
    '13:00': 'River',
    '14:00': 'Lunch',
    '15:00': 'River',
    '16:00': 'River',
    '17:00': 'River',
    '18:00': 'River',
    '19:00': 'Dinner',
    '20:00': 'Television',
    '21:00': 'Television',
    '22:00': 'Sleep',
    '23:00': 'Sleep',
    }

class Action(IntEnum):
     Monday = 1
     Tuesday = 2
     Wednesday = 3
     Thursday = 4
     Friday = 5
     Saturday = 6
     Sunday = 7

class Agent():
    def __init__(self, day, time):
        self.state = day
        self.time = time

    def perform_action(self):
       if self.state == Action.Monday:
           return Monday_data.get(self.time, 'Invalid Option')

       elif self.state == Action.Tuesday:
           return Tuesday_Data.get(self.time, 'Invalid Option')

       elif self.state == Action.Wednesday:
           return Wednesday_data.get(self.time, 'Invalid Option')

       elif self.state == Action.Thursday:
           return Thursday_data.get(self.time, 'Invalid Option')

       elif self.state == Action.Friday:
           return Friday_data.get(self.time, 'Invalid Option')

       elif self.state == Action.Saturday:
           return Saturday_data.get(self.time, 'Invalid Option')

       elif self.state == Action.Sunday:
           return Sunday_data.get(self.time, 'Invalid Option')