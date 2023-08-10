# Python Containers
#Lists, Tuples, and Dictionaries

student = {
    'name': 'Maria',
    'course': 'SEI',
    'current_week': 7
}

students_name = 'name'
name = student['name']


student['name'] = 'Tina'
print(student['name'])
print(student['course'])

print(student.get('skills', {
    'HTML': 5,
    'JavaScript': 4
}) )

student['age'] = 21
print(student)


# del student['course']

if 'course' in student:
  print( f"{student['name']} is enrolled in {student['course']}")
else:
  print( f"{student['name']} is not enrolled in a course")


for key in student:
  print( f"{key} = {student[key]}" )


print(student.items())

for item_tuple in student.items():
  print( f"key = {item_tuple[0]} / value = {item_tuple[1]}" )


# same thing better practice. iterate over items through the dictionary 
  for key, value in student.items():
   print( f"key = {key} / value = {value}" )
  
where_my_things_are = {
  'car': 'in the garage',
  'keys': 'in the car',
  'wallet': 'in the drawer'
}

for thing, location in where_my_things_are.items():
  print( f"My  {thing} is kept {location}")


  # Lists (like js arrays)

  colors = ['red', 'green', 'blue']
  colors[-1] = 'brown'
  colors.append('purple')
  colors.extend(['orange', 'black'])

  colors.pop(2)
  print(colors)

odds = [1, 3, 5]
evens = [2, 4, 6]
nums = odds + evens
print(nums)


# iterate over items in a python list
idx = 0
colors = ['red', 'green', 'blue']
for color in colors:
  print(idx, color)
  idx += 1


# best practice same thing as above
for idx, color in enumerate(colors):
  print(idx, color)



scores = [
  {
    'name': 'Dylan',
    'points': 25  # points the player scored
  }
]
scores.append({
  'name': 'jacob',
  'points': 24
})

for score in scores:
  print(f"{score['name']} scored {score['points']} points")


  nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


  squares = [num * num for num in nums]

  even_squares = [n * n for n in nums if (n * n) % 2 == 0]

#Tuples

colors = ('red', 'blue', 'green')
print(colors)


short_name = 'Alexandria'[0:4]


#Exercise 1
#Create a list named students containing some student names (strings).
#Print out the second student’s name.
#Print out the last student’s name.

students = ['james', 'bob', 'dylan']
print(students[1])
print(students[2])

# Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string “[food goes here] is a good food”.

foods = ('burger', 'fries', 'chicken')
for food in foods:
  print(f'{food} is good food')


# Exercise 3
# Using a for loop, print just the last two food strings from foods.
# Hint: Use the slice operator to select the last two foods

for food in foods[-2:]:
  print(food)


# Exercise 4
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# “I was born in city, state - population of population”

home_town = {
  'city': 'Roanoke',
  'state': 'Virginia',
  'population': '100,000'
}

print(f'I was born in {home_town["city"]}, {home_town["state"]} - population of {home_town["population"]}')



# Exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# “city = Arcadia”
# “state = California”
# “population = 58000”


for key, value in home_town.items():
   print( f"key = {key} / value = {value}" )



#    Exercise 6
# Create an empty list named cohort.
# Using a for loop to iterate over the students list.
# Hint: Use the enumerate function to provide both the index & student

# Within the for loop, add a dictionary to the cohort list that combines the student’s name and the food in the foods list at the same index. Each dictionary will have this shape:

#   {
#     'student': 'Tina',
#     'fav_food': 'Cheeseburger'
#   }
# Iterate over the cohort list, printing out each item (it’s not necessary to format the dictionaries).
cohort = []

for index, student in enumerate(students):
     cohort.append({
    'student': student,
    'fav_food': foods[index]
  })

for student in cohort:
  print(student)


#   Exercise 7
# Using the list of students and a list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over the awesome_students list, printing out each string.



awesome_students = [f"{name} is awesome!" for name in students]

for student in awesome_students:
  print(student)


# Exercise 8
# Use a for loop to iterate over a list comprehension that filters the foods tuple to only include food strings that contains the letter a.
# Within the for loop, print each food string.


for food in [food for food in foods if 'a' in food]:
  print(food)