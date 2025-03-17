input("welcome to the score board, type hello to start")
print("hello")
print("x ends the session ")
print("q adds a score to home team")
print("w adds a score to away team")
home = 0
away = 0
period = 1
while period < 4:
    key = input("enter one of the following keys: q,w,x")
    if key == "q":
        home = home + 1
        print("home team: ",home)
        print("away team: ",away)
        print("period ",period)
            
    elif key == "w":
        away = away + 1
        print("home team: ",home)
        print("away team: ",away)
        print("period ",period)
            
    elif key == "x":
        
            print("home team: ",home)
            print("away team: ",away)
            print("period ",period)
            period = period + 1

print("final score")
print("home team: ",home)
print("away team: ",away)
print("period ",period)
print("game over")
            
