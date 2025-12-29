def hello():
  print("This is the hello fuction so i am doing hello")
  
#hello()

# Paramaterized Functions --> the thing you accept is para meter and the thing you provide is aargument

# Types of Argument

#1. Positinal argument 

a = float(input("Enter the Value of a -> "))
b = float(input("Enter the Value of b -> "))
def sum(a,b):
  print(f"The sum of two Number is {a+b}")
sum(a,b)



# 2 . Default Argument

def substract(x,y=25):
  print(f"the Subs of two number is {x-y}")
substract(34,89)

# 3 . KeyWord Argument

def say_hello(name , age):
  print(f"My name is {name} and i am {age}")
say_hello(age=22,name="Krishna garg") # Known as KeyWord Argument