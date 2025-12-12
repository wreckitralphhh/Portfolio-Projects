# There are 50,000 iterations in the raw file and that way too much to look at 
# Let's divide the 50K into chunks and take a look at each "checkpoint"
# Let's say every "checkpoint" == 10K iterations and we will look at the 10Kth plot

import pandas as pd 
import matplotlib.pyplot as plt

#loads in CSV, make sure you use a raw string or \\ on windows 
#importing Path and using it doesn't work for some reason
df = pd.read_csv(r"C:\Users\Ralph\Desktop\test_engineer_data.csv")

#prints top of dataset, just making sure it arrived safely
print(df.head())

#this will let us group the dataset, by iteration 
groups = [g for _, g in df.groupby(df.index // 20)] #Every 20 rows, it's a new iteration number 
group_indices = [0, 10000, 20000, 30000, 40000, 49999]  # the 5 groups
group_idx_names = ['0 Iterations', '10000 Iterations', '20000 Iterations', '30000 Iterations', '40000 Iterations', '49999 Iterations']
# print(groups[20000]['Iteration']) # I was just making sure it was grouped correctly

# I locked the "relative time" of each test since I kept seeing that 8.13 seconds is the same duration of each test iteration all the way to 49999th 
# This makes it easier to plot using the same x-axis 
rel_time = groups[0]['Timestamp (s)']
plt.figure(figsize=(12,5))

for i, idx in enumerate(group_indices):
    g = groups[idx].copy()
    print(i)
    print(idx)
    encoder_motion = groups[idx]['Encoder (deg)']
    plt.scatter(rel_time, encoder_motion)
    plt.plot(rel_time, encoder_motion)

plt.xlabel("Time Elapsed (sec)")
plt.ylabel("Encoder Position (deg)")
plt.legend(labels=group_idx_names, loc='center left', bbox_to_anchor=(1,0.5))
plt.tight_layout()  #automatically adjust size based on legend that is outside the plot area
plt.show() 