import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Initial definitions
flip_count = [] # Number of flips to get two in a row
results_list = [] # Array of results arrays
num_of_sets = 999 # Change value to change how often it loops. 0-999 provides 1000 flips.
timer = 0

#randint(1,3) = random between integer 1 and 2
#integer 1 = Heads
#integer 2 = Tails

# Main loop
while timer <= num_of_sets:

    # Initial flip for test
    results = [np.random.randint(1,3), np.random.randint(1,3)]
    index = len(results) - 1
    
    while not (results[-1]==2 and results[-2]==2): # Check if most recent 2 flips are interger 2 (tails)
        results.append(np.random.randint(1,3)) # Add flips
        
    # Adding on results to lists
    results_list.append(results)
    flip_count.append(len(results))
    
    timer += 1 # Loop counter

# Getting arrays for plotting histogram - this part is not necessary but I thought it would be cool to keep 
bin_count = np.arange(np.min(flip_count), np.max(flip_count) + 1)
hist, edges = np.histogram(flip_count, bin_count) # Histogram function
bin_error = np.sqrt(hist) # Error for counting = root of count

# Plotting histogram 
plt.figure()
plt.bar(edges[:-1], hist, width = 0.8, color = 'red', edgecolor = 'black', yerr = bin_error, capsize = 2)
plt.xlabel('Total Number of Flips')
plt.ylabel('Flip Count')
plt.title('Flip Distribution')

# Plotting table as a .csv file to be exported to Excel
data = {
    'Trial #': range(1, len(flip_count) + 1),
    '# of flips until 2 tails': flip_count
}

df = pd.DataFrame(data)

print("Table of Results")
print(df.head(1000)) #1000 trials

df.to_csv(r'C:\Users\rinra\Downloads\Data Challenge 3\coin_flip_simulation.csv', index=False) #this is for Cake's Computer



# Way to extract and see the longest results array - another cool thing that is not necessary
print('Max was ' + str(np.max(flip_count)) + ' at ' + str(flip_count.index(np.max(flip_count))))
print(results_list[flip_count.index(np.max(flip_count))])

plt.show()