
from datetime import datetime

from tools import existsAndTrue, checkFunctions
import plottingAndRegression
from listPrintFunctions import getFunctionDictionary as getListFuncs
from dictPrintFunctions import getFunctionDictionary as getDictFuncs
from objectPrintFunctions import probeObject
import savingModule

# Main printing function
def bprint(*args, savePath = None, plot = False, noPrint = False, probe = False, **kwargs):

    # Set intitial value for outputString
    outputString = " ".join([str(arg) for arg in args])

    # Plots the data in either "line" or "scatter" modes
    if plot:
        plottingAndRegression.plot(plot, *args, **kwargs)
        outputString = "Plotted the data"

    # If probe then probe
    if probe:

        # Step the probe
        probeHistory = [args[0]]
        lastCommand = None

        # Iterate through object ultil None returned then exit
        while True:

            # Exit out of function
            if lastCommand == "probeExitCommand":
                return None

            # Return back one step
            if lastCommand == "probeHistoryReverseCommand":
                probeHistory.pop()

                # Output to the user if cannot return back one
                if len(probeHistory) == 0:
                    print("Cannot step back one")
                    probeHistory = [args[0]]
                
                lastCommand = probeObject(probeHistory[-1])

            # Then allow probe further
            else:
                lastCommand = probeObject(probeHistory[-1])

            # Add record of probing
            if lastCommand not in ["probeExitCommand", "probeHistoryReverseCommand"]:
                probeHistory.append(lastCommand)

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

    # Dict table test
    bprint({i : chr(i) for i in range(80, 84)}, dictTable = True)

    # Write text as pickle file
    bprint("hello", savePath="outputA.pkl")

    # Write custom object as pickle file
    bprint(customObject = {1 : "a"}, savePath="outputB.pkl")

    # Object probe example
    class test():

        def __init__(self):
            self.a = "a"
            self.b = 28

        def ok(self):
            self.c = test()

        def mov(self, q):
            return self.a + q
        
    testObj = test()
    testObj.ok()

    bprint(testObj, probe=True) 