#
#
# Applied Stochastic Analysis HW1 Sixian(Suavis) Liu
#
# This code will compute the sample average of the of N i.i.d. exponential 
# random variables with mean 1, by generating the uniform distribution and 
# take -log(U).
# This program will print out the average and get a histogram for the density 
# of the random variables. 
# The references I used are Geeksforgeeks and Stochstic project last semester.
#
#
#################################################################################
from   numpy.random import Generator, PCG64     # numpy randon number generator routines
import numpy             as np
import matplotlib.pyplot as plt
import random           



# set up the parameters
a = 0                       # lower bound of the uniform dist.
b = 1                       # upper bound of the uniform dist. 
N = 1000                    # number of r.v.
nlist = np.zeros(N)         # store the r.v. for exponential dist.
nbins = 30                  # number of bins
blist = np.zeros(nbins)     # store the number of elements in each bin
binC = np.zeros(nbins)      # bin center for the histogram
avg = 0

# Generate the uniform distribution on (0,1) and take -log(U)
for k in range(N):
    nlist[k] = (-1)*np.log(random.uniform(a, b))

# Compute the average
avg = sum(nlist)/N

# Generate the histogram
max = max(nlist)
min = 0
dT = (max - min)/nbins

# count the number of each bin
for ii in range(N): 
    nk = nlist[ii]
    if (nk < max):         # make sure bk < nbins 
        bk = int(nk/dT)
        blist[bk] += 1

# set the value for bin center 
for jj in range(nbins):    
    binC[jj] = (jj+1)*dT/2


# Print the average
infoLine = "\n The average of {N} exponential random variable is {avg:10.3e}"
infoLine = infoLine.format( N = N, avg = avg)
print(infoLine)

# Plot the histogram
fig, ax = plt.subplots()                                 
ax.plot(binC, blist, 'bo')    
ax.legend()                                            
ax.set_ylabel('p')                                       
ax.set_xlabel('x')
title = "Monte Carlo Density Histogram" 
title = title +infoLine
ax.set_title(title)
ax.grid()                                                                              
plt.show()
    
