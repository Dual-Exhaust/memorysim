#TODO
# Add removing jobs from dynamic partitions
# this includes combining the partitions back together again
# add user input to create new partitions?
# next fit allocation needs to be created for everything
# definitely take back a tuple of lists (one for partitions and one for ondeck jobs),
# then take the on deck jobs and set them back into the list of jobs that we pass to the allocation algorithms
# this will require individual job lists for each type of allocation scheme for each type of memory BUT it will allow
# us to actually have a running tab of jobs waiting to be put into memory and eventually get them put in -
# put them in on removal of another job, AKA when the job finishes
# there is more specifics of this inside the sim class itself, all this shit needs to be reworked

# import our classes we need to simulate everything
from Mem import gen, sim, job

# initialize the counter we use to set job names
c = 0

# create fixed partitions for each type of allocation scheme
# each variable holds a list of partitions
# gen.createpartitions() creates five partitions of set size and locations
ffirstpartition = gen.createpartitions()
fbestpartition = gen.createpartitions()
fworstpartition = gen.createpartitions()
fnextpartition = gen.createpartitions()

# create the dynamic partitions for each type of allocation scheme
# the partitions themselves do not change, its how we manipulate it that makes it dynamic
# the dynamic partitions also start out the same way as the fixed partitions do
dfirstpartition = gen.createpartitions()
dbestpartition = gen.createpartitions()
dworstpartition = gen.createpartitions()
dnextpartition = gen.createpartitions()

# create the fixed simulation objects that hold the methods that actually perform the allocation algorithms
fixedfirst = sim.sim()
fixedbest = sim.sim()
fixedworst = sim.sim()
fixednext = sim.sim()

# create the dynamic simulation objects that hold the methods that actually perform the allocation algorithms
dynafirst = sim.sim()
dynabest = sim.sim()
dynaworst = sim.sim()
dynanext = sim.sim()

# create the lists that hold the on deck jobs
ffirstondeck = []
fbestondeck = []
fworstondeck = []
fnextondeck = []

dfirstondeck = []
dbestondeck = []
dworstondeck = []
dnextondeck = []

# create the index holders for nextfit algorithms
flast = 0
dlast = 0

