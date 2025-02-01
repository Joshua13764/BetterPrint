# Function checks the kwarg exists and is true otherwise returns False
def existsAndTrue(kwargs : dict, key : str):
    return key in kwargs and kwargs[key]

# Function which checks if kwarg(s) exist and returns the function(s) corrosponding to the satisfied conditions
def checkFunctions(functionsDict : dict, kwargs : dict) -> list:

    # Placeholder for the valid functions
    validFunctions = []

    for functionKey, function in functionsDict.items():

        # Checks if all elements in the functionKey are kwargs submitted by the user
        isValid = all([functionToken in kwargs for functionToken in functionKey])

        # If the function is valid then append it to the validFunctions list
        if isValid:
            validFunctions.append(function)

    # Return the list of the valid functions to the user
    return validFunctions
        
