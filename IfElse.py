x = int(input('Enter the number: \t'))

if x%2==0:
    if x%3==0:
        print("Number is divisible by 2 and 3")
    else:
        print("Number is divisible by 2 only")
        print("x%3= ", x%3)
elif x%3==0:
    print("Number is divisible by 3 only")
else:
    print("Number is not divisible by 2 and 3")
    print("x%2= ", x%2)
    print("x%3= ", x%3)
print("Thank you")