from src.data import *

def compute_time(n):
    initial_time = 4
    return int(initial_time * (1.75 ** n))


if __name__ == '__main__':
    mydata = Data()
    mydata.read()