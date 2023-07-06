import time
import random
import matplotlib.pyplot as plt


def bsort(a):
    """
    Perform Bubble Sort on the given array.
    """
    n = len(a)
    
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        
        if not swapped:
            break
                
                
def main():    
    """
    Main function to generate data, measure execution time, and plot the results.
    """
    
    # Notify users about the potentially long runtime
    print("Please wait. The script may take some time to execute.")
   
    num_elems_list = [i for i in range(1000, 20001, 1000)]  # Number of elements in the array
    execution_times = []
    
    for elem_nums in num_elems_list: 
        # Generate a random array of specified length
        randomly_generated = [random.randrange(1000000) for _ in range(elem_nums)]
        
        # Measure the execution time of bubble sort
        start_time = time.time()
        bsort(randomly_generated)
        end_time = time.time()
        
        execution_times.append(end_time - start_time)
        
    # Create plot with custom styling
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(num_elems_list, execution_times, linewidth=2, color='blue', label='Times vs Num of Elements')
    
    ax.set_title('Time mesaurements')
    ax.set_xlabel('num. of elements')
    ax.set_ylabel('Time in sec')
    ax.grid(alpha=.5)
    ax.legend()
    
    # Show plot
    plt.show()


if __name__ == '__main__':
    main()
