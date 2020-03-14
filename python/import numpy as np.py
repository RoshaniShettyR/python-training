import numpy as np
import matplotlib.pyplot as plt
slices= [7,2,8,2,1]
acts =["sleep", "eat", "work", "play","music"]
cols = ['c','m','r','b','g']
pullout = acts.index(input("What to pull"))
tuplex  = np.zeros(len(acts))
tuplex[pullout] = 0.5
plt.pie(slices, labels = acts, colors = cols , startangle=90, shadow = True, explode=(tuplex), autopct  ='%1.1f%%')
plt.title('Works in a day')
plt.show()