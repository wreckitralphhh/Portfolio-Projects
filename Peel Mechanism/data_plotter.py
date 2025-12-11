# There are 50,000 iterations in the raw file and that way too much to look at 
# Let's assume we set divide the 50K into chunks and take a look at each "checkpoint"
# Let's say every 10K iterations we look at the 10Kth plot

import pandas as pd 
import matplotlib.pyplot as plt

#loads in CSV, make sure you use a raw string or \\ on windows 
#importing Path and using it doesn't work for some reason
df = pd.read_csv(r"C:\Users\Ralph\Desktop\test_engineer_data.csv")

#prints top of dataset, just making sure it arrive safely
print(df.head())

# this will let us group the dataset, by iteration 
groups = [g for _, g in df.groupby(df.index // 20)]

# g0 = groups[0]
# g10k = groups[10000]
# g20k = groups[20000]
# g30k = groups[30000]
# g40k = groups[40000]
# g49k = groups[49999]

group_index = [0, 10000, 20000, 30000, 40000, 49999]
plt.figure(figsize=(12,5))

for idx in group_index:
    g = groups[idx].copy()
    
    # Convert timestamp to datetime if needed
    g['Timestamp (s)'] = pd.to_datetime(g['Timestamp (s)'])
    
    # Compute relative time (seconds)
    g['t_rel'] = (g['Timestamp (s)'] - g['Timestamp (s)'].iloc[0]).dt.total_seconds()
    
    plt.plot(g['t_rel'], g['Encoder (deg)'], label=f'Group {idx}')

plt.xlabel("Relative Time (seconds)")
plt.ylabel("Y Value")
plt.title("Groups Compared on Same X-Axis (Relative Time)")
plt.legend()
plt.tight_layout()
plt.show()

# plt.scatter(x, y, label=df.columns)
# plt.plot(x,y)

# plt.tight_layout()  #automatically adjust size based on legend that is outside the plot area
#plt.show()