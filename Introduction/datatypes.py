# 1. Numeric type - int number , flaot nber , complex nber

a = 3 
b = 10.20
c =20+4j
print(a,b,c)
print(type(a) ,type(b) ,type(c))

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