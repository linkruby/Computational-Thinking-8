import random

# Pick a word at random 
word_list = ["loopy","heart","hopes","laugh","trial"]
hidden_word = random.choice(word_list)

#Repeat 
for i in range (6):
    # Guess a word
    Guess_word = input ()
    output = ""

    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    

    #Result
    print(output)
    if output == "🟩🟩🟩🟩🟩🟩":
        print("you win")
        break
print (f"you used {i +1} guesses")