import logging
from os.path import basename

class LoggingObject():

    def __init__(self):
        
        # Dictionary of logger path : logger used to find the created loggers
        self.loggerDict = {}

    # Create a log
    def _createLogger(self, name : str, logPath : str, level = logging.INFO) -> logging.Logger:

        # Setup a custom logger file handler
        handler = logging.FileHandler(logPath)

        # Setup a custom logger formatter handler
        formatter = logging.Formatter('%(message)s') 
        handler.setFormatter(formatter)

        # Get the logger using the name
        logger = logging.getLogger(name)

        # Set the logging level from the method input
        logger.setLevel(level)

        # Add the logging handlers
        logger.addHandler(handler)

        # Return the logger
        return logger

    # Save a string to the log
    def saveToLogger(self, outputString : str, loggerPath : str) -> None:

        # If a logger doesn't exist create it
        if loggerPath not in self.loggerDict:
            self.loggerDict[loggerPath] = self._createLogger(
                name = f"logger {basename(loggerPath)}",
                logPath = loggerPath,
            )

        # Add output string to the log
        self.loggerDict[loggerPath].info(outputString)
