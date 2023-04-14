import timeit
track = []
track_2 = []
start = timeit.default_timer()
with open('input06.txt','r') as f:
    w = f.readline().split(' ')
    w = f.readline()
    st = w.rsplit('\n')
    st = st[0].split(' ')
    for i in range(len(st)):
        st[i] = int(st[i])
    track = st[:]
    while f.readline() != '100000\n':
        f.readline()
    st = f.readline().split('\n')
    st = st[0].split(' ')
    for i in range(len(st)):
        st[i] = int(st[i])
    track_2 = st[:]


def testing(rank, player):
    #start timer
    

    #binary search


    #result


    #end timer
    stop = timeit.default_timer()
    execution_time = stop - start
    print("Program Executed in "+str(execution_time)) # It returns time in seconds

    #return


print(testing(track,track_2))
