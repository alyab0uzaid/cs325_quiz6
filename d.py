from abc import ABC, abstractmethod

# Abstract logger interface
class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

# Implementation of a specific logging library (e.g., logging, loguru)
class LoggingLibraryLogger(Logger):
    def log(self, message):
        # Logging logic using the specific logging library
        print("Logging message using specific logging library:", message)

# A class demonstrating dependency inversion by utilizing the logger interface
class Application:
    def __init__(self, logger):
        self.logger = logger

    def perform_action(self):
        # Business logic
        self.logger.log("Performing action...")

def main():
    # Dummy value
    logger = LoggingLibraryLogger()

    # Injecting logger dependency
    app = Application(logger)
    app.perform_action()

if __name__ == "__main__":
    main()
