
from datetime import datetime

import plottingAndRegression
from loggingPrint import LoggingObject
from listPrintFunctions import runListPrintFunctions

logObject = LoggingObject()

# Private function checks the kwarg exists and is true otherwise returns False
def _existsAndTrue(kwargs : dict, key : str):
    return key in kwargs and kwargs[key]

# Main printing function
def bprint(*args, savePath = None, plot = False, noPrint = False, **kwargs):

    # Set intitial value for outputString

    outputString = " ".join([str(arg) for arg in args])

    # ======================= 2 List / Array settings

    # Plots the data in either "line" or "scatter" modes
    if plot:
        plottingAndRegression.plot(plot, *args, **kwargs)
        outputString = "Plotted the data"

    # ======================= List / Array settings

    # Try list print functions
    res = runListPrintFunctions(*args, **kwargs)
    if res != None:
        outputString = res

    # ======================= General settings

    # Add a timestamp to the printout
    if _existsAndTrue(kwargs, "timeStamp"):
        outputString = f"{datetime.now()}\t" + outputString

    # Save the output string as a file (if is a plot will save the plot with the given file name
    # this is handled by plottingAndRegression)
    if savePath and (not plot):
        logObject.saveToLogger(outputString, savePath)

    # print the output string at the end
    if not noPrint:
        print(outputString)

if __name__ == "__main__":

    # Basic print test
    bprint("hello", "world")

    # zfillList test
    bprint([i for i in range(10)], zfillList=5)

    # Tabulate test
    bprint([['John', 38], ['Amy', 24]], headers=['Name', 'Age'], tablefmt='orgtbl')

    # Plot test
    # bprint([i for i in range(10)], [i * 1.2 + 0.3 for i in range(10)], plot="scatter")

    # Timestamp test
    bprint("Timestamp test", timeStamp=True, savePath="log1.log")
    bprint("Timestamp test2", timeStamp=False, savePath="log2.log", noPrint=True)
    bprint("Timestamp test3", timeStamp=True, savePath="log1.log")