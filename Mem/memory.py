from Mem import partition


# TODO
# gotta fix the next fit algorithms in here for both classes

# these two classes actually do the work and set the jobs in each partition that they need to be in

# for fixed memory partitions
class fixedmem():
    # initialization
    def __init__(self):
        # A list of the partitions available in the memory simulation
        self.partitions = []

    # Returns a list of the partitions that the memory has
    def getpartitions(self):
        return self.partitions

    # adds a new partition to the memory
    def addpartition(self, part):
        self.partitions.append(part)

    # returns a list of jobs that were not used and are not using any memory, they are next in line to to get memory

    # fixed first fit
    def firstfit(self, joblist):
        ondeck = []
        # we look at each job we have
        for job in joblist:
            # flag keeps track of if a job has been added or not
            flag = True
            # we then check each partition in order
            for x in range(len(self.partitions)):
                # If the job fits inside, then we add it and flag this job to end the inner loop
                # moving on to the next job in the list
                if job.getsize() <= self.partitions[x].getsize() and flag and self.partitions[
                    x].getstatus() != 'Loaded':
                    self.partitions[x].addjob(job)
                    flag = False
            # Job was not added to any partition, it was too big or all partitions were full
            if flag:
                # add the job to the list of jobs that are waiting to be executed
                ondeck.append(job)
        return ondeck

    # fixed best fit
    def bestfit(self, joblist):
        # init on deck jobs
        ondeck = []
        # go through each job in the job list we receive
        for job in joblist:
            # our target partition is nothing to start
            target = ''
            # starting fit for the job to partition is a really high number, the smaller the fit the better the job is for the partition
            fit = 100000
            # cycle partitions that we have
            for part in self.partitions:
                # if fit is less than what we have recorded, partition is not being used, and job fits in partition
                if (part.getsize() - job.getsize() < fit) and (part.getstatus() != 'Loaded') and (
                        job.getsize() <= part.getsize()):
                    # set the new fit
                    # fit is the size of the partition minus the job size
                    fit = part.getsize() - job.getsize()
                    # mark the current partition as our target
                    target = part
            # if the target was never set (job does not fit or all partitions are full)
            if target == '':
                # add job to on deck jobs
                ondeck.append(job)
            # if the target was set (we have a partition we want to add the job to)
            else:
                # add the job to the partition
                target.addjob(job)
        # return the list of jobs that are still waiting to be executed
        return ondeck

    # fixed worst fit
    # this is literally the same as best fit except for the fact that we track our fit value in the opposite way
    # the higher the number the better the fit is, so we check for > fit and also start our fit as a negative number
    # it is otherwise the same and functions in the same way
    def worstfit(self, joblist):
        ondeck = []
        for job in joblist:
            target = ''
            fit = -1
            for part in self.partitions:
                if (part.getsize() - job.getsize() > fit) and (part.getstatus() != 'Loaded') and (
                        job.getsize() <= part.getsize()):
                    fit = part.getsize() - job.getsize()
                    target = part
            if target == '':
                ondeck.append(job)
            else:
                target.addjob(job)
        return ondeck

    # fixed next fit
    # TOTALLY BROKEN OH GOD LORD HELP ME
    # Possibly just delete the whole thing and start over
    # maybe pass back another value in addition to the on deck jobs that we can set so that we know what
    # partition to start off with? We do use an indexed for loop rather than a for each
    def nextfit(self, joblist, index):
        ondeck = []
        # we start looking at the last index that we assigned a job
        c = index
        # we look at each job we have
        for job in joblist:
            # flag keeps track of if a job has been added or not
            flag = True
            # we then check each partition starting where we last added a job
            # only covers from index to the end of the partition list
            while c < len(self.partitions):
                # If the job fits inside, then we add it and flag this job to end the inner loop
                # moving on to the next job in the list
                if job.getsize() <= self.partitions[c].getsize() and flag and self.partitions[
                        c].getstatus() != 'Loaded':
                    self.partitions[c].addjob(job)
                    # we set a job so now we want to mark the index as this one
                    index = c
                    flag = False
                c += 1
            # reset c to start from the front of the list
            c = 0
            # while loop covers from 0 to index we last set a job at
            while c < index:
                # If the job fits inside, then we add it and flag this job to end the inner loop
                # moving on to the next job in the list
                if job.getsize() <= self.partitions[c].getsize() and flag and self.partitions[
                        c].getstatus() != 'Loaded':
                    self.partitions[c].addjob(job)
                    index = c
                    flag = False
                c += 1
            # Job was not added to any partition, it was too big or all partitions were full
            if flag:
                # add the job to the list of jobs that are waiting to be executed
                ondeck.append(job)

        return [ondeck, index]

