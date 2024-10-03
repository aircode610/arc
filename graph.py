# importing the required module
import matplotlib.pyplot as plt
import numpy as np
# x axis values
x = [1,2,3]
# corresponding y axis values
y = [2,4,1]
  
# plotting the points 
plt.plot(x, y)
  
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

plt.xticks(np.arange(1, 4, 1))
plt.yticks(np.arange(-4, 5, 2))

# giving a title to my graph
plt.title('My first graph!')
  
# function to show the plot
plt.show()