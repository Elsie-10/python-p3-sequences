#!/usr/bin/env python3
# fibonacci sequence sums the previous two numbers
# [0,1] => 0+ 1 next sequence [0,1,1] then [0,1,1,2]
def print_fibonacci(length):
    # length is an argument that tells us how many numbers we want in the sequence.
    if length == 0:
        print ([])
        return
    # if user ask for 0 numbers it prints an empty list and stop using return
    elif length == 1 :
        print([0])
        return
    # if user wants just want 1 number we print [0] then we exit.

    fib =[0,1]
    # creates a list with the first two numbers of the fibonacci sequence
    while len(fib) < length :
    # will continue to loop as long as the length of fib list is less than what the user asked for.
        next_number = fib[-1] + fib [-2]
    # fib[-1] the last number in the list
    # fib[-2] the second last number in the list
    # we add then together to get the next number
        fib.append(next_number)
# add the new number to the end of the list
    print(fib)
    # once the loop is done we print the list of fibonacci number