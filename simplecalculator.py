#simple calculator
def getting_choice():
    def add(a,b):
         print(f"Answer= {a+b}")
    def sub(a,b):
         print(f"Answer= {a-b}")
    def mul(a,b):
        print(f"Answer= {a*b}")
    def div(a,b):
        try:
            print(f"Answer= {a/b}")
        except ZeroDivisionError:
            print("cannot divided the values by zero")
    def mod(a,b):
        try:
            print(f"Answer= {a%b}")
        except ZeroDivisionError:
            print("cannot divided the values by zero")
    frt_num=float(input("Enter the first number :"))
    sec_num=float(input("Enter the second number :"))
    menu_choice=int(input("Enter you choice to perform calculation :"))
    a,b=frt_num,sec_num
    try:
        if menu_choice==1:
           add(a,b)
        elif menu_choice==2:
           sub(a,b)
        elif menu_choice==3:
           mul(a,b)
        elif menu_choice==4:
           div(a,b)
        elif menu_choice==5:
           mod(a,b)
        else:
           print("Given value",menu_choice,"is not a valid menu number")
    except ValueError:
        print("value error")
def menu():
    menu_options=["Menu",
                  "1.Addition",
                  "2.subraction",
                  "3.Multiplication",
                  "4.Division",
                  "5.modulo"]
    for option in menu_options:
        print(str(option))
print("Calculator")
choice1=input(f"To perform  calculation [yes \ no]:")
if choice1.upper()=="YES":
    menu()
    getting_choice()
    while True:
        getting_choice_reprefomance=input(f"Do you want to perform another calculation[yes \ no] :")
        if getting_choice_reprefomance.upper()=="YES":
            menu()
            getting_choice()
        else:
            print("exit!")
            break
else:
    print("Exit!")
      
      
