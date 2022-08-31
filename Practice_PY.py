#Python Practice 
import random
#this function inputs the random method 
#choice method gives random values from a list of random values
#this greeting command allows a random combo of greetings next to your name each time the script is executed.
greetings = ['Hello', 'Hi', 'Hey', 'Sup']
value = random.choice(greetings)
print(value + ', Jeri!')


value = random.uniform(1, 10)
print(value) 
value = random.randint(0, 1)
print(value)
#create list of colors. the k value shows how many times it will pick a random value 
colors = ['Red', 'Black', 'White']
results = random.choices(colors, k=10)
print(results)
#weights is a list that you want to weigh the value. The total will be 38..so each values weight will be a chance 
colors = ['Pink', 'Blue', 'Gray']
results = random.choices(colors, weights=[18, 18, 2], k=10)
print(results)

#deck of cards example 
deck = list(range(1, 53))
print(deck)

#add a random shuffle to the list
deck = list(range(1, 53))
random.shuffle(deck)
print(deck)

#add function to grab unique cards with sample method
deck = list(range(1, 53))
hand = random.sample(deck, k=5)
print(hand)

#new lab practice on LOOPS
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)
#add new condition: if number equals 3 then print out value
for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)
#continue statements will skip to next iteration
for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)
#loop within a loop example:for ea number within a string it will loop and print, then do it again with ev number
for num in nums:
    for letter in 'abc':
        print(num, letter)
#range allows you to go through a loop a certain number of times
for i in range(10):
    print(i)
#to start value at 1 and end at 11
for i in range(1, 11):
    print(i)
#while loops will continue until theres a break
x = 0
while x < 10:
    print(x)
    x += 1
#10 isnt less than 10 so it breaks the loop without an actual 'script'
#keep a loop going infinite (press ctrl + c to stop infinite)
x = 0

while True:
    if x == 5:
        break
    print(x)
    x += 1
#Functions : instructions that help you complete a specific task
#functions use [def] key for definition. Parameters go in ().Pass allows you to leave function blank 
def hello_func():
    pass
print(hello_func())
#put code into function. The () at the end of hello executes function
def hello_func():
    print('Hello Function!')
#practice execute. You can change the (!) in the function by changing it in the print section-execution will then update
hello_func()
hello_func()
#Dry code: repeating the code instead of utilizing code. Return codes are 
def hello_function():
    return 'Hello Function.'
#print(hello_func()

#print(len(hello_func()))
#uppercase your string within the funtion:
#print(hello_func().upper())
#pass arguments to your functions with parameters (). Greeting has to be passed with function or youll get an error
def hello_func(greeting):
    return '{} Function.'.format(greeting)
    print(hello_func())
#greeting var will equal string 'hi' and will return function
def hello_func(greeting):
    return '{} Function.'.format(greeting)
print(hello_func('Hi'))
#Practice more with greeting function
def hello_func(greeting, name = 'You'):
    return '{}, {}'.format(greeting, name)
print(hello_func('Hi', name = 'Jeri'))
#Arguments: *args, **kwargs = arbitrary positional argument.
#ex: student info has positional argument and reps the classes the student is taking plus
#keyword args with random info
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
student_info('Math', 'Art', name='Jeri', age=30)
#dictionaries need curly bracs 
courses = ['Math', 'Art']
info = {'name': 'Jeri', 'age':30}
student_info(*courses, **info)