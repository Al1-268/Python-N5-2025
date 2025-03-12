input("welcome to the score board, type hello to start")
print("hello")
print("x ends the session ")
print("q adds a score to home team")
print("w adds a score to away team")
home = 0
away = 0
while True:
    key = input("enter one of the following keys: q,w,x")
    if key == "q":
        home = home + 1
    elif key == "w":
        away = away + 1
    elif key == "x":
            print("home team: ",home)
            print("away team: ",away)
            
