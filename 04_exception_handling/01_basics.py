a = int(input("Enter the Value of a -> "))
try:
  print(10/a)
#except ZeroDivisionError:
  #print("You cant divide the value of a with Zero ")
except Exception as err:
  print(f"Sorry there is an Error {err}")
else:
  print("There is no error")
finally:
  print("i will run no matter what")
print("OK !! Division is done ")

age = int(input("Enter the age = "))

if age >10 or age < 18 :
  raise ValueError("Your Age must be between 10 and 18")
else:
  print("Welcome to the clud ")
print("The clud will start soon")