# for dynamic partitions
class dynamem():
    def __init__(self):
        # A list of the partitions available in the memory simulation
        self.partitions = []

    # Returns a list of the partitions that the memory has
    def getpartitions(self):
        return self.partitions

    # adds a new partition to the memory
    def addpartition(self, part):
        self.partitions.append(part)

    def combinepartitions(self):
        total = 0
        tmpparts = []
        for part in self.partitions:
            if part.getstatus() != 'Loaded':
                # print(self.partitions[x].getsize())
                total += part.getsize()
                # self.partitions.remove(part)
            else:
                tmpparts.append(part)
        tmpparts.append(partition.partition(name=("P" + str(len(self.partitions))), size=total))

        self.partitions = tmpparts

    # returns a list of jobs that were not used and are not using any memory, they are next in line to to get memory
    def firstfit(self, joblist):
        ondeck = []
        # we look at each job we have
        for job in joblist:
            # flag keeps track of if a job has been added or not
            flag = True
            # we then check each partition in order
            for x in range(len(self.partitions)):
                # If the job fits inside, then we add it and flag this job to end the inner loop
                # moving on to the next job in the list
                if job.getsize() <= self.partitions[x].getsize() and flag and self.partitions[
                        x].getstatus() != 'Loaded':
                    # add the job to the partition
                    self.partitions[x].addjob(job)
                    # if our fragmentation is 0, check prevents creating a new partition with 0 size
                    if self.partitions[x].getfragmentation != 0:
                        # create a new partition for the empty memory that is caused by the job added add a name
                        # using the length of the current partition list (length is always one number above the last
                        # name because it is zero indexed) add a size (the difference between the partition we added
                        # the job to and the job size itself) the address is just the old address of the partition we
                        # added the job to plus the job size
                        self.addpartition(partition.partition(name=("P" + str(len(self.partitions))),
                                                              size=(self.partitions[x].getsize() - job.getsize()),
                                                              address=str(int(
                                                                  self.partitions[x].getaddress()) + job.getsize())))
                        # because we created a new partition for the unused memory, we need to reset the size of the
                        # current partition that we added the job to it just becomes the size of the job itself
                        self.partitions[x].setsize(job.getsize())
                    # the job was added so we change our flag
                    flag = False
            # Job was not added to any partition, it was too big or all partitions were full
            if flag:
                # add job to the ondeck list
                ondeck.append(job)
        # return waiting jobs
        return ondeck

    def bestfit(self, joblist):
        ondeck = []
        for job in joblist:
            target = ''
            fit = 100000
            for part in self.partitions:
                if (part.getsize() - job.getsize() < fit) and (part.getstatus() != 'Loaded') and (
                        job.getsize() <= part.getsize()):
                    fit = part.getsize() - job.getsize()
                    target = part
            if target == '':
                ondeck.append(job)
            else:
                target.addjob(job)
                if target.getfragmentation() != 0:
                    self.addpartition(partition.partition(name=("P" + str(len(self.partitions))),
                                                          size=(target.getsize() - job.getsize()),
                                                          address=str(int(target.getaddress()) + job.getsize())))
                    target.setsize(job.getsize())

        return ondeck

    def worstfit(self, joblist):
        ondeck = []
        for job in joblist:
            target = ''
            fit = -1
            for part in self.partitions:
                # print(part.getsize() - job.getsize())
                if (part.getsize() - job.getsize() > fit) and (part.getstatus() != 'Loaded') and (
                        job.getsize() <= part.getsize()):
                    fit = part.getsize() - job.getsize()
                    target = part
            if target == '':
                ondeck.append(job)
            else:
                target.addjob(job)
                if target.getfragmentation() != 0:
                    self.addpartition(partition.partition(name=("P" + str(len(self.partitions))),
                                                          size=(target.getsize() - job.getsize()),
                                                          address=str(int(target.getaddress()) + job.getsize())))
                    target.setsize(job.getsize())
        return ondeck

    # I don't even want to look at this yet
    # I am not looking forward to it nor am I going to have a fun time figuring it out
    def nextfit(self, joblist, index):
        ondeck = []
        # we start looking at the last index that we assigned a job
        c = index
        # we look at each job we have
        for job in joblist:
            # flag keeps track of if a job has been added or not
            flag = True
            # we then check each partition starting where we last added a job
            # only covers from index to the end of the partition list
            while c < len(self.partitions):
                # If the job fits inside, then we add it and flag this job to end the inner loop
                # moving on to the next job in the list
                if job.getsize() <= self.partitions[c].getsize() and flag and self.partitions[
                    c].getstatus() != 'Loaded':
                    self.partitions[c].addjob(job)
                    if self.partitions[c].getfragmentation() != 0:
                        self.addpartition(partition.partition(name=("P" + str(len(self.partitions))),
                                                              size=(self.partitions[c].getsize() - job.getsize()),
                                                              address=str(int(self.partitions[c].getaddress()) + job.getsize())))
                        self.partitions[c].setsize(job.getsize())
                    # we set a job so now we want to mark the index as this one
                    index = c
                    flag = False
                c += 1
            # reset c to start from the front of the list
            c = 0
            # while loop covers from 0 to index we last set a job at
            while c < index:
                # If the job fits inside, then we add it and flag this job to end the inner loop
                # moving on to the next job in the list
                if job.getsize() <= self.partitions[c].getsize() and flag and self.partitions[
                    c].getstatus() != 'Loaded':
                    self.partitions[c].addjob(job)
                    if self.partitions[c].getfragmentation() != 0:
                        self.addpartition(partition.partition(name=("P" + str(len(self.partitions))),
                                                              size=(self.partitions[c].getsize() - job.getsize()),
                                                              address=str(int(self.partitions[c].getaddress()) + job.getsize())))
                        self.partitions[c].setsize(job.getsize())
                    index = c
                    flag = False
                c += 1
            # Job was not added to any partition, it was too big or all partitions were full
            if flag:
                # add the job to the list of jobs that are waiting to be executed
                ondeck.append(job)

        return [ondeck, index]
