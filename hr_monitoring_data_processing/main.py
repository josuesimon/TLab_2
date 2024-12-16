from metrics import window_max, window_average, window_stddev
from cleaner import filter_nondigits, filter_outliers
import matplotlib.pyplot as plt

#We are creating a definition called run that takes in a file of strings and returns none
def run(filename: str) -> None:
    try: #This is a try block to catch any exceptions that may occur
        with open(filename, "r") as file: # This opens the file in read mode
            data = file.readlines() #This reads the file and returns a list of strings which we call data
    except FileNotFoundError: #This is an exception for when the file is not found 
        print(f"The following file was not found:'{filename}'.") #This prints an error message
        return [], [], []  # Return three empty lists if the file is not found
    

    #Below we are filtering out any non-digit characters from the data by calling cleaner.py 
    cleaned_data = filter_nondigits(data) #This filters out any non-digit characters from the data
    cleaned_data = filter_outliers(cleaned_data) #This filters out any outliers from the data

    max_values = window_max(cleaned_data, n=6) #This calculates the maximum value of a window of 6
    avg_values = window_average(cleaned_data, n=6) #This calculates the average value of a window of 6
    stddev_values = window_stddev(cleaned_data, n=6) #This calculates the standard deviation of a window of 6


    # Below we are plotting the data of max, average and standard deviation, ensuring that we cover the entire range of the data
    plt.plot(max_values, label="Max Values") # This plots the max values
    plt.title("Rolling Maximums") # This sets the title of the plot
    plt.xlabel("Window") # This sets the x-axis label
    plt.ylabel("Maximum") # This sets the y-axis label
    plt.legend() #This adds a legend to the plot
    plt.savefig("images/maximums.png") # This saves the plot as a png file
    plt.clf() # This clears the plot

    #We repeat the above process for average and standard deviation below
    plt.plot(avg_values, label="Average Values")
    plt.title("Rolling Averages")
    plt.xlabel("Window")
    plt.ylabel("Average")
    plt.legend()
    plt.savefig("images/averages.png")
    plt.clf()

    plt.plot(stddev_values, label="Standard Deviation")
    plt.title("Rolling Standard Deviations")
    plt.xlabel("Window")
    plt.ylabel("Standard Deviation")
    plt.legend()
    plt.savefig("images/stdevs.png")
    plt.clf()

    # Below we are printing the max, average and standard deviation values
    print("You can locate the plots in the images folder.") # This prints a message to let the user know that the plots have been saved in images folder
    return max_values, avg_values, stddev_values # This returns the max, average and standard deviation values


if __name__ == "__main__": # This ensures that the run function is only called when the script is run directly 
    run("data/data1.txt") # This calls the run function with the file data1.txt
