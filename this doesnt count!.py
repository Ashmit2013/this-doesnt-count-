try:
    number = int(input("enter a number ONLY: "))
    print("the number enter is:", number)
except ValueError as x:
   print("this doesnt count!:", x)
