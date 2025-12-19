# 1. Numeric type - int number , flaot nber , complex nber

a = 3 
b = 10.20 # if anything in p/q is always a float number
c =20+4j
d = 20/30
print(a,b,c)
print(type(a) ,type(b) ,type(c) , type(d))

# 2. Boolean - True , False -> for logical operations
is_raining =  True
is_sunny =  False;
print(is_raining,is_sunny)

#3.  None - For Absence of the Value;

result = None;
print(result) 

#4.  Sequence - String -> mutable , list-> mutable , Tuple->unmutable
string  = " Hello ! My name is krishna"
print(string)

# String slicing => a[start:end:difference]
slicing=string[-8:-1:1]
print(slicing)


list =  ['data ', 'data2','data3']
print(list)

tuple={is_raining,is_sunny,is_raining}
print(tuple)

# set - Mutable ,  FrozenSet - UnMutable

set = {1,2,3,4,3,3,3,3}
print(set)

frozenset = frozenset([1,2,3,4,4,4,4])
print(frozenset)
 # Pair - dictinary 
 
dictionary = {
  'name': 'Gopal',
  'age':100,
  'none': None
}
print(dictionary)

# type Casting 
"""
int(),float(),str().bool()
"""

x = -123
xstr = str(x)
xbool = bool(x)
xfloat=float(x)
print("change int into str",type(xstr),xstr)
print("change int into float",type(xfloat),xfloat)
print("change int into bool",type(xbool),xbool)  # it only return false when we intialse the x with 0 otherwise this line return true

y = True 
yint = int(y)
yfloat = float(y)
ystr = str(y)
print("changing bool into int : ",type(yint),yint)
print("changing bool into float : ",type(yfloat),yfloat)
print("changing bool into str : ",type(ystr),ystr)

z = "krishna Garg"
#zint = int(z) ======>>>we cant do this
#zfloat = float(z)   ======>>>we cant do this
zbool = bool(z)

#print("changing str into int : ", type(zint),zint)    ======>>>we cant do this
#print("changing str into float : ", type(zfloat),zfloat)    ======>>>we cant do this
print("changing str into bool : ", type(zbool),zbool)
