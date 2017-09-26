
def partition(lst):
    for name in lst:
        if name[0] < 'N':
            print(name)


partition(['Eleanor', 'Evelyn', 'Sammy', 'Owen', 'Gavin'])  # do not use print(partition(...)) as it will print None as well
