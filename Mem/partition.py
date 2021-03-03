# Covers partitions themselves and their properties
class partition:
    def __init__(self, name=-1, size=-1, address='NA', access='NA', accesssize='NA', status='Free'):
        # name of the partition
        self.name = name
        # size of the partition
        self.size = size
        # address is the first address in the partition
        self.address = address
        # The name of the job that is currently accessing and using the partition
        self.access = access
        # The size of the job that is currently accessing the partition
        self.accesssize = accesssize
        # Busy or Free, denotes if a job is currently using the partition
        self.status = status
        # The internal fragmenation of a partition
        self.fragmentation = 'NA'

    # add a new job to the partition
    def addjob(self, job):
        # if the partition is free (ready to be used) and the job fits inside the partition
        if self.status == 'Free' and job.getsize() <= self.size:
            # set the name of the job
            self.access = job.getname()
            # set the job size
            self.accesssize = job.getsize()
            # change the status to loaded
            self.status = 'Loaded'
            # edit fragmentation?
            # might need to be removed here if the fragmentation only occurs when a job exits the partition
            self.fragmentation = self.size - self.accesssize

    # when we set the size of a partition we want to update it to have the proper fragmentation as well
    # this could break if we have no job assigned to the partition yet we change the size of it
    # i am unsure if this method is being used
    def setsize(self, size):
        self.size = size
        self.fragmentation = self.size - self.accesssize

    def getsize(self):
        return self.size

    def getstatus(self):
        return self.status

    def setstatus(self, status):
        self.status = status

    def getaddress(self):
        return self.address

    def getaccess(self):
        return self.access

    def getfragmentation(self):
        return self.fragmentation

    # what we use to print each partition, seems to work fine formats okay
    def getpartitiondata(self):
        return ('|\t|Name:%s|\t|Size:%s|\t|Address:%s|\t|Access:%s|\t|Job Size:%s|\t|Status:%s|\t|Frag:%s|\t|' % (self.name, self.size, self.address, self.access, self.accesssize, self.status, self.fragmentation))

    # don't think this is used? but i don't want to break anything accidentally by removing it
    def __str__(self):
        return self.name, self.size, self.address, self.access, self.accesssize, self.status, self.fragmentation
