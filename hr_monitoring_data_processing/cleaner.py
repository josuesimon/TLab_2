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
    outlier_int_heart_rates = []  #Our new list will be called outlier_int_heart_rates to store our new filtered list
    for value in data: #We will perform a for loop that goes through data and if it is between 30 or 250, it will add it to the outlier_int_heart_rates list
        if 30 <= value <= 250:
            outlier_int_heart_rates.append(value)
    return outlier_int_heart_rates  #Return the filtered outlier_int_heart_rates list


#filtered_data = filter_nondigits(data1.txt)  # Removes items that are not integars
#valid_data = filter_outliers(filtered_data)  # Removes outliers less than 30 or greater than 250
#print("The filtered data is as follows:", valid_data)  #Print out the filtered data