# application loop
while True:
    print("########################################################################################################################")
    # get user input for the action they want to perform
    userin = input('Enter J for a new job or R to remove a job: ')
    # if the user wants to add a job
    if userin == "J":
        # the job name is "J" plus the count of total jobs we have already added
        # this is zero indexed so the first job we had has the name "J)"
        jobname = 'J' + str(c)
        # increment the total of jobs we have added
        c += 1
        # get the user input on the size of the job
        # this needs to be an integer to work
        jobsize = int(input("Enter the size of a job: "))

        # append the job that the user wants to the list of jobs for each allocation scheme
        ffirstondeck.append(job.job(jobname, jobsize))
        fbestondeck.append(job.job(jobname, jobsize))
        fworstondeck.append(job.job(jobname, jobsize))
        fnextondeck.append(job.job(jobname, jobsize))

        dfirstondeck.append(job.job(jobname, jobsize))
        dbestondeck.append(job.job(jobname, jobsize))
        dworstondeck.append(job.job(jobname, jobsize))
        dnextondeck.append(job.job(jobname, jobsize))

        # actually call the allocation schemes on the partitions we have, using the new job we just received
        # method returns a list of the updated list of partitions that we passed it, so we set the new variable here
        # inside the method we take care of printing out the partitions though
        # yeah yeah nested prints aren't good and all that but it *functions*
        # just comment out the lines if you don't want to see any particular allocation scheme

        # Fixed Partitions
        print('========================================================================================================================')
        # Fixed Partition using first fit allocation
        print('FIXED FIRST FIT >> JOBS: ', end='')
        print(*ffirstondeck)
        data = fixedfirst.fixedfirstfit(ffirstondeck, ffirstpartition)
        ffirstpartition = data[0]
        ffirstondeck = data[1]
        for part in ffirstpartition:
            print(part.getpartitiondata())
        print('ON DECK JOBS: ', end='')
        print(*ffirstondeck)
        print('========================================================================================================================')
        # Fixed Partition using next fit allocation
        print('FIXED NEXT FIT >> JOBS: ', end='')
        print(*fnextondeck)
        data = fixednext.fixednextfit(fnextondeck, fnextpartition, flast)
        fnextpartition = data[0]
        fnextondeck = data[1]
        flast = data[2]
        for part in fnextpartition:
            print(part.getpartitiondata())
        print('ON DECK JOBS: ', end='')
        print(*fnextondeck)
        print('========================================================================================================================')
        # Fixed Partition using best fit allocation
        print('FIXED BEST FIT >> JOBS: ', end='')
        print(*fbestondeck)
        data = fixedbest.fixedbestfit(fbestondeck, fbestpartition)
        fbestpartition = data[0]
        fbestondeck = data[1]
        for part in fbestpartition:
            print(part.getpartitiondata())
        print('ON DECK JOBS: ', end='')
        print(*fbestondeck)
        print('========================================================================================================================')
        # Fixed Partition using worst fit allocation
        print('FIXED WORST FIT >> JOBS: ', end='')
        print(*fworstondeck)
        data = fixedworst.fixedworstfit(fworstondeck, fworstpartition)
        fworstpartition = data[0]
        fworstondeck = data[1]
        for part in fworstpartition:
            print(part.getpartitiondata())
        print('ON DECK JOBS: ', end='')
        print(*fworstondeck)
        print('========================================================================================================================')

        # Dynamic Partitions
        print('========================================================================================================================')
        # Dynamic Partition using first fit allocation
        print('DYNAMIC FIRST FIT >> JOBS: ', end='')
        print(*dfirstondeck)
        data = dynafirst.dynafirstfit(dfirstondeck, dfirstpartition)
        dfirstpartition = data[0]
        dfirstondeck = data[1]
        for part in dfirstpartition:
            print(part.getpartitiondata())
        print('ON DECK JOBS: ', end='')
        print(*dfirstondeck)
        print('========================================================================================================================')
        # Dynamic Partition using best fit allocation
        print('DYNAMIC BEST FIT >> JOBS: ', end='')
        print(*dbestondeck)
        data = dynabest.dynabestfit(dbestondeck, dbestpartition)
        dbestpartition = data[0]
        dbestondeck = data[1]
        for part in dbestpartition:
            print(part.getpartitiondata())
        print('ON DECK JOBS: ', end='')
        print(*dbestondeck)
        print('========================================================================================================================')
        # Dynamic Partition using worst fit allocation
        print('DYNAMIC WORST FIT >> JOBS: ', end='')
        print(*dworstondeck)
        data = dynaworst.dynaworstfit(dworstondeck, dworstpartition)
        dworstpartition = data[0]
        dworstondeck = data[1]
        for part in dworstpartition:
            print(part.getpartitiondata())
        print('ON DECK JOBS: ', end='')
        print(*dworstondeck)
        print('========================================================================================================================')

    # if the user selects to remove a job
    elif userin == "R":
        # user inputs the job name
        target = input("Enter job by name to be removed: ")

        # we search through each partition to find the job that the user wanted to remove
        # for fixed partitions this is easy, all we do is set the status of that specific partition to free
        # so that when we want to add a new job and we check if its free, we can add a new job to it
        # I am only commenting out the first fit partition because the other allocation schemes are the same thing,
        # we just need to do the same thing for all of them
        print('========================================================================================================================')
        # search first fit partitions
        print('FIXED FIRST FIT')
        for part in ffirstpartition:
            # if partitions job name is the target set by the user
            if part.access == target:
                # set partition status to free
                part.setstatus('Free')
            # we print the blocks of partitions again to show the user the updated changes
            print(part.getpartitiondata())
        print('========================================================================================================================')
        # best fit partitions
        print('FIXED BEST FIT')
        for part in fbestpartition:
            if part.access == target:
                part.setstatus('Free')
            print(part.getpartitiondata())
        print('========================================================================================================================')
        # worst fit partitions
        print('FIXED WORST FIT')
        for part in fworstpartition:
            if part.access == target:
                part.setstatus('Free')
            print(part.getpartitiondata())
        print('========================================================================================================================')
        # next fit partitions
        print('FIXED NEXT FIT')
        for part in fnextpartition:
            if part.access == target:
                part.setstatus('Free')
            print(part.getpartitiondata())
        print('========================================================================================================================')
        # dynamic partitions
        print('========================================================================================================================')
        print('DYNAMIC FIRST FIT')
        # search first fit partitions
        for part in dfirstpartition:
            # if partitions job name is the target set by the user
            if part.access == target:
                # set partition status to free
                part.setstatus('Free')
            # we print the blocks of partitions again to show the user the updated changes
            print(part.getpartitiondata())
        print('========================================================================================================================')
        # best fit partitions
        print('DYNAMIC BEST FIT')
        for part in dbestpartition:
            if part.access == target:
                part.setstatus('Free')
            print(part.getpartitiondata())
        print('========================================================================================================================')
        # worst fit partitions
        print('DYNAMIC WORST FIT')
        for part in dworstpartition:
            if part.access == target:
                part.setstatus('Free')
            print(part.getpartitiondata())
        print('========================================================================================================================')
        # next fit partitions
        print('DYNAMIC NEXT FIT')
        for part in dnextpartition:
            if part.access == target:
                part.setstatus('Free')
            print(part.getpartitiondata())
        print('========================================================================================================================')
