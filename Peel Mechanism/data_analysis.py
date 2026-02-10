# There are 50,000 iterations in the raw file and that way too much to look at 
# Let's divide the 50K into chunks and take a look at each "checkpoint"
# Let's say every checkpoint = 10K iterations and we will look at the 10Kth plot
# We can still make conclusions about the performance of the product if we're only plotting the data at these checkpoints  

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import statistics as stat
from prettytable import PrettyTable

#loads in CSV, prints top of dataset to make sure it arrived safely
df = pd.read_csv(r"C:\Users\Ralph\Desktop\test_engineer_data.csv")
# print(df.head())
#this will let us group the dataset, by iteration 
groups = [g for _, g in df.groupby(df.index // 20)] # Every 20 rows = 1 "group" 
group_indices = [0, 10000, 20000, 30000, 40000, 49999]  # These are the "checkpoints" I want to look at 
group_idx_names = ['0 Iterations', '10000 Iterations', '20000 Iterations', '30000 Iterations', '40000 Iterations', '49999 Iterations']
# print(groups[20000]['Iteration']) # I was just making sure it was grouped correctly

def accuracy_analysis():
    # This tabulates the "drift" from target positions of 0 deg and 4 deg at motion start and end  
    table = PrettyTable(group_idx_names)
    table.title = "End-point Accuracy Over Cycles ('Iterations')"

    temp_list_1 = []
    temp_list_2 = []

    for i, idx in enumerate(group_indices):
        measured_min = groups[idx]['Encoder (deg)'].min()
        drift_at_min = measured_min - 0
        temp_list_1.append(drift_at_min)
    for i, idx in enumerate(group_indices):
        measured_max = groups[idx]['Encoder (deg)'].max()
        drift_at_max = measured_max - 4
        temp_list_2.append(drift_at_max)

    results_list_1 = np.array(temp_list_1)
    results_list_2 = np.array(temp_list_2)

    table.add_row(results_list_1)
    table.add_row(results_list_2)
    table.add_column("Metric", ["Drift at 0deg", "Drift at 4deg"])
    
    print(table)

def repeatability_analysis():
    # We can look at the position of the hinge encoder at a specific time
    # Let's look at the position when motion is at max 
    temp_list = []
    for i, idx in enumerate(group_indices):
        positon_near_4 = groups[idx]['Encoder (deg)'].max()
        temp_list.append(positon_near_4)

    std_dev = stat.stdev(temp_list)
    variance = stat.variance(temp_list)

    print(f"Standard deviation at motion max: {std_dev} deg")
    print(f"Variance at motion max: {variance}")

def plot_data():
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

if __name__ == "__main__":
    accuracy_analysis()
    repeatability_analysis()
    plot_data()
