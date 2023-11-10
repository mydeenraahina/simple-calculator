#simple calculator
def cal_main():
    def add(a,b):
        print(f"Answer= {int(a+b)}")
    def sub(a,b):
        print(f"Answer= {int(a-b)}")
    def mul(a,b):
        print(f"Answer= {int(a*b)}")
    def div(a,b):
        print(f"Answer= {int(a/b)}")
    def mod(a,b):
        print(f"Answer= {int(a%b)}")
    frt_num=input("Enter the first number :")
    sec_num=input("Enter the second number :")
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
print("Calculator")
print("Menu")
print("1.Addition")
print("2.subraction")
print("3.Multiplication")
print("4.Division")
print("5.module")
choice1=input(f"Enter your choice to start calculation [yes \ no]:")
if choice1=="yes":
    cal_main()
    while True:
        getting_choice_reprefomance=input(f"Do you want to perform another calculation[yes \ no] :")
        if getting_choice_reprefomance=="yes":
            cal_main()
        else:
            print("exit!")
            break
else:
    print("Exit!")
      
      
