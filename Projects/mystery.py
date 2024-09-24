# Intro 

print("You wake up in a dark room with a chair in one corner and a bed in the other there appears to be no door in or out but more      concerning you have no idea how you got here or why you are here")
print("after the initial fear of where you are or how you got here you find a plate of food in the middle that was not there a minute   ago it looks like bread and cheese if it is here there must be a way in and out!")

# choice 1

c1 = input("Do you want to explore the area by the [Food] or do you want to explore the [Chair and Bed]?")

if "o" in c1:
    print("you find a small hatch under the food you might be able to fit into it but you dont dont know whats under it ")

    # choice 2

    c2 = input("do you want to [go through] or [not]")
    if "go through" in c2:
        print("you make your way through the gears into another small dark room")
        print("as you slowly make your way your way toward the door you hear a whimpering sound. you crack the door just a bit and see a monster arms to long for its body legs that seem strangely strong there appears to be a door on the other side of the room")

        # choice 3

        c3 = input("do you want to [run] over to the door or try and [reach out to the monster]")
        if "run" in c3:
            print("you are able to dodge the attack of the monster as you run to the door and make it out of the testing facility")
            print("after making it back to your house you call the police and tell them what happened during the raid on the facility they find three other people and two other monsters apparently they wanted to create a superior life form but obviously failed they were all arrested                                                                YOU WIN")
        else:
            print("As you try and reach out to the monster it attacks it is much to strong for you and it kills you GAME OVER")
        
    else:
        print("You decided not to go through after a while a strange cult looking person comes in and knock you out. You wake up on a surgery table where they conduct experiments on you GAME OVER")
else:
    print("there is nothing special about the chair but in the bed you find a paper clip")

    # Choice 4

    c4 = input("do you want to keep exploring the [bed] or just [wait]")

    if "bed" in c4:
        print("You notice that the floor boards beneath the bed is a different color than then the others when you pry them up you notice a locked hatch")

        # Choice 5
        c5 = input(" do you want to [give up] or try and think if there is any way for you to [open the lock]?")

        if "open" or "lock" in c5:
            print("you are stumped for a while until you remember the paper clip it could probably pick the lock if you tried")
            print("After 20minute of trying you finally are able to open the lock")
             
             #Choice 6

            c6 = input("The hatch opens into a hall way that goes in four directions [forward], [left], [back], or [right] which way do you want to go")
            
            if "right" in c6:
                print("as you walk right for a while you finally reach a room where a bunch of people are huddled around something that you cant really see they then notice you")
                print("they seem very startled but that wears off and they start to run at you. You try your best but they are faster and kill you                                                                GAME OVER")

            elif "left" in c6:
                print("it leads out side and you are able to escape YOU WIN")

            elif "forward" in c6:
                print("you come to a dead end you have to go back but on the way back you fall into a trap and die                                               GAME OVER")
            else: 
                print("you decided to take the  path leading behind you as you walk down it it gets colder and tighter  until eventually you are in a shivering crawl after what seems like days of crawling you finally make it out in to a strange land you made it out of the facility but to where? YOU WIN? I guess")
        else: 
            print("you really fumbled GAME OVER")  
                                                   # if you find this I think you may have cheated you cheater      
            


        