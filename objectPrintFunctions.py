from tabulate import tabulate

def probeObject(object, excludeStandardDir = True, probeable = True):

    # Exclude standard dir will remove the standard class items which are not usually important
    standardDir = {'__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
     '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__',
     '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__',
     '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
     '__sizeof__', '__str__', '__subclasshook__', '__weakref__'}
    
    nonProbeableTypes = {"<class 'type'>", "<class 'method-wrapper'>", "<class 'builtin_function_or_method'>",
                         "<class 'method'>"}

    # Collect data on object
    objectDir = dir(object)

    # Create an array of dir data
    dirArray = []
    for dirIndex, attr in enumerate(objectDir):

        attrType = type(getattr(object, attr))
        attrProbeable = str(type(getattr(object, attr))) not in nonProbeableTypes

        attrValue = str(getattr(object, attr))
        attrValueMaxLength = 30
        if len(attrValue) > attrValueMaxLength:
            attrValue = attrValue[:attrValueMaxLength] + "..."

        dirArray.append([dirIndex, attr, attrType, attrProbeable, attrValue])


    # Remove common data from printout
    dirArrayPrint = dirArray
    if excludeStandardDir:
        dirArrayPrint = filter(lambda i : i[1] not in standardDir, dirArray)

    dirArrayPrint = list(dirArrayPrint)

    # Output to user
    print(tabulate(dirArrayPrint, headers = ["Attribute index", "Attribute name", "Attribute type", "Can probe", "Value"]))

    # Allow probing
    if probeable:

        attr = input("Attribute to probe (Enter to close, - to return, name or index) ")

        if attr.isdigit() and 0 <= int(attr) < len(dirArray):
            attrIndex = int(attr)
            return getattr(object, dirArray[attrIndex][1])

        elif attr == "":
            return "probeExitCommand"
        
        elif attr == "-":
            return "probeHistoryReverseCommand"

        # Since only lookup once then set not required
        elif attr in dir(object):
            return getattr(object, attr)
        
        else:
            print(f"{attr} is not a valid input")
            return "probeExitCommand"

