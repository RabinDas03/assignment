def LargestNumber(a,b):
  if (a>b):
    return a
  else:
    return b

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
LargestNum=LargestNumber(number1,number2)
print(f"{LargestNum} is largest number.")