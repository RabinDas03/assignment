def sum_natural(n):
  total = 0
  for i in range(0,n+1):
    total=total+i
  return total
num = int(input("Enter number:"))
Sum = sum_natural(num)
print(f"The sum is: {Sum}")