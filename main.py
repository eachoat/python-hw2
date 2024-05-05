# Write a Python function called max_num()to find the Max of three numbers.

def max_num(num1, num2, num3):
    return max([num1, num2, num3])

print(max_num([3,5,2]))




# Write a Python function called mult_list()  to multiply all the numbers in a list.

def mult_list(lst):

    if len(lst) < 1:
        return lst

    product = lst[0]

    if len(lst) > 1:

        for i in lst [1:]:
            product = product * i
    
    return product

print(mult_list([1,2,3]))






# Write a Python function called rev_string() to reverse a string.

def rev_string(input_string):
    return input_string[::-1]









# Write a Python function called num_within() to check whether a number falls in a given range.


    # The function accepts the number, beginning of range, and end of range (inclusive) as arguments.

    # Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False


def num_within(number, start, end):
    return start <= number <= end






  # Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.


  # Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.


def pascal(n):
    for i in range(n):
        num = 1 
        for j in range(i + 1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)
        print()