## Question 1

Take a look at the file labeled `data/data2.txt`. Why might we have missing values or values that state "NO SIGNAL" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

We have missing values in this dataset because they were unable to be read or were possibly skipped due to a technical error. The risk of filtering these values out is disregarding them without possibly looking further into why this might be happening. It might not be a technical error and instead there might be an underlying health issue that might be causing this.

## Question 2

While the "averages.png" and "maximums.png" graphs visualize typical values in our time-series data of heart rates and subsequently describe similar trends, the "stdevs.png" graph visualizes the standard deviations, which results in a graph with less apparent trends. In the context of heart rate, what does the standard deviation describe?

The standard deviation describes how spread out the values are for our data, highlighting points in where there are significant changes. It is a measure of the amount of variation or dispersion of a set of values. 

## Question 3

Run your `main.py` module and look at the graph labeled "averages.png." Roughly speaking, where do you see the time series experience a significant difference in values along the x-axis? Point out all x-values where you notice a drastic difference in future values.

You can notice a significant difference around the following values as they have major drops/ increases:
10 
30 
36
42

## Question 4

Do you also notice a corresponding difference in values in the "stdevs.png" graph? If so, do these differences align with the "averages.png" graph? 

I notice a correlation regarding the four highest points on stdevs.png are the four points that I mentioned above. It helps illustrate how these four points that I mentioned have signigicant changes in their values whether that's an increase or drop.

