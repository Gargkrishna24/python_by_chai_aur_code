# immutable , Duplicate value , Ordered , Heterogeneous

my_tuple = (1, 2, 3, 4, 4, 5, 6, True,print("hello"),(2,3,4,5,66)) 
for i in my_tuple:
    print(i)
    
# tuple have only 2 Specific inbuilt method 

t = (1, 2, 2, 3, 4, 2)
print(t.count(2))    # 3
print(t.index(2))    # 1 (first occurrence)
#print(t.index(5))  # ValueError!

a,b,c,d=(1,2,3,4)
print(a,b,c,d)

a = (1) # pack
b = (1,) # unpack
print(a,type(a),b,type(b))

numbers = 1, 2, 3     
print(type(numbers)) # tuple
print(f"orginal value of a  and b is {a} {b} ")
a, b = b, a          # a=10, b=5 (no temp variable needed!)
print(f"after swapping the  value of a  and b is {a} {b} ")
