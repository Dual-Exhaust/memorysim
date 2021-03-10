from Mem import memory

#TODO
# Any nextfit allocation should also send back an integer representation of the partition we are going to
# start with the next time we receive a job
# the integer should just be the index of the partition
# what will happen is we will intake an integer to the next fit algorithm method from the memory class
# and take a tuple back of the ondeck jobs and of the index
# then we will return index, ondeck jobs, and updated partitions to the application class itself
# got it? cool okay do this then before anything else

# prints the output for each allocation scheme, needs partitions and jobs to function
class sim:
    def __init__(self):
        self.partitions = []
        self.jobs = []
        self.ondeckjobs = []
        self.mem = None

    # The following fixed methods manipulate the variables set in __init__ and then print output
    def fixedfirstfit(self, jobs, partitions):
        self.jobs = jobs
        self.partitions = partitions
        # Create memory object
        self.mem = memory.fixedmem()
        # add partitions to the memory
        for part in self.partitions:
            self.mem.addpartition(part)
        # get the list of jobs that could not make it into memory
        self.ondeckjobs = self.mem.firstfit(self.jobs)
        # grab the partitions after their data has been set by firstfit
        self.partitions = self.mem.getpartitions()

        return [self.partitions, self.ondeckjobs]

    def fixednextfit(self, jobs, partitions, index):
        self.jobs = jobs
        self.partitions = partitions
        # Create memory object
        self.mem = memory.fixedmem()
        # add partitions to the memory
        for part in self.partitions:
            self.mem.addpartition(part)
        # get the list of jobs that could not make it into memory
        # also get the index to start at
        tmp = self.mem.nextfit(self.jobs, index)
        self.ondeckjobs = tmp[0]
        startindex = tmp[1]
        # grab the partitions after their data has been set by firstfit
        self.partitions = self.mem.getpartitions()

        return [self.partitions, self.ondeckjobs, startindex]

    def fixedworstfit(self, jobs, partitions):
        self.jobs = jobs
        self.partitions = partitions
        # Create memory object
        self.mem = memory.fixedmem()
        # add partitions to the memory
        for part in self.partitions:
            self.mem.addpartition(part)
        # get the list of jobs that could not make it into memory
        self.ondeckjobs = self.mem.worstfit(self.jobs)
        # grab the partitions after their data has been set by firstfit
        self.partitions = self.mem.getpartitions()

        return [self.partitions, self.ondeckjobs]

    def fixedbestfit(self, jobs, partitions):
        self.jobs = jobs
        self.partitions = partitions
        # Create memory object
        self.mem = memory.fixedmem()
        # add partitions to the memory
        for part in self.partitions:
            self.mem.addpartition(part)
        # get the list of jobs that could not make it into memory
        self.ondeckjobs = self.mem.bestfit(self.jobs)
        # grab the partitions after their data has been set by firstfit
        self.partitions = self.mem.getpartitions()

        return [self.partitions, self.ondeckjobs]

    def dynafirstfit(self, jobs, partitions):
        self.jobs = jobs
        self.partitions = partitions
        # Create memory object
        self.mem = memory.dynamem()
        # add partitions to the memory
        for part in self.partitions:
            self.mem.addpartition(part)
        # get the list of jobs that could not make it into memory
        self.ondeckjobs = self.mem.firstfit(self.jobs)
        self.mem.combinepartitions()
        # grab the partitions after their data has been set by firstfit
        self.partitions = self.mem.getpartitions()

        return [self.partitions, self.ondeckjobs]

    def dynanextfit(self, jobs, partitions, index):
        self.jobs = jobs
        self.partitions = partitions
        # Create memory object
        self.mem = memory.dynamem()
        # add partitions to the memory
        for part in self.partitions:
            self.mem.addpartition(part)
        # get the list of jobs that could not make it into memory
        # also get the index to start at
        tmp = self.mem.nextfit(self.jobs, index)
        self.ondeckjobs = tmp[0]
        startindex = tmp[1]
        self.mem.combinepartitions()
        # grab the partitions after their data has been set by nextfix
        self.partitions = self.mem.getpartitions()

        return [self.partitions, self.ondeckjobs, startindex]

    def dynaworstfit(self, jobs, partitions):
        self.jobs = jobs
        self.partitions = partitions
        # for part in self.partitions:
        #     print(part.getpartitiondata())
        # Create memory object
        self.mem = memory.dynamem()
        # add partitions to the memory
        for part in self.partitions:
            self.mem.addpartition(part)
        # get the list of jobs that could not make it into memory
        self.ondeckjobs = self.mem.worstfit(self.jobs)
        self.mem.combinepartitions()
        # grab the partitions after their data has been set by firstfit
        self.partitions = self.mem.getpartitions()

        return [self.partitions, self.ondeckjobs]

    def dynabestfit(self, jobs, partitions):
        self.jobs = jobs
        self.partitions = partitions
        # Create memory object
        self.mem = memory.dynamem()
        # add partitions to the memory
        for part in self.partitions:
            self.mem.addpartition(part)
        # get the list of jobs that could not make it into memory
        self.ondeckjobs = self.mem.bestfit(self.jobs)
        self.mem.combinepartitions()
        # grab the partitions after their data has been set by firstfit
        self.partitions = self.mem.getpartitions()

        return [self.partitions, self.ondeckjobs]
