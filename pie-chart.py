import  matplotlib.pyplot as plt

labels = 'Slice_0','Slice_1','Slice_2','Slice_3'
sizes = [15,30,45,10]
explode = (0,0.1,0,0) #Explode 
fig1,ax1 = plt.subplots()
ax1.pie(sizes, explode=explode,labels=labels,
    autopct='%1.1f%%',shadow=True, startangle=90)
ax1.axis('equal') #Ensures that pie is drawn as a circle
plt.show()