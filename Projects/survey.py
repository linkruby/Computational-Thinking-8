#start
score = 0
health = 4
secret_score = 0
import sys




print("you are about to take a test on basketball YOU HAVE TO ANSWER IN CAPITAL IT WILL NOT WORK IN LOWER CASE")
print("_________________________________________________________________________")


#Middle

# question 1:
answer = input("Who has more points A) Kobe Bryant or B) Stephen Curry?")
if answer == "A":
	 score += 1
elif answer == "B":
	health -= 1
	if health <= 0:
		print("You failed!")
		sys.exit()
	elif health > 0:
		print(f"you lost health you have {health} health left")

# question 2:
answer = input("Who has more Three Pointers A) Larry Bird or B) Damian Lillard?")
if answer == "A":
	health += -1
	if health <= 0:
		print("You failed!")
		sys.exit()
	elif health > 0:
		print(f"you lost health you have {health} health left")
elif answer == "B":
	score += 1

# question 3:
answer = input("Who has more blocks A) Shaquille O'Neal or B) Giannis Antetokounmpo?")
if answer == "B":
	score += 1
elif answer == "A":
	health += -1
	if health <= 0:
		print("You failed!")
		sys.exit()
	elif health > 0:
		print(f"you lost health you have {health} health left")


# question 4:
answer = input("Who has the most rebounds A) Bill Russel or B) Kareem Abdul-Jabbar?")
if answer == "A":
	score += 1
elif answer == "B":
	health += -1
	if health <= 0:
		print("You failed!")
		sys.exit()
	elif health > 0:
		print(f"you lost health you have {health} health left")
elif answer == "neither" or "wilt":
	secret_score += 1

# question 5:
answer = input("Who has more points A) Kobe Bryant or B) Karl Malone?")
if answer == "A":
	health += -1
	if health <= 0:
		print("You failed!")
		sys.exit()
	elif health > 0:
		print(f"you lost health you have {health} health left")
elif answer == "B":
	score += 1

# question 6:
answer = input("Who is taller A) Giannis Antetokounmpo or B) Shaquille O'Neal?")
if answer == "A":
	health += -1
	if health <= 0:
		print("You failed!")
		sys.exit()
	elif health > 0:
		print(f"you lost health you have {health} health left")
elif answer == "B":
	score += 1

# question 7:
answer = input("Who has more triple doubles A) Nikola Jokic or B) Magic Johnson?")
if answer == "A":
	health += -1
	if health <= 0:
		print("You failed!")
		sys.exit()
	elif health > 0:
		print(f"you lost health you have {health} health left")
elif answer == "B":
	score += 1
	
# question 8:
answer = input("Who Played longer A) Kobe Bryant B) Micheal Jordan?")
if answer == "B":
	health += -1
	if health <= 0:
		print("You failed!")
		sys.exit()
	elif health > 0:
		print(f"you lost health you have {health} health left")
elif answer == "A":
	score += 1

# question 9:
answer = input("Besides Stephen Curry who is on the top three in terms of scoring the most three pointers in a season?")
if answer == "James" or "James harden" or "Harden":
	score += 1
	
else:
	health += -1
	if health <= 0:
		print("You failed!")
		sys.exit()
	elif health > 0:
		print(f"you lost health you have {health} health left")

# end 
if health > 0:
	print(f"You passed you got {score} correct!")
elif secret_score > 0:
	print(f"you passed you got {score} correct! You also found the secret answer so good job!!!")

