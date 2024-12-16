import statistics #We import the statistics library to use the math functions 
#Below we are creating three definition: window_max, window_average & window_stddev



def window_max(data: list, n: int) -> list: #We are calculating the maxmimum value of every "n" sized window in the data
    maximum_list = []  #We are creating a list called maximum_list to store the largest values
    if n <= 0:  #If n is less than or equal to 0, we return an empty list
        return maximum_list
    
    for i in range(0, len(data), n):  #We are looping through the data "n" number of times
        window = data[i:i + n]  #We are creating a window of "n" sized data
        if window:  #We are checking to see if the window is not empty
            maximum_value = max(window)  #We are finding the maximum value in the window
            maximum_list.append(round(maximum_value, 2))  #Round to 2 decimal places and append
    return maximum_list # Return the list of maximum values



#Below we repeat the steps that we did for window_max and repeat it to the definition of window_average and window_stddev
#The difference is that we are instead calculating the average and the standard deviation of every "n" sized window in the data
def window_average(data: list, n: int) -> list:
    average_list = [] 
    if n <= 0: 
        return average_list
    
    for i in range(0, len(data), n):  
        window = data[i:i + n]  
        if window: 
            average_value = statistics.mean(window)  
            average_list.append(round(average_value, 2))
    return average_list



def window_stddev(data: list, n: int) -> list:
    stddev_list = [] 
    if n < 0: 
       return stddev_list

    for i in range(0, len(data), n):  
        window = data[i:i + n] 
        if len(window) > 1: 
            stddev = statistics.stdev(window) 
            stddev_list.append(round(stddev, 2))  
    return stddev_list
