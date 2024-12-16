#We are first filtering the data by removing any items that are not integars
def filter_nondigits(data: list) -> list: #We begin by creating def filter_non_digits and using a list as the input
    int_heart_rates = []  #We create an empty list called int_heart_rates
    for heart_rate in data: #We perform a for loop that removes whitespace (including '\n')
        heart_rate = heart_rate.strip()
        if heart_rate.isdigit(): #We check if it is an int, and if it is not we convert it in the following line and append to the int_heart_rates list
            int_heart_rates.append(int(heart_rate))
    return int_heart_rates  # Return the list of integers in int_heart_rates


#We are now creating a second filter that removes any extreme values
def filter_outliers(data: list) -> list: #The def will be called filter_outliers and the input is a list
    filtered_heart_rates = []  #Our new list will be called filtered_heart_rates to store our new filtered list
    for value in data: #We will perform a for loop that goes through data and if it is between 30 or 250, it will add it to the created list
        if 30 < value < 250:
            filtered_heart_rates.append(value)
    return filtered_heart_rates  #Return the filtered filtered_heart_rates list