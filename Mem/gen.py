#TODO
# this class is severely unused for the most part
# clean it up chop chop

from Mem import partition

# create partitions to start with
def createpartitions():
    tmp = []
    # create and append standard partitions to return
    tmp.append(partition.partition(name='P0', size=1500, address='0000'))
    tmp.append(partition.partition(name='P1', size=10, address='1500'))
    tmp.append(partition.partition(name='P2', size=500, address='1510'))
    tmp.append(partition.partition(name='P3', size=100, address='2010'))
    tmp.append(partition.partition(name='P4', size=25, address='2110'))
    return tmp