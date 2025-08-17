age =int(input("Enter your age:"))

if age < 0 :
    print("sorry you are to small for voting.")
elif age < 10 :
    print("sorry you are underaged.")
else:
    print("You can vote")