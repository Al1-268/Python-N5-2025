location = ['Entrance Hall','Library','kitchen','garden']
locationds = ['A grand foyer with a crystal chandelier','Dusty bookshelves stretch from floor to ceiling','Copper pots hang above an old stone hearth','Overgrown vines twist around marble statues']
commands = ['N', 'S', 'E', 'W', 'quit', 'help']

print("Welcome to the adventure game!")
name = input("Enter your name: ")
print ("welcome the mystery mansion " + name + "!")
print ("you have 10 moves to explore the mansion")

for index in range(10):
    user = input("enter the direction you want to go in: ")
    if user != commands[index] :
        print("invalid command it has to be eithewr N, S, E, W,")
    if user == 'N':
        print ("you have entered the " + location[0] + " - " + locationds[0])
    elif user == 'S':
        print ("you have entered the " + location[1] + " - " + locationds[1])
    elif user == 'E':
        print ("you have entered the " + location[2] + " - " + locationds[2])
    elif user == 'W':
        print ("you have entered the " + location[3] + " - " + locationds[3])
    elif user == 'quit':
        print ("you have quit the game")
    elif user == 'help':
        print ("the commands are N, S, E, W, quit, help")
