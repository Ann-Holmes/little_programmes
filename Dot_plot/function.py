import matplotlib.pyplot as plt


def input_sequence():
    """get sequences and window size"""
    judgment = input("Please choose input way, read from a file or enter by keyboard.\n"
                     "(Sorry, this function can't be used now!) \n"
                     "Please enter 'file' or 'keyboard':")
    if judgment == 'file':
        filename_a = input("Please enter filename of sequence a and absolutely path(e.g.:/home/andy/filename): ")
        seq_a = ''
        with open(filename_a) as file_object:
            lines = file_object.readlines()
            for line in lines:
                if '>' not in line:
                    seq_a.join(line)
        filename_b = input("Please enter filename of sequence b and absolutely path(e.g.:/home/andy/filename): ")
        seq_b = ''
        with open(filename_b) as file_object:
            lines = file_object.readlines()
            for line in lines:
                if '>' not in line:
                    seq_b.join(line)
    elif judgment == 'keyboard':
        seq_a = input("Please input sequence a: ")
        seq_b = input("Please input sequence b: ")
    win_size = input("window size: ")

    # judgment for wrong input
    if win_size == '':
        win_size = 1
    if int(win_size) > min(len(seq_a), len(seq_b)) or len(seq_a) == 0 or len(seq_b) == 0:
        print("Please enter right information! ")
    else:
        win_size = int(win_size)
    return seq_a, seq_b, win_size

    # ? no the function for change threshold. thd = input("Threshold: ")


def initialization_list(seq_a,seq_b,win_size):
    """
    This function is to initialization dot matrix, make two sequences lie in a matrix
    :param seq_a: one sequence, string
    :param seq_b: another sequence, string
    :param win_size: sliding window size, int
    :return: an initialized dot matrix, list
    """
    lst_a = [nt for nt in seq_a]  # split sequence str in list
    lst_b = [nt for nt in seq_b]  # split sequence str in list
    lst_a.insert(0, ' ')  # because of column, insert a blank in the beginning of lst_a
    lst_alg = [[]]
    lst_alg[0] = lst_a
    for n in range(len(lst_b)):  # fill the first row and column
        lst_alg.append([lst_b[n]])
    if win_size > 1:  # if win_size is 1, won't complete the window blank
        for i in range(1, win_size):  # complete the window blank in the beginning of lst_alg's row
            lst_alg[i].extend(len(lst_a)*' ')
        for j in range(win_size, len(lst_b)+1):  # complete the window blank in the beginning of lst_alg's column
            lst_alg[j].extend((win_size-1)*' ')
    return lst_alg


def alignment(lst_alg, win_size):
    """
    Alignment two sequences and fill the dot matrix
    :param lst_alg: an initialized dot matrix, list
    :param win_size: sliding window size, int
    :return: a filled dot matrix, list
    """
    for i in range(1, (len(lst_alg[0]) - win_size)):  # scan by row
        for j in range(1, (len(lst_alg) - win_size + 1)):  # scan by column
            # alignment of diagonal in the window
            counter = 1  # setting a counter to control the window size
            for k in range(win_size + 1):
                if counter > win_size:
                    lst_alg[j + win_size - 1].append('*')
                    break
                elif lst_alg[0][i + k] != lst_alg[j + k][0]:
                    lst_alg[j + win_size - 1].append(' ')
                    break
                counter += 1
    return lst_alg


def show_simply(lst_alg_filled):
    """
    show on 'run window' and can't see clearly but can get every nucleotide's position
    :param lst_alg_filled:a filled dot matrix, list
    :return:None
    """
    alg_output = []
    for j in range(len(lst_alg_filled)):
        temp = ''.join(lst_alg_filled[j])
        alg_output.append(temp)
        for i in range(len(alg_output)):
            print(alg_output[i])
    return None


def show_picture(lst_alg_filled, win_size):
    """
    count lst_alg_filled to get x and y, then draw a picture
    :param lst_alg_filled: a filled dot matrix, list
    :return: None
    """
    x_values = []
    y_values = []
    for i, row in enumerate(lst_alg_filled):
        for j, nt in enumerate(row):
            if nt == '*':
                x_values.append(j)
                y_values.append(i)
    #   painting picture
    plt.figure(dpi=140, figsize=(32, 32))
    plt.scatter(x_values, y_values, c='red', edgecolors='none', s=5)
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.axis([0, len(lst_alg_filled[0]), 0, len(lst_alg_filled)])
    plt.title("window size = {}".format(win_size), fontsize=24)
    plt.xlabel("sequence a", fontsize=12)
    plt.ylabel("sequence b", fontsize=12)
    plt.savefig("/home/andy/Documents/Learning/Bioinformatics/experiment/"
                "2_Entrez/Zea mays/dot_matrix/NM/sub1&sub2_NM{}.png".format(win_size),  bbox_inches='tight')
    # plt.show()
    return None