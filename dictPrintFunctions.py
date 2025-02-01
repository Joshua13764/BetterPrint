from tools import existsAndTrue

# Print a dictionary as a table of keys and values
def printDictAsTable(args : tuple, kwargs : dict) -> str:

    # Import the tabulate function
    from tabulate import tabulate

    # Return the output string
    return tabulate(list(args[0].values()), headers=list(args[0].keys()), **kwargs)

# Returns a dictionary of the functions specified in this file
def getFunctionDictionary() -> dict:

    # Dictionary with the keys beeing the required kwargs and the values being the functions to run
    # all of the functions only require args : tuple, kwargs : dict as inputs

    return {
        tuple(["dictTable"]) : printDictAsTable,
    }
