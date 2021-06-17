#Left Shift :

# Denoted as : << 
# Eg: x<<y (x: first operand, y: second operand)
# Takes two numbers, left shifts the bits of the first operand, the second operand decides the number of places to shift.
# Or in other words left shifting an integer “x” with an integer “y” 
# denoted as ‘(x<<y)’ is equivalent to multiplying x with 2^y (2 raised to power y). 
# eg: lets take x=22; which is 00010110 in Binary Form.
# Now, if “x is left-shifted by 2” 
# i.e x=x<<2 then N will become x=x*(2^2). 
# Thus, x=22*(2^2)=88 which can be wriiten as 01011000.

# Leftwise Shift evaluates to x * 2^y
# Where the x is the value on the left handside of the operator
# and y being used as the power is the value on the right handside of the operator


# So Lets look at the following evaluation to add more context
# Remember this x * 2^y
# 1. Given 4 << 3  evaluates 4 * 2^3
# 2. Given 1 << 2  evaluates 1 * 2^2
# 3. Given 2 << 2  evaluates 2 * 2^2
# 4. Given 5 << 3  evaluates 5 * 2^3
# 5. Given 3 << 9  evaluates 3 * 2^9

print(4 << 3) #32 
print(1 << 2) #4
print(2 << 2) #8
print(5 << 3) #40
print(3 << 9) #1536`