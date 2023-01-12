from random import randint


def readLine_Print(start, end):  # helper function
    # opens file and gets lines in range
    with open("hangman-ascii.txt", encoding='utf8') as file:
        line_range = file.readlines()[start:end]
    for i in range(len(line_range)):
        # prints all those lines
        print(line_range[i].strip('\n'))


def displayIntro():
    # displays intro screen
    readLine_Print(0, 23)


def displayEnd(result):
    # checks whether player lost or won
    if result:
        readLine_Print(190, 203)
    else:
        readLine_Print(99, 112)


def displayHangman(state):
    # depended on the remaining lines, prints hangman
    if state == 5:
        readLine_Print(24, 32)
    elif state == 4:
        readLine_Print(37, 45)
    elif state == 3:
        readLine_Print(50, 58)
    elif state == 2:
        readLine_Print(63, 71)
    elif state == 1:
        readLine_Print(76, 84)
    else:
        readLine_Print(89, 97)
    print()


def getWord():
    # gets random lines from function
    ran_int = randint(0, 854)
    with open("hangman-words.txt", "r") as file:
        return file.readlines()[ran_int]


def valid(c):
    # checks whether input is valid or not
    return c.isalpha() and c.islower() and len(c) == 1 and c.isascii()


def play():
    user_input_set = set()
    cur_word = getWord().strip()
    temp_word = cur_word
    displayed_word = "-" * len(cur_word)
    lives = 5  # give 5 lives

    while True:
        displayHangman(lives)  # display hangman

        print("Guess the word:", displayed_word)

        user_char = input("Enter the letter:\n").strip()

        while not valid(user_char) or user_char in user_input_set:  # if user input is not valid ask for it again
            if not valid(user_char):
                print("Invalid input! Please, enter one lowercase English letter")
            elif user_char in user_input_set:
                print("You already tried that letter, try another one")
            user_char = input("Enter the letter:\n")

        user_input_set.add(user_char)

        if user_char not in cur_word:
            lives -= 1

        elif user_char in temp_word:  # if user input is in the word
            temp_word = temp_word.replace(user_char, "")  # remove char from the temp
            for i in range(len(cur_word)):
                if cur_word[i] == user_char:
                    displayed_word = displayed_word[:i] + user_char + displayed_word[i + 1:]
                    # replace "-" with corresponding word

        if lives == 0:  # depending on the result, return true or false
            displayHangman(lives)
            print("Hidden word was: ", cur_word)
            return False
        elif "-" not in displayed_word:
            print("Hidden word was: ", cur_word)
            return True


def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)
        player_decision = input("Do you want to play again? (yes/no) ")
        while player_decision != "yes" and player_decision != "no":
            player_decision = input("Do you want to play again? (yes/no) ")
        if player_decision == "no":
            break


if __name__ == "__main__":
    hangman()