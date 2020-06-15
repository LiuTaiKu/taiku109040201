# TODO
c=eval(input())

if (c%3==0) and (c%5==0):
    print("{:d} is a multiple of 3 and 5.".format(c))
elif (c%3==0):
    print("{:d} is a multiple of 3.".format(c))
elif (c%5==0):
    print("{:d} is a multiple of 5.".format(c))
else:
    print("{:d} is not a multiple of 3 or 5.".format(c))




"""
_ is a multiple of 3 and 5.
_ is a multiple of 3.
_ is a multiple of 5.
_ is not a multiple of 3 or 5.
"""