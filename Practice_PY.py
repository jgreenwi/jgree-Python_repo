#Python Practice 
import Value
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