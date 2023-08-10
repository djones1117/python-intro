
def add(*numbers):
    return sum(numbers)

print(add(1,2,3,4,5))
#output: 15

## Write a function called say_hello, that takes one
## argument a persons name, and returns a string like
## Hello Lindsey!
## Hello Jim!
## Hello Shay!



def say_hello(name):
    return f'Hello {name}!'

print(say_hello('Dylan'))

### say_greeting, takes two arguments, greeting + persons name
## returns Hello Jim
## Howdy Lindsey
## Top of the Morning Paddy

def say_greeting(greeting, persons_name):
    return f'{greeting} {persons_name}!'

print(say_greeting('howdy', 'Mike'))

def dev_skills(dev_name, *args):
  dev = {'name': dev_name, 'skills': []}
  # args will be a tuple
  for skill in args:
    dev['skills'].append(skill)
  return dev

print(dev_skills('Alex', 'HTML', 'CSS', 'JavaScript', 'Python'))
# -> {'name': 'Alex', 'skills': ['HTML', 'CSS', 'JavaScript', 'Python']}

#sum_to(6)  # returns 21
#sum_to(10) # returns 55

def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum

print(sum_to(6))




#largest([1, 2, 3, 4, 0])  # returns 4
#largest([10, 4, 2, 231, 91, 54])  # returns 231



#occurrences('fleep floop', 'e')   # returns 2
#occurrences('fleep floop', 'p')   # returns 2
#occurrences('fleep floop', 'ee')  # returns 1
#occurrences('fleep floop', 'fe')  # returns 0




#product(-1, 4) # returns -4
#product(2, 5, 5) # returns 50
#product(4, 0.5, 5) # returns 10.0


