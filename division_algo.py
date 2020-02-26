#!/usr/bin/env python3
# division_algo.py - Uses the division algorithm to find the 
# greatest common divisor of two integers and shows the 
# intermediate steps in tabular form

from prettytable import PrettyTable

# Number 1. a = 28056, b = 3032
# Number 2. a = 48432, b = 47376

def division_algorithm(a, b):
    # Set up table headers
    table = PrettyTable(['u_1', 'v_1', 'u_2', 'v_2', 'u_3', 'v_3', 'q'])
    
    # Populate the first row of the table
    # The first row is always 1, 0, 0, 1, max(a,b), min(a,b), 0
    currentRow = [1, 0, 0, 1, max([a,b]), min([a,b]), 0]
    table.add_row(currentRow)

    # Use division algorithm to populate subsequent rows
    while currentRow[5] != 0: # Exit condition is when v_3 == 0
        # new u = old v
        u_1 = currentRow[1]
        u_2 = currentRow[3]
        u_3 = currentRow[5]
        # q = div part of quotient of u_3 and v_3
        q = currentRow[4] // currentRow[5]
        # new v = old u - (current q)(old v)
        v_1 = currentRow[0] - q * currentRow[1]
        v_2 = currentRow[2] - q * currentRow[3]
        v_3 = currentRow[4] - q * currentRow[5]
        newRow = [u_1, v_1 , u_2, v_2, u_3, v_3, q] 
        
        # append row to the table and set it to the current row
        table.add_row(newRow)
        currentRow = newRow
    
    # pull the gcd, x, and y values from the last row
    gcd = currentRow[4]
    x = currentRow[0]
    y = currentRow[2]

    # print the table
    print(table)
    print("gcd(%d, %d) = %d" %(a, b, gcd))
    print("x = %d, y = %d" %(x, y))

print("Problem 1: a = 28056, b = 3032")
division_algorithm(28056, 3032)
print()
print("Problem 2: a = 48432, b = 47376")
division_algorithm(48432, 47376)
print()
division_algorithm(48, 56)


