# x=int(input("Enter a number:"))
# y=int(input("Enter 2nd number:"))
# if x>y:
#     print("X is greater than y")
# elif x==y:
#     print("X and y has same value")
# else:
#     print("Y is greater than x")




# WAP TO enter user age and check if he is eligible to vote or not 18 -60


# input=int(input("enter your age:"))
# if input<18:
#     print("You are not eligible to vote")
# elif input>=18 or input<60:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible")

# x,y,z=10,20,30
# if x>y:
#     if y>z:
#         print("x is greater than y and z")
#     else:
#         print("Z is greater than x and y")

# else:
#     if y>z:
#         print("Y is greater than z and y")
#     else:
#         print("Z is greater than x and y")



# # pin: 12345, amount: 10000
# amount=10000
# pin=int(input("Enter the pin:"))
# if pin==12345:
#     print("Your amount is 10000")
#     withdraw=int(input("Enter the amount you want to winthdraw:"))
#     if withdraw>10000:
#         print("Unsufficent balance ")
#     else:
#         # print(f"You have withdrawn {withdraw}")
#         amount2=amount-withdraw
#         print(f"Your new balance is {amount2}")

# else:
#     print("invalid pin")




a=int(input("Enter value1:"))
b=int(input("Enter value2:"))
c=int(input("Enter value3:"))


if a>b:
    if a>c:
        if b>c:
            print(c,b,a)
        else:
            print(b,c,a)
    else:
        exit
elif b>a:
    if b>c:
        if a>c:
            print(c,a,b)
        else:
            print(a,c,b)
    else:
        exit
elif c>a:
    if c>b:
        if b>a:
            print(a,b,c)
        else:
            print(b,a,c)