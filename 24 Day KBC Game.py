# Simple KBC program
text = "★ Kaun Banega CrorePati ★"
print(text.center(60))
name = input("Please Enter you Name : ")
location = input("Where are you from : ")
age = input("Enter you age : ")

print(f"\nToday! We have a person named {name} ,Age = {age} from {location} on the show {text}\n")

print("Welcome !", name, "Ji in KBC")
print("Are you existed to play..... ")
input("Your responce : ")
text = "So,lets start the game !"
print("\n", text.center(60, "•"))
questions = ("(1) Which of the following gods is also known as ‘Gauri Nandan’? ",
             "(2) In the game of ludo the discs or tokens are of how many colours? ",
             "(3) What is the full form of RAM ? ", "(4) Which of the following corresponds to ‘ek bataa do’? ",
             "(5) Which of these terms can only be used for women?")

options = ("(A) Agni\n(B) Indra\n(C) Hanuman\n(D) Ganesha\n", "(A) One\n(B) Two\n(C) Three\n(D) Four\n",
           "(A) Ready Access memory \n(B) Random Access Memory \n(C) Random Across Memory \n(D) None \n",
           "(A) Pura\n(B) Sawa\n(C) Adha\n(D) Pauna\n", "(A) Dirghaayu\n(B) Suhagan\n(C) Chiranjeevi\n(D) Sushil\n")

while True:
    # Question 1
    text = "First question on your Screen for 5000 Rupees ! "
    print("\n", text.center(60, "-"), "\n")
    print(questions[0])
    print(options[0])

    Choise = input("Select your Answer : ")
    choise = Choise.upper()
    if choise == 'D':
        print("Correct! You won the prise amount of ₹5000 \n")
        totalAmount = 5000
    else:
        print("Incorrect ! You lose the game \n")
        break

    # Question 2
    text = "Second question on your Screen for 25000 Rupees ! "
    print("\n", text.center(60, "-"), "\n")
    print(questions[1])
    print(options[1])

    Choise = input("Select your Answer : ")
    choise = Choise.upper()
    if choise == 'D':
        print("Correct! You won the prise amount of ₹25000 \n")
        totalAmount += 25000
    else:
        print("Incorrect ! You lose the game \n")
        break

    # Question 3
    text = "Next question on your Screen for 50000 Rupees ! "
    print("\n", text.center(60, "-"), "\n")
    print(questions[2])
    print(options[2])

    Choise = input("Select your Answer : ")
    choise = Choise.upper()
    if choise == 'B':
        print("Correct! You won the prise amount of ₹50000 \n")
        totalAmount += 50000
    else:
        print("Incorrect ! You lose the game \n")
        break

    # Question 4
    text = "Next question on your Screen for 90000 Rupees ! "
    print("\n", text.center(60, "-"), "\n")
    print(questions[3])
    print(options[3])

    Choise = input("Select your Answer : ")
    choise = Choise.upper()
    if choise == 'C':
        print("Correct! You won the prise amount of ₹90000 \n")
        totalAmount += 90000
    else:
        print("Incorrect ! You lose the game \n")
        break

    # Question 5
    text = "Last question on your Screen for 150000 Rupees ! "
    print("\n", text.center(60, "-"), "\n")
    print(questions[4])
    print(options[4])

    Choise = input("Select your Answer : ")
    choise = Choise.upper()
    if choise == 'B':
        print("Correct! You won the prise amount of ₹150000 \n")
        totalAmount += 150000
    else:
        print("Incorrect ! You lose the game \n")
        break

print(f"\nTotal Amount Earn by {name} Ji is : ₹{totalAmount} \n")
text = "Thank you! Have a nice day "
print(text.center(60, "•"))