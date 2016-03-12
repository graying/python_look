"""
# The Fibonacci sequence is defined by the recurrence relation:
#
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

f_1 = 1
fib = 2
f2 = 0
index = 3

while True:
    f2 = fib
    fib = fib + f_1
    f_1 = f2
    index += 1
    print index, fib

    if fib > 10 ** 999:
        print index, fib
        break
