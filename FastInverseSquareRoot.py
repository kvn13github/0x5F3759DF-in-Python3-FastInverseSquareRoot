import struct

def fast_inverse_sqrt(number):
    # Convert the input number to a 32-bit floating point value
    x = float(number)
    
    # Interpret the input number as a 32-bit signed integer
    i = struct.unpack('i', struct.pack('f', x))[0]
    
    # Use the magic number to estimate the square root
    i = 0x5F3759DF - (i >> 1)
    
    # Interpret the estimate as a 32-bit floating point value
    y = struct.unpack('f', struct.pack('i', i))[0]
    
    # Use Newton's method to refine the estimate
    y = y * (1.5 - 0.5 * x * y * y)
    
    # Return the reciprocal square root
    return 1 / y

# Get user input for the number to calculate the inverse square root of
number = float(input("Enter a number to calculate the inverse square root of: "))

# Calculate the inverse square root using the fast inverse square root algorithm
result = fast_inverse_sqrt(number)

# Print the result
print("The inverse square root of", number, "is", result)

#--------------------------------------------------------------------------------------------------------------------------
# more info: https://breq.dev/2021/03/17/5F3759DF
# https://en.wikipedia.org/wiki/Fast_inverse_square_root

#more magic numbers: https://en.wikipedia.org/wiki/Magic_number_(programming)
