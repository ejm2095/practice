__author__ = 'undergroundskier'

def smallestM(lg):
    cnt = 1
    while True:
        x = cnt * lg
        for x in range(lg, 1):
            if x%lg:
                break

