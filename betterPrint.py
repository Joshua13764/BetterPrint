from tabulate import tabulate
from datetime import datetime

import plottingAndRegression
from loggingPrint import LoggingObject

logObject = LoggingObject()

# Checks the kwarg exists and is true otherwise returns False
def _existsAndTrue(kwargs : dict, key : str):
    return key in kwargs and kwargs[key]

# Main printing function
def bprint(*args, savePath = None, noPrint = False, **kwargs):

    # ======================= List / Array settings

    # Zfill list will print out all of the numbers in a list with the specified z fill (needs type list)
    if type(args[0]) == list and _existsAndTrue(kwargs, "zfillList"):
        outputString = "[" + ", ".join([str(item).zfill(kwargs["zfillList"]) for item in args[0]]) + "]"

    # Tabulate headers will allow the data to be tabulated
    elif _existsAndTrue(kwargs, "headers"):
        outputString = tabulate(args[0], headers=kwargs["headers"], **kwargs)

    # ======================= 2 List / Array settings

    # Plots the data in either "line" or "scatter" modes
    elif _existsAndTrue(kwargs, "plot"):
        plottingAndRegression.plot(kwargs["plot"], *args, **kwargs)
        outputString = "Plotted the data"

    # Expect args to be a tuple of strings
    else:
        outputString = " ".join(args)

    # ======================= General settings

    # Add a timestamp to the printout
    if _existsAndTrue(kwargs, "timeStamp"):
        outputString = f"{datetime.now()}\t" + outputString

    # Save the output string as a file (if is a plot will save the plot with the given file name
    # this is handled by plottingAndRegression)
    if savePath and (not _existsAndTrue(kwargs, "plot")):
        logObject.saveToLogger(outputString, savePath)

    # print the output string at the end
    if not noPrint:
        print(outputString)

if __name__ == "__main__":

    # zfillList test
    bprint([i for i in range(10)], zfillList=5)

    # Tabulate test
    # bprint([['John', 38], ['Amy', 24]], headers=['Name', 'Age'], tablefmt='orgtbl')

    # Plot test
    # bprint([i for i in range(10)], [i * 1.2 + 0.3 for i in range(10)], plot="scatter")

    # Timestamp test
    bprint("Timestamp test", timeStamp=True, savePath="log1.log")
    bprint("Timestamp test2", timeStamp=False, savePath="log2.log", noPrint=True)
    bprint("Timestamp test3", timeStamp=True, savePath="log1.log")