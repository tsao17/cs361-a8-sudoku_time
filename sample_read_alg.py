if __name__ == '__main__':

    with open('./fastest_alg.txt', 'r+') as file1:
        line1 = file1.readline()
        line2 = file1.readline()

        print("The fastest alg was:" + line1)
        print("It was faster by: " + line2)
    file1.close()