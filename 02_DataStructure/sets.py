#Mutables , no-duplicates , Unordered , semi-Heterogeneous

# each value is hashed using the hashed functions and hash is used as an index to store the element in memory since hashing does not maintain any order so set is unordered , only hashable objects are stored in the sets only immutable objects but immutable objects like list and dictionaries are not allowed 


s = {1,2,3,4,5,6}

x = hash("hello")
print(x)  #5232907490539105165  when we do hashing of a same objects thenhash value will change since set is unordered
#y = hash(s)
# print(y) -> gives an error cause tuples cant be hashed 


# Create a sample set
my_set = {1, 2, 3}

# add(): Adds a SINGLE element to the set (mutates original, ignores duplicates)
# Time: O(1) average
my_set.add(4)          # Now: {1, 2, 3, 4}
my_set.add(2)          # No change (duplicate ignored): {1, 2, 3, 4}
print(my_set)

# update(): Adds MULTIPLE elements from iterables (lists, tuples, sets, strings)
# Mutates original set, unpacks iterable and adds unique items
my_set.update([5, 6, 1])           # Adds 5,6 (ignores 1): {1, 2, 3, 4, 5, 6}
my_set.update("py")                # Adds 'p','y': {1, 2, 3, 4, 5, 6, 'p', 'y'}
my_set.update({7}, [8])            # Multiple iterables OK
print(my_set)


my_set = {1, 2, 3, 4, 5}

# discard(): Removes element IF it exists (safe, no error if missing)
# Mutates original set
my_set.discard(3)      # Now: {1, 2, 4, 5}
my_set.discard(10)     # No error, no change (10 not present)

# remove(): Removes element (raises KeyError if missing - UNSAFE)
# Mutates original set
my_set.remove(4)       # Now: {1, 2, 5}
# my_set.remove(99)    # Uncomment: Raises KeyError!

# pop(): Removes and RETURNS a RANDOM element (order not guaranteed)
# Mutates original set, useful for arbitrary removal
popped = my_set.pop()  # e.g., removes 1, returns 1: {2, 5}
print(f"Popped: {popped}, Set: {my_set}")

# clear(): Removes ALL elements (mutates to empty set)
my_set.clear()         # Now: set()
print(my_set)


set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# difference_update(): Remove elements found in other set(s) -=
# Mutates set_a to set_a - set_b
set_a.difference_update(set_b)     # Removes 3,4: {1, 2}
print(f"After difference_update: {set_a}")

# intersection_update(): Keep only common elements &=
# Mutates to intersection
set_a = {1, 2, 3}
set_a.intersection_update(set_b)   # Keeps 3: {3}
print(f"After intersection_update: {set_a}")

# symmetric_difference_update(): Toggle elements (in one but not both) ^=
set_a = {1, 2, 3}
set_a.symmetric_difference_update(set_b)  # {1,2,4,5,6}
print(f"After symmetric_difference_update: {set_a}")


original = {1, 2, 3}

# copy(): Shallow copy (new independent set)
copy_set = original.copy()         # {1, 2, 3} (separate object)

# issubset(): True if all elements in other set <=
print({1, 2}.issubset(original))   # True

# issuperset(): True if contains all of other >=
print(original.issuperset({1}))    # True

# isdisjoint(): True if no common elements
print(original.isdisjoint({4, 5})) # True


