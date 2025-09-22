prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print(prime_numbers[0:4])  # Output: [2, 3, 5, 7]
print(prime_numbers[4:8])  # Output: [11, 13, 17, 19]
print(prime_numbers[:6])   # Output: [2, 3, 5, 7, 11, 13]
print(prime_numbers[5:])   # Output: [13, 17, 19, 23, 29]
print(prime_numbers[-4:])  # Output: [19, 23, 29]
# Slicing examples with a list of prime numbers
print(prime_numbers[::2])  # Output: [2, 5, 11, 17, 23]
print(prime_numbers[1::2]) # Output: [3, 7, 13, 19, 29]# Slicing examples with a list of prime numbers
print(prime_numbers[::-1]) # Output: [29, 23, 19, 17, 13, 11, 7, 5, 3, 2]
print(prime_numbers[3:8:2]) # Output: [7, 13, 19]

prime_tuple = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
print(prime_tuple[0:4])  # Output: (2, 3, 5, 7)
print(prime_tuple[4:8])  # Output: (11, 13, 17, 19)
print(prime_tuple[:6])   # Output: (2, 3, 5, 7, 11, 13)
print(prime_tuple[5:])   # Output: (13, 17, 19, 23, 29)
print(prime_tuple[-4:])  # Output: (19, 23, 29)
# Slicing examples with a tuple of prime numbers    