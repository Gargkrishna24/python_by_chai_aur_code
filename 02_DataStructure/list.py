# Mutable - objects values might be change after the creation of it.
# Duplicate - same vlaues occur multiple times 
# ordered - lsit maintain the Squence as they were inserted. access element by its index
# Heterogeneous - we can hiave multiple types of data structure
import math
a = [12,13,14,15,36.6 ,True]


def print_list():
  for i in range(len(a)):
    print(a[i])
    
#print_list()


a.append("krishna Garg")
a.insert(3,"Vaishnavi")
#print_list()

a.remove("Vaishnavi") # First Apperance will delete 
#print_list()


l = [0,-1,-2,-3,0,1,2,3,4,5,-10,-11,-99,8]

def print_positive_negative_number():
  for i in l:
    if i >= 0:
      print(i)
    else:
      print(i)
#print_positive_negative_number()

list = [23,45,67,89,0,12,34]
def sum_of_lst():
  sum = 0 
  for i in list:
    sum =sum + i
  return sum
#print(sum_of_lst())

# Find Maximum Element in the list
lst = [0,12,34,56,2,-5,98,8888,990000,-3,-5,-7]
def max_element(lst):
    if not lst:  # Handle empty list
        return None
    maximum = lst[0]
    for i in lst[1:]:
        maximum = max(maximum, i)
    return maximum
#print(max_element(lst))

