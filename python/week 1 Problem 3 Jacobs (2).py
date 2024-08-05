import random #The first part of the program that was done was to import the random Python library.
#After was the creation of a dictionary that contains the states of the USA and their capitals. States are keys, while capitals are represented as variables.
states_capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver','Connecticut': 'Hartford','Delaware': 'Dover','Florida': 'Tallahassee','Georgia': 'Atlanta','Hawaii': 'Honolulu','Idaho': 'Boise','Illinois': 'Springfield','Indiana': 'Indianapolis','Iowa': 'Des Moines',
    'Kansas': 'Topeka','Kentucky': 'Frankfort','Louisiana': 'Baton Rouge','Maine': 'Augusta','Maryland': 'Annapolis',
    'Massachusetts': 'Boston','Michigan': 'Lansing','Minnesota': 'Saint Paul','Mississippi': 'Jackson',
    'Missouri': 'Jefferson City','Montana': 'Helena','Nebraska': 'Lincoln','Nevada': 'Carson City','New Hampshire': 'Concord',
    'New Jersey': 'Trenton','New Mexico': 'Santa Fe','New York': 'Albany','North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',	'Ohio': 'Columbus','Oklahoma': 'Oklahoma City','Oregon': 'Salem','Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence','South Carolina': 'Columbia','South Dakota': 'Pierre','Tennessee': 'Nashville',
    'Texas': 'Austin','Utah Salt': 'Lake City', 'Vermont': 'Montpelier','Virginia': 'Richmond','Washington': 'Olympia',
    'West Virginia': 'Charleston','Wisconsin': 'Madison','Wyoming': 'Cheyenne'}
states = list(states_capitals.keys())#this statement lists all the keys in the dictionary states_capitals.
# These two statements allow for a container to count the participants correct and incorrect answers.
correct = 0
incorrect =0
# next is a for loop that goes within the range of 10.
for b in range(10):# used as reference: https://snakify.org/en/lessons/for_loop_range/
#inside the for loop is a variable that takes a key randomly selected from the list in states
    state = random.choice(states)
#  the for loop also contains a statement that takes the value from the randomly selected state(its capital)
    capital = states_capitals[state]
#then the loop  prints the question what is the state capital and prints state.
    print("what is this state capital",state:
# the for loop  will ask for the users input.
    guess = input()
# then at the if else statement it will compare the input of the user to the value as stated in the dictionary. Both of which will turn into lowercase so that way the program is not case-sensitive to their answers. If it matches the integer variable will add one to correct if it doesn't it will add one to incorrect.
    if guess.lower()==capital.lower():
        correct += 1
    else:
        incorrect +=1
#Finally after the for loop is complete it will print to the user how many they got correct and incorrect

print( 'you have guessed this many correct:',correct)
print('you have guessed this many invorrect:',incorrect)
