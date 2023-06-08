---

1. Write the sort_cards function that sorts the cards received as a parameter in ascending order in a game where
cards are created and distributed in a class.


    def sort_cards(cards):
        pass

The function sorts the card list received as a parameter. The function has no return value (i.e. None).
Here is the code for the part done in the class:

    import random
    
    def create_deck():
        types = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
        numbers = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
    
        deck = []
        for number in numbers:
            for type in types:
                deck.append(type + '-' + number)
    
        return deck
    
    def distribute_deck(deck):
        cards = ([], [], [], [])
    
        for i in range(len(deck)):
            cards[i % 4].append(deck[i])
    
        return cards
    
    deck = create_deck()
    random.shuffle(deck)
    print(deck)
    
    north, east, south, west = distribute_deck(deck)
    print(north)
    print(east)
    print(south)
    print(west)

The point values of the cards are from low to high as follows:

    types = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

For example, the lowest card is 'Spades-2' and the highest card is 'Clubs-Ace'.

---

2. Write a function called "increasing_numbers" that takes a string consists of numerical characters as a parameter
and returns a list of integers created from the numeric characters in the string, in increasing order.

    
    def increasing_numbers(s):
        pass

The function should obtain the next value made up of the minimum number of characters possible, greater than the
previous value. The example numbers entered as parameters and the lists that the function should return are given below:

    '0'                         [0]
    '045349'                    [0, 4, 5, 34]
    '77777777'                  [7, 77, 777]
    '19510899'                  [1, 9, 51, 89]
    '3141592653589793238462643' [3, 14, 15, 92, 653, 5897, 9323, 84626]

---

3. Write a function called "consecutive_total" that returns the largest sum of n consecutive numbers in a list,
along with the starting index of that sequence, as a tuple.

        
    def consecutive_total(a, n):
        pass

The first parameter of the function is the list in question, and the second parameter specifies the amount of
consecutive numbers. For example, if the list is [3, 8, 6, 9, 4, 7, 5] and the consecutive amount is 2, the highest
consecutive sum is 6 + 9 = 15. The value 6 is at the second index of the list. In this case, the function should
return (15, 2) as a tuple. If there are not enough elements in the list for the given consecutive amount, the function
should stop at that point. If there are multiple instances of the highest consecutive sum, the function should return
the sequence that appears earlier in the list.

---

4. Let's assume that a hypothetical machine is located at position (0, 0) in a Cartesian coordinate system.
The following commands are sent to this machine:


    Up n
    DOWN n
    Left n
    RigHT n

Where n is a number. The commands are not case-sensitive. Please write a function called move_machine that takes a
text as a parameter. The text consists of the above commands. The commands are separated in the text by ';' characters.
The function should take this command text and return a tuple in the form (x, y) indicating the machine's new position.
You can test the program with the following code:

    def move_machine(s):
        pass
    
    s = 'Up 4 ; Down 2 ; Down 3; Left 4; Up 2'
    x, y = move_machine(s)
    
    print(x, y)

---

5. The means of random samples taken from a population tend to be normally distributed. This is called the central
limit theorem in statistics. The more sample numbers there are and the larger the sample size, the closer the sample
averages are to a normal distribution. This applies regardless of what the distribution of the population is.

Write a program that tests the central limit theorem as follows:

* Let the numbers between 0 and 10_000 represent the population.
* Set the sample size to 5.
* Each time, calculate the averages by generating 5 random numbers between 0 and 10000 (i.e., by randomly sampling from
the population). You can use the '**random.sample**' function to do this. For example:
    

    population = range(0, 10000)
    sample = random.sample(population, 5)

* Perform this process a certain number of times (e.g., 5000 times).
* Create a list of 10 elements and reset it. Each element of the list represents the frequency range [0-1000],
[1000-2000], [2000-3000], ... . Increase the element of the list corresponding to the range the obtained sample
average belongs to. As a result of these operations, you will obtain a list of frequency numbers. Plot this as a
histogram to observe the normal distribution. The histogram will be drawn with X characters that are proportional to
the number of elements in each row. For example:


    XX
    XXXXX
    XXXXXXXX
    XXXXXXXXXXX
    XXXXXXXXXXXXXXX
    XXXXXXX
    XXXXX
    XXX
    XX
    X

Assume that the frequency numbers range from 0 to 1000. In this case, each X may represent 30 frequency numbers.
You will determine how many samples you will take in total and how many frequency numbers each X character
will represent.

---

6. To solve the central limit theorem question above:

Again, let the numbers between 0 and 10000 represent the population.

* Set the sample size to 5.

* Each time, calculate the averages by generating 5 random numbers between 0 and 10000 (i.e., by randomly sampling from
the population). Perform this process a certain number of times (e.g., 5000 times). Add the averages to a list.
(i.e. A list containing 5000 elements should be obtained.)

* Use the following pyplot function to draw the histogram:

    
    import matplotlib.pyplot as plt
    
    plt.hist(a, 10)

In this, 'a' is the list containing the sample averages, and 10 is the number of frequency intervals the histogram
should be made of. (If you are doing the example in PyCharm, you should also call the plt.show() method.)

---

7. Create a list in the form of x values from -10 to 10 with increments of 0.1. Use the Gaussian function to obtain
the y values from these values and also collect these values in a list. Use the plot function of the Matplotlib
library to plot the curve as follows:

    
    import matplotlib.pyplot as plt
    
    plt.plot(x_list, y_list)

If you are doing the example in PyCharm, you will also need to call the plt.show() method at the end.

The standard normal distribution (also known as the Gaussian or normal distribution) is described by the probability
density function:

    f(x) = 1/(sqrt(2*pi) * sigma) * exp(-1/2 * (x-mu)^2/sigma^2)

    where:
    x = random variable
    mu = mean (set to 0)
    sigma = standard deviation (set to 1)
    pi = 3.14159
    e = 2.71828

You can directly obtain the numbers of Pi and E from the math module using the math.pi and math.e expressions.

---