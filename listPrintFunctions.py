from tools import existsAndTrue

# ======================= List / Array settings

# Zfill list will print out all of the numbers in a list with the specified z fill (needs type list)
def zfillList(args : tuple, kwargs : dict) -> str:
    return "[" + ", ".join([str(item).zfill(kwargs["zfillList"]) for item in args[0]]) + "]"

# Tabulate the array
def tabulateArray(args : tuple, kwargs : dict) -> str:
    # Extract the headers and remove entry from kwargs
    headers = kwargs.pop("headers")

    # Import the tabulate function
    from tabulate import tabulate

    # Return the output string
    return tabulate(args[0], headers=headers, **kwargs)

# Returns a dictionary of the functions specified in this file
def getFunctionDictionary() -> dict:

    # Dictionary with the keys beeing the required kwargs and the values being the functions to run
    # all of the functions only require args : tuple, kwargs : dict as inputs

    return {
        tuple(["zfillList"]) : zfillList,
        tuple(["headers"]) : tabulateArray
    }
