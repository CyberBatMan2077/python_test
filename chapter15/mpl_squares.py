import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.title("Square Numbers",fontsize = 24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square OF Value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=15)

#plt.scatter(2,4,color=([1,0,0]),edgecolor='black')
#plt.show()

#homework  15-1
x_value = range(1, 6)
y_value = [x**3 for x in x_value]
#plt.plot(x_value,y_value)
#plt.show()

x1_value = range(1,5001)
y1_value = [x**3 for x in x1_value]
#plt.plot(x1_value,y1_value)
#plt.show()

#homework  15-2
plt.scatter(x1_value,y1_value,c=y1_value,cmap=plt.cm.Blues)
plt.show()
