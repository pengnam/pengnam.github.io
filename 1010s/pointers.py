##################
#Order of Growth #
##################

n = 100000000000000000000
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


def help(x):
    if x == 0:
        return x
    else:
        return x + help(x-1)

#Time: O(n)
#Space: O(n)

i = 1
while(i<n):
    print(i)
    i *= 2
#Time: O(logn)
#Space: O(1)

"""
Helpful sites (If you don't believe me):
https://stackoverflow.com/questions/35180377/time-complexity-of-string-slice
https://stackoverflow.com/questions/33191470/difference-in-complexity-of-append-and-concatenate-for-this-list-code
"""
