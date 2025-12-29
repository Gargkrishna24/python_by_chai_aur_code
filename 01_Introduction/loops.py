# Only two types of Loop - while loop(Condition) and for loop(number or range)
#range(start , end , diff)  default values(0,compulsory value,1)
#Break - break the loop means terminate the loop
# continue - skip the current iteration than continue the loop
# In for Loop if break statement is executed then else statment will not be executed if break statement is not executed then else statment will be executed 
"""
a = range(1,20,1)
for i in a:
  print(i)


for i in range(16 ,-5, -1):
  print(i)
  
n = int(input("Enter the digit : "))
for i in range(11):
  print(i*n)
  
# Loops for String

str = input("enter the string: ")
for i in range(len(str)):
  print(str[i])
  
for j in str:
  print(j)
  
  
for i in range(10):
  if(i==15):
    break
  print(i)
else:
  print("this statment is not executed ")
  
for i in range(10):
  if(i==9):
    continue
  print(i)
else:
  print("this statment is not executed ")
  
x = int(input("enter the number that you want to add till that nber : "))
sum=0
for i in range(x+1):
  sum=sum+i
print(sum)
"""

m = 256
while m>0:
  print(m%10)
  m=m//10
