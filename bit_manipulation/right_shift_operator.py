# Right Shift :

# Denoted as : >>

# Eg: x>>y (x: first operand, y: second operand)

# Takes two numbers, right shifts the bits of the first operand, 
# the second operand decides the number of places to shift. 
# In other words right shifting an integer “x” with an integer “y” 
# denoted as ‘(x>>y)‘ is equivalent to dividing x with 2^y. 

# eg: lets take x=32; which is 100000 in Binary Form.

# Now, if “x is right-shifted by 2” i.e x=x>>2 then x will become x=x/(2^2). 
# Thus, x=32/(2^2)=8 which can be wriiten as 1000.


# Right Shift evaluates to x / 2^y
# Where the x is the value on the left handside of the operator
# and y being used as the power is the value on the right handside of the operator


# So Lets look at the following evaluation to add more context
# Remember this x * 2^y
# 1. Given 100 >> 2  evaluates 4 / 2^2
# 2. Given 64  >> 1  evaluates 1 / 2^1
# 3. Given 124 >> 2  evaluates 2 / 2^2
# 4. Given 96  >> 2  evaluates 5 / 2^2

print(100 >> 2) #25 
print(64  >> 1) #32
print(124 >> 2) #31
print(96  >> 2) #24