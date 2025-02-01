
from datetime import datetime

from tools import existsAndTrue, checkFunctions
import plottingAndRegression
from listPrintFunctions import getFunctionDictionary as getListFuncs
from dictPrintFunctions import getFunctionDictionary as getDictFuncs
import savingModule

# Main printing function
def bprint(*args, savePath = None, plot = False, noPrint = False, **kwargs):

    # Set intitial value for outputString
    outputString = " ".join([str(arg) for arg in args])

    # Plots the data in either "line" or "scatter" modes
    if plot:
        plottingAndRegression.plot(plot, *args, **kwargs)
        outputString = "Plotted the data"

    # Find the functions to run
    functionsToRun = []

    # Find and append the functions which need to be run
    functionsToRun += checkFunctions(getListFuncs(), kwargs)
    functionsToRun += checkFunctions(getDictFuncs(), kwargs)
    
    # Run the functions
    for function in functionsToRun:
        outputString = function(args, kwargs)

    # Add a timestamp to the printout
    if existsAndTrue(kwargs, "timeStamp"):
        outputString = f"{datetime.now()}\t" + outputString

    # Save the output string as a file (if is a plot will save the plot with the given file name
    # this is handled by plottingAndRegression)
    if savePath and (not plot):
        savingModule.save(savePath, outputString, args, kwargs)

    # print the output string at the end
    if (not noPrint) and ("customObject" not in kwargs):
        print(outputString)

if __name__ == "__main__":

    # # Basic print test
    # bprint("hello", "world")

    # # zfillList test
    # bprint([i for i in range(10)], zfillList=5)

    # # Tabulate test
    # bprint([['John', 38], ['Amy', 24]], headers=['Name', 'Age'], tablefmt='orgtbl')

    # # Plot test
    # # bprint([i for i in range(10)], [i * 1.2 + 0.3 for i in range(10)], plot="scatter")

    # # Timestamp test
    # bprint("Timestamp test", timeStamp=True, savePath="log1.log")
    # bprint("Timestamp test2", timeStamp=False, savePath="log2.log", noPrint=True)
    # bprint("Timestamp test3", timeStamp=True, savePath="log1.log")

    # Dict table test
    bprint({i : chr(i) for i in range(80, 84)}, dictTable = True)

    # Write text as pickle file
    bprint("hello", savePath="outputA.pkl")

    # Write custom object as pickle file
    bprint(customObject = {1 : "a"}, savePath="outputB.pkl")