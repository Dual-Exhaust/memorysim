# A class to cover job obects themselves that we insert into memory.
class job:
    def __init__(self, name, size):
        # Name of the job
        self.name = name
        # Size of the job
        self.size = size
        # The location of the job, what partition it is using
        self.location = None
        # May not be used
        self.status = None

    # Sets the location of the job, then returns the location (could be useful for printing)
    def setlocation(self, location):
        self.location = location
        return self.location

    def getname(self):
        return self.name

    def getsize(self):
        return self.size

    # defines how we print jobs (really only used when displaying what jobs we have and which ones are on deck)
    def __str__(self):
        return self.name + ':' + str(self.size)
