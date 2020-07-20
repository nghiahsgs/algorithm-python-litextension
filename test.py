import numpy
a = [[0,1,2],[0,1,2]]
L=[list(x) for x in numpy.array(numpy.meshgrid(*a)).T.reshape(-1,len(a))]
# [[ 1, 4, 7], [1, 5, 7], [1, 6, 7], ....]

print(L)