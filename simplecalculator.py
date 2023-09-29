#simple calculator
def cal():
    def add(a,b):
        print(a+b)
    def sub(a,b):
        print(a-b)
    def mul(a,b):
        print(a*b)
    def div(a,b):
        print(a/b)
    def mod(a,b):
        print(a%b)
    a=int(input("Enter the first number :"))
    b=int(input("Enter the second number :"))
    choice=int(input("Enter you choice to perform calculation :"))
    if choice==1:
        add(a,b)
    elif choice==2:
        sub(a,b)
    elif choice==3:
        mul(a,b)
    elif choice==4:
        div(a,b)
    elif choice==5:
        mod(a,b)
    else:
        print("error")
print("welcome to our calculator")
print("Menu")
print("1.Addition")
print("2.subraction")
print("3.Multiplication")
print("4.Division")
print("5.module")
choice1=input("Enter y to start calculation :")
if choice1=="y":
    cal()
else:
    print("Thankyou")
while True:
    choice2=input("Enter 1 to continue calculation :")
    if choice2=="1":
        cal()
    else:
        print("!")
        break
      
      
