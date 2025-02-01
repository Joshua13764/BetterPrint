from tabulate import tabulate
from datetime import datetime

import plottingAndRegression
from loggingPrint import LoggingObject

logObject = LoggingObject()

# Main printing function
def bprint(*args,
           
           # General settings

           # Save the printout to a text file
           savePath = False,

           # Add a timestamp to the printout
           timeStamp = False,
           
           # List / Array settings

           # Zfill list will print out all of the numbers in a list with the specified z fill (needs type list)
           zfillList = False,

           # Tabulate headers will allow the data to be tabulated
           headers = False,

           # 2 List / Array settings

           # Plots the data in either "line" or "scatter" modes
           plot = False,

           **kwargs):

    # For zfill the list
    if type(args[0]) == list and zfillList:
        outputString = "[" + ", ".join([str(item).zfill(zfillList) for item in args[0]]) + "]"

    # Tabulate data
    elif headers:
        outputString = tabulate(args[0], headers=headers, **kwargs)

    # Plot the data
    elif plot:
        plottingAndRegression.plot(plot, *args, **kwargs)
        outputString = "Plotted the data"

    # Expect args to be a tuple of strings
    else:
        outputString = " ".join(args)

    ## Post outputString creation settings

    # Add a timeStamp
    if timeStamp:
        outputString = f"{datetime.now()}\t" + outputString

    # Save the output string as a file (if is a plot will save the plot with the given file name
    # this is handled by plottingAndRegression)
    if savePath and (not plot):
        logObject.saveToLogger(outputString, savePath)

    # print the output string at the end
    print(outputString)

if __name__ == "__main__":

    # zfillList test
    bprint([i for i in range(10)], zfillList=5)

    # Tabulate test
    bprint([['John', 38], ['Amy', 24]], headers=['Name', 'Age'], tablefmt='orgtbl')

    # Plot test
    # bprint([i for i in range(10)], [i * 1.2 + 0.3 for i in range(10)], plot="scatter")

    # Timestamp test
    bprint("Timestamp test", timeStamp=True, savePath="log1")
    bprint("Timestamp test2", timeStamp=True, savePath="log2")
    bprint("Timestamp test3", timeStamp=True, savePath="log1")