<div align='center'>

<h1>THIS IS A simple calculator USING PYTHON</h1>
<p>This code implements a simple calculator that performs basic arithmetic operations (addition, subtraction, multiplication, division, and modulo). 
  Here's a  working pattern of this code:

User Interaction and Initial Input:

The program starts by asking the user if they want to perform calculations.
If the user enters "yes," it proceeds to the calculator menu; otherwise, it exits.

print("Calculator")
choice1 = input("To perform calculation [yes/no]: ")
Calculator Menu (menu function):

The menu function displays a list of available operations.

def menu():
    menu_options = ["Menu", "1.Addition", "2.Subtraction", "3.Multiplication", "4.Division", "5.Modulo"]
    for option in menu_options:
        print(str(option))
Calculator Logic (getting_choice function):

The getting_choice function prompts the user to enter two numbers and select an operation from the menu.
The user's input is then used to perform the chosen calculation.

def getting_choice():
    # ... (Code for inputting numbers and selecting an operation)
    try:
        if menu_choice == 1:
            add(a, b)
        elif menu_choice == 2:
            sub(a, b)
        elif menu_choice == 3:
            mul(a, b)
        elif menu_choice == 4:
            div(a, b)
        elif menu_choice == 5:
            mod(a, b)
        else:
            print("Given value", menu_choice, "is not a valid menu number")
    except ValueError:
        print("Value error")
User Iteration and Repetition:

After performing a calculation, the user is asked if they want to perform another calculation.
If the user enters "yes," the process is repeated; otherwise, the program exits.

while True:
    getting_choice_reprefomance = input("Do you want to perform another calculation [yes/no]: ")
    if getting_choice_reprefomance.upper() == "YES":
        menu()
        getting_choice()
    else:
        print("Exit!")
        break
Handling Exceptions:

The code includes try-except blocks to handle potential errors, such as a ValueError when converting user input to numbers and a ZeroDivisionError when attempting to divide by zero.

try:
    # ... (Code for performing the calculation)
except ValueError:
    print("Value error")
This structure ensures that the program provides a user-friendly interface for performing calculations, displays a menu of available operations, and handles errors gracefully. The main loop allows the user to perform multiple calculations until they choose to exit.</p>

<h4> <span> · </span> <a href="https://github.com/MydeenRaahia/simple calculator/blob/master/README.md"> Documentation </a> <span> · </span> <a href="https://github.com/MydeenRaahia/simple calculator/issues"> Report Bug </a> <span> · </span> <a href="https://github.com/MydeenRaahia/simple calculator/issues"> Request Feature </a> </h4>


</div>



## :star2: About the Project

## :handshake: Contact

MYDEENRAAHINA - - mydeenraahina862@gmail.com

Project Link: [https://github.com/mydeenraahina/simplecalculator](https://github.com/mydeenraahina/simplecalculator)
