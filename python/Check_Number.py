def check_number(n):
  if(n>0):
    print(f"{n} is a Possitive Number.")
  elif(n<0):
    print(f"{n} is a Negative Number.")
  else:
    print(f"{n} is Zero.")


user_input = int(input("enter a number: "))
check_number(user_input)