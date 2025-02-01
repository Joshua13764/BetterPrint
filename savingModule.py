from os.path import splitext

from loggingPrint import LoggingObject

# Init the logging object
logObject = LoggingObject()

def saveToPickle(savePath : str, outputString : str, kwargs : dict):

    # Import the pickle module
    from pickle import dump

    # Write as a pickle file
    if "customObject" in kwargs:
        objectToWrite = kwargs["customObject"]
    else:
        objectToWrite = outputString

    with open(savePath, "wb") as pk:
        dump(objectToWrite, pk)

# Coodinates the saving of objects
def save(savePath : str, outputString : str, args : tuple, kwargs : dict) -> None:

    # Get extension of the path
    root, ext = splitext(savePath)

    if ext == ".log":
        logObject.saveToLogger(outputString, savePath)

    elif ext == ".pkl":
        saveToPickle(savePath, outputString, kwargs)