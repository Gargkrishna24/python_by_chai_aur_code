# Variable scope in Python determines where a variable can be accessed and modified, following the LEGB rule for lookups

# Local Scope
#  Variables defined inside a function are local and inaccessible outside it.

#  Global Scope
#Variables defined at the module level are global and readable from anywhere, but modification inside functions requires the global keyword.

# Enclosing (Nonlocal) Scope
# In nested functions, inner functions can read outer variables; use nonlocal to modify them.

# Built-in Scope
# Python's built-ins like print or len are always available unless shadowed by locals.

