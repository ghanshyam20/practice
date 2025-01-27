#what is matplotlib ???



#Matplotlib is a low level graph plotting library in python that servers as a visualixation

# the command to install matplotlib is pip install matplotlib


# import matplotlib


# print(matplotlib.__version__)

#most of the matplotlib utilities lies under the pyplot submodule and are usually imported uder the plt alias:



import matplotlib.pyplot as plt




import numpy as np



xpoints=np.array([0,6])

ypoints=np.array([0,250])


plt.plot(xpoints,ypoints)

plt.show()

