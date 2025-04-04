Password=input("Enter the Password")
result=[]
if len(Password)>8:
    result.append("True")
    # print(result)
else:
    result.append("False")
    # print(result)

digit=False
for i in Password:
    if i.isdigit():
     digit = True

result.append(digit)

alpha=False
for i in Password:
    if i.isupper():
        alpha = True

result.append(alpha)


if (all(result))==True:
    print("Correct Password")
else:
    print("Wrong Password")

