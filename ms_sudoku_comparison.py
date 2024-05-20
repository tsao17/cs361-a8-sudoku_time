import time
import math


def readTimes(read_path):
    with open(read_path, 'r+') as file1:

        try:
            time_1 = float(file1.readline())
            time_2 = float(file1.readline())

            # determine which one is faster
            if time_1 > time_2:
                fastest = 'Algorithm 1'
                percentage = ((time_1 - time_2) / time_2) * 100
            else:
                fastest = 'Algorithm 2'
                percentage = ((time_2 - time_1) / time_1) * 100

            percentage = str(round(percentage, 2)) + '%'
            file1.truncate(0)

            writeData('./fastest_alg.txt', fastest, percentage)
        except:
            print('Waiting for data')
            file1.truncate(0)

    file1.close()


def writeData(write_path, fastest, percentage=''):
    with open(write_path, 'r+') as file2:
        file2.seek(0)
        file2.writelines(fastest + '\n')
        file2.writelines(percentage)
        file2.truncate()
    file2.close()


while True:
    time.sleep(1)
    readTimes('./sudoku_times.txt')
