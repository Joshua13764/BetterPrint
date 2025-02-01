# Private function checks the kwarg exists and is true otherwise returns False
def _existsAndTrue(kwargs : dict, key : str):
    return key in kwargs and kwargs[key]

def runListPrintFunctions(*args, **kwargs):

    # ======================= List / Array settings

    # Zfill list will print out all of the numbers in a list with the specified z fill (needs type list)
    if type(args[0]) == list and _existsAndTrue(kwargs, "zfillList"):

        # Return the output string
        return "[" + ", ".join([str(item).zfill(kwargs["zfillList"]) for item in args[0]]) + "]"

    # Tabulate headers will allow the data to be tabulated
    elif _existsAndTrue(kwargs, "headers"):

        # Extract the headers and remove entry from kwargs
        headers = kwargs.pop("headers")

        # Import the tabulate function
        from tabulate import tabulate

        # Return the output string
        return tabulate(args[0], headers=headers, **kwargs)

    # Expect args to be a tuple of strings
    else:
        return None

