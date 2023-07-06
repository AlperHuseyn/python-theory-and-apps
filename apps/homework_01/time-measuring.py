import time
import random
import matplotlib.pyplot as plt


def bsort(a):
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
    horizontal_axis = [i for i in range(1000, 20001, 1000)]
    vertical_axis = []
    
    for elem_nums in horizontal_axis:        
        randomly_generated = [random.randrange(1000000) for _ in range(elem_nums)]
        
        t1 = time.time()
        bsort(randomly_generated)
        t2 = time.time()
        
        vertical_axis.append(t2 - t1)
        
    # Create plot with custom styling
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(horizontal_axis, vertical_axis, linewidth=2, color='blue', label='Times vs Num of Elements')
    
    ax.set_title('Time mesaurements')
    ax.set_xlabel('num. of elements')
    ax.set_ylabel('Time in sec')
    ax.grid(alpha=.5)
    ax.legend()
    
    # Show plot
    plt.show()


if __name__ == '__main__':
    main()
