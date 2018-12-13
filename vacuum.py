"""
CVR COLLEGE OF ENGINEERING AND TECHNOLOGY
DEPARTMENT OF ARTIFICIAL INTELLIGENCE
PROGRAM: A SIMPLE REFLEX BASED VACUUM CLEANING AGENT
BY: MIR HABEEBULLAH SHAH QUADRI
ROLL NO: 18B81DA914
CLASS: MTECH - I YEAR (AI)
UNDER THE GUIDANCE AND SUPERVISION OF: DR.PONUSAMY
"""
import random

# Create the environment with two locations A and B
# Assign values 1 or 0 randomly to the locations
# 0 means clean and 1 means dirty
class Environment(object):
    def __init__(self):
        self.locationCondition = {'A':'0', 'B':'0'}

        self.locationCondition['A'] = random.randint(0,1)
        self.locationCondition['B'] = random.randint(0,1)
        print('Location Conditions are:', self.locationCondition)

# Create the simple reflex agent as an extention to the evironment class
# Set the score to 0
# Place the agent randomly at one location 0 or 1
# 0 means location A and 1 means location B
class SimpleReflexVacuumAgent(Environment):
    def __init__(self, Environment):
        self.score = 0
        self.vacuumLocation = random.randint(0,1)
        self.locationCondition = Environment.locationCondition

# Check the position the agent currently is in
# If dirty, clean and increment the score by 1
# If clean, decrement the score by 1 and move to next location
# Repeat the same process for the next location
    def runVacuum(self):
        if self.vacuumLocation == 0:
            print('Currently at location A')
            if self.locationCondition['A'] == 1:
                self.cleanLocation(0)
                print('Moving to location B')
                if self.locationCondition['B'] == 1:
                    self.cleanLocation(1)
                else:
                    print('Location B is already clean!')
                    self.score -= 1
            else:
                print('Location A is already clean!')
                self.score -= 1
                print('Moving to location B')
                if self.locationCondition['B'] == 1:
                    self.cleanLocation(1)
                else:
                    print('Location B is already clean!')
                    self.score -= 1
        else:
            print('Currently at Location B')
            if self.locationCondition['B'] == 1:
                self.cleanLocation(1)
                print('Moving to location A')
                if self.locationCondition['A'] == 1:
                    self.cleanLocation(0)
                else:
                    print('Location A is already clean')
                    self.score -= 1
            else:
                print('Location B is already clean')
                self.score -= 1
                print('Moving to location A')
                if self.locationCondition['A'] == 1:
                    self.cleanLocation(0)
                else:
                    print('Location A is already clean')
                    self.score -= 1

# Used for executing the suck operation of the vacuum cleaner
# If location is 0 then clean location A and set location condition to 0
# If location is 1 then clean location B and set location condition to 0
# Increment the score by 1 in both cases
    def cleanLocation(self, location):
        if location == 0:
            print('Location A is dirty. Use Vacuum Cleaner')
            self.locationCondition['A'] = 0
            self.score += 1
            print('Location A is now clean!')
        else:
            print('Location B is dirty. User Vacuum Cleaner')
            self.locationCondition['B'] = 0
            self.score += 1
            print('Location B is now clean!')

    def printScore(self):
        print('The score is: ', self.score)

e = Environment()
srva = SimpleReflexVacuumAgent(e)
srva.runVacuum()
srva.printScore()
