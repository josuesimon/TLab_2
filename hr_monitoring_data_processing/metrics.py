import statistics

def window_max(data: list, n: int) -> list: #We are calculating the maxmimum value of every "n" sized window in the data
    maximum_list = []  #We are creating a list called maximum_list to store the largest values
    for i in range(0, len(data), n):  # Iterate through data in steps of 'n'
        window = data[i:i + n]  # Extract the current window
        if window:  # Ensure the window is not empty
            maximum_list.append(max(window))  # Find and append the maximum value
    return maximum_list

    """
    Calculate maximum value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of maximums from each window (size should be len(data)//6)
    """
    maximums = []
    ...


def window_average(data: list, n: int) -> list:
  maximum_list = []  #We are creating a list called maximum_list to store the largest values
    for i in range(0, len(data), n):  # Iterate through data in steps of 'n'
        window = data[i:i + n]  # Extract the current window
        if window:  # Ensure the window is not empty
            maximum_list.append(max(window))  # Find and append the maximum value
    return maximum_list




 #   pass


#def window_stddev(data: list, n: int) -> list:
 #   pass
