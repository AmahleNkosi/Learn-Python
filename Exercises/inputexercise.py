#I will be using a straight python file for this exercise
#Found it in the "Python For Beginners" book. Link: https://payhip.com/b/4WRco

colour=input("Enter your favorite color: ")#Asks the user to insert their fav colour
pythonYear=int(input('Enter the year in which you started learning python: '))
currentYear=2025
yearsLearningPython=currentYear-pythonYear
print('You have been learning Python for '+ str(yearsLearningPython) +' year(s) and your favorite colour is ' + colour) #the str function converts an integer to string
