import pandas as pd 
import matplotlib.pyplot as plt

#loads in CSV, make sure you use a raw string or \\ on windows 
#importing Path and using it doesn't work for some reason
df = pd.read_csv(r"C:\Users\Ralph\Desktop\dummy_dataset.csv")

#prints entire dataset 
print(df.head())

#iloc lets you grab just the index of the column
x = df.iloc[:,0]

plt.figure(figsize=(12,5))  #width = 12 inches, height = 5 inches

#for loop lets you plot all vals 
for i in range(1, len(df.columns)):
    y = df.iloc[:,i]
    plt.scatter(x, y, label=df.columns[i])
    plt.plot(x,y)

#show the plot 
plt.xlabel(df.columns[0])
plt.ylabel("Pressure (psig)")
plt.legend(loc='center left', bbox_to_anchor=(1,0.5))
plt.tight_layout()  #automatically adjust size based on legend that is outside the plot area
plt.show()
