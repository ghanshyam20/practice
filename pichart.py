import matplotlib.pyplot as plt 

import numpy as np 




y=np.array([25,35,25,15])

mylabels=['Apples',"Bananas",'Cherries',"Dates"]



plt.pie(y,labels=mylabels)

plt.legend(title='Four Fruits')


plt.show()





