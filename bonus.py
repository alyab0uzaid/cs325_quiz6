from abc import ABC, abstractmethod

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, data):
        pass

# Subject interface
class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

# Concrete Subject class representing user activity monitor
class ActivityMonitor(Subject):
    def __init__(self):
        self.observers = []
        self.activity_data = {}

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.activity_data)

    def set_activity_data(self, data):
        self.activity_data = data
        self.notify()

# Concrete Observer class representing data storage
class DataStorage(Observer):
    def update(self, data):
        # Store activity data
        print("Storing activity data:", data)

# Concrete Observer class representing activity display
class ActivityDisplay(Observer):
    def update(self, data):
        # Display activity data
        print("Displaying activity data:", data)

# User class representing a fitness tracker user
class User:
    def __init__(self, name):
        self.name = name

# Activity class representing different types of activities
class Activity:
    def __init__(self, name):
        self.name = name

# Concrete activity subclass
class Running(Activity):
    pass

# Concrete activity subclass
class Swimming(Activity):
    pass

# Concrete activity subclass
class Cycling(Activity):
    pass

def main():
    # Create instances
    monitor = ActivityMonitor()
    storage = DataStorage()
    display = ActivityDisplay()

    # Attach observers
    monitor.attach(storage)
    monitor.attach(display)

    # Simulate activity data
    user = User("John")
    activity = Running("Running")
    data = {"user": user, "activity": activity, "steps": 5000, "distance": 5.0, "calories": 300}

    # Set activity data
    monitor.set_activity_data(data)

if __name__ == "__main__":
    main()
