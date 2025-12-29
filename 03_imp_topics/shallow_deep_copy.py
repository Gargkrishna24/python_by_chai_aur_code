import copy

original = [[1, 2], [3, 4]]  # Nested list

# SHALLOW COPY
shallow = original.copy()
shallow[0][0] = 999
print(original[0])  # [[999, 2], [3, 4]] 😱 CHANGED!

# DEEP COPY  
original = [[1, 2], [3, 4]]  # Reset
deep = copy.deepcopy(original)
deep[0][0] = 888
print(original[0])  # [[1, 2], [3, 4]] ✅ SAFE!
