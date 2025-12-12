# There are 50,000 iterations in the raw file and that way too much to look at 
# Let's divide the 50K into chunks and take a look at each "checkpoint"
# Let's say every checkpoint = 10K iterations and we will look at the 10Kth plot
# We can still make conclusions about the performance of the product if we're only plotting the data at these checkpoints  

import pandas as pd 
import matplotlib.pyplot as plt

#loads in CSV, prints top of dataset to make sure it arrived safely
df = pd.read_csv(r"C:\Users\Ralph\Desktop\test_engineer_data.csv")
print(df.head())

#this will let us group the dataset, by iteration 
groups = [g for _, g in df.groupby(df.index // 20)] # Every 20 rows, it's a new iteration index 
group_indices = [0, 10000, 20000, 30000, 40000, 49999]  # These are the "checkpoints" I want to look at 
group_idx_names = ['0 Iterations', '10000 Iterations', '20000 Iterations', '30000 Iterations', '40000 Iterations', '49999 Iterations']
# print(groups[20000]['Iteration']) # I was just making sure it was grouped correctly

# I locked the "relative time" of each test since I kept seeing that 8.13 seconds is the same duration of each test iteration all the way to 49999th 
# This makes it easier to plot using the same x-axis 
rel_time = groups[0]['Timestamp (s)']
plt.figure(figsize=(20,8))  #Sorry if you have small screen

# Plots each iteration using a for loop, using the same x-axis
for i, idx in enumerate(group_indices):   
    encoder_motion = groups[idx]['Encoder (deg)']
    plt.plot(rel_time, encoder_motion, marker='o', linestyle='-')

plt.grid(True)
plt.title("Encoder Postion Through Iterations")
plt.xlabel("Time Elapsed (sec)")
plt.ylabel("Encoder Position (deg)")
plt.legend(labels=group_idx_names, loc='center left', bbox_to_anchor=(1,0.5))
plt.tight_layout()  #automatically adjust size based on legend that is outside the plot area
plt.show() 