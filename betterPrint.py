import plottingAndRegression

from tabulate import tabulate


# Main printing function
def bprint(*args,
           
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
        print(outputString, **kwargs)

    # Tabulate data
    if headers:
        outputString = tabulate(args[0], headers=headers, **kwargs)
        print(outputString)

    if plot:
        plottingAndRegression.plot(plot, *args, **kwargs)

if __name__ == "__main__":

    # zfillList test
    bprint([i for i in range(10)], zfillList=5)

    # Tabulate test
    bprint([['John', 38], ['Amy', 24]], headers=['Name', 'Age'], tablefmt='orgtbl')

    # Plot test
    bprint([i for i in range(10)], [i * 1.2 + 0.3 for i in range(10)], plot="scatter")