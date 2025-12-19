result = 10+5*2;
print(result)

# Airthmatic Operator - add , subs , division , floor, modulus Operator
print("Airthmatic Operator")
x = 10
y = 3
print("add=",(x+y));
print("subs=",(x-y));
print("division=",(x/y)); # give decimal values
print("floor=",(x//y)); # remove values after decimals
print("Modulus=",(x%y)); # remainder
print()
# Comparisions Operators - always give boolean values - Equal to , NOt Equal to  , greater than , less than less than or equal to , grater than or equal to 
print("comparision operators")
print(x==y)
print(x>y)
print(x<y)
print(x>=y)
print(x!=y)
print(x<=y)
print()
print("Logical Operators")
#Logical Operator -> and  all condition must be true , or  atleast one condition must be true , not reverse output
age = 20 ;
is_student = True;

print(age>20 and is_student)
print(age < 20 or is_student)
print(not is_student)
 # Assisgment Operators 
z = 10;
z+=10;
print(z)
z-=-1
print(z)

print()
# identity Operator - is - return true if both object have same memory locations and is not return vice versa of is operator
l = [1,2,3]
m =l 
n = 2
print(l is m)
print(l is n)

print()
# memberShip Operator -> in - return true if element are in the collection , not in - return true if value isd not in the collection

vegetables = ["bindi", "karala","potato" ]
print("apple"in vegetables)
print("bindi"  in vegetables)
print("bindi" not in vegetables)

check_type = type(vegetables)
print(check_type)

