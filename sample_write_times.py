import random


if __name__ == '__main__':
    time1 = random.randrange(10)
    time2 = random.randrange(10)

    with open('./sudoku_times.txt', 'r+') as file1:
        file1.seek(0)
        file1.writelines(str(time1) + '\n')
        file1.writelines(str(time2))
        file1.truncate()
    file1.close()