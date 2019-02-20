"""
Format for midterms(usually) and concepts tested

    1. Tracing
        - higher order functions(*), function scope
    2. Iteration/Recursion
        - Order Of Growth, writing iteration or recursion
"""



##################
#Order of Growth #
##################

n = 100000000
k = 40000
"""
Lists
"""

x = [i for i in range(n)]
y = [i for i in range(k)]

x + [1]
#O(n)

#You might not need to know this
x.append(1)
#O(1)

#You might not need to know this
x.extend(y)
#O(length of y)


"""
Tuples
"""
x = tuple(i for i in range(n))

x + (1,)
#O(n)

"""
Strings
"""

x = "".join(str(i) for i in range(n))

x[k:]
#O(n)

x + "1"
#O(n)

"""
Loops
"""
for i in range(n):
    print(i)

#Time: O(n)
#Space: O(1)


def recursion(x):
    if x == 0:
        return x
    else:
        return x + recursion(x-1)

#Time: O(n)
#Space: O(n)

i = 1
while(i<n):
    print(i)
    i *= 2
#Time: O(logn)
#Space: O(1)

"""
Trees
"""

def tree(x):
    if x == 0:
        return x
    else:
        return tree(x-1) + tree(x-1)

#Time: O(2^n)
#Space: O(n)

"""
Tips

1) Identify if its recursion/iteration
2) Determine number of for loops, or number of levels of recursion.
3) Determine if there is any nested complexity.
i.e.
for i in range(n):
    #Some O(n) function, called at each iteration of the for loop.

The complexity of the above algorithm is O(n^2)


If all else fails,
count the number of times certain pieces of code will run and see if it scales linearly, above linear or sublinear.


"""



"""
Helpful sites (If you don't believe me):
https://stackoverflow.com/questions/35180377/time-complexity-of-string-slice
https://stackoverflow.com/questions/33191470/difference-in-complexity-of-append-and-concatenate-for-this-list-code
"""
