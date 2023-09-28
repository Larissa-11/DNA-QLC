"""
Name: Data Handle

Coder: Zheng Yanfen

Current Version: 1

Function(s):
Conversion of DNA sequences and binary document
"""

import math
import sys, time

import utils.log as log
from utils.monitor import Monitor


# noinspection PyProtectedMember
def read_binary_from_all(binary_str, segment_length, need_log=False):
    """
    introduction: Split binary.

    :param binary_str: Binary string.
                  Type: string

    :param segment_length: The binary segment length used for DNA sequence generation.
                           Considering current DNA synthesis technique limitation,
                           we usually set 360 as default segment length.

    :param need_log: choose to output log file or not.

    :return matrix: A matrix in which each row represents a binary segment that will be used for DNA sequence generation.
                    Type: two-dimensional list(int)
    """

    m = Monitor()
    try:

        # Open selected file

        if need_log:
            log.output(log.NORMAL, str(__name__), str(sys._getframe().f_code.co_name),
                       "Read binary from Binary string ")

        size = len(binary_str)
        matrix = [[0 for _ in range(segment_length)] for _ in range(math.ceil(size / segment_length))]
        row = 0
        col = 0

        for bit_index in range(size):
            matrix[row][col] = int(binary_str[bit_index])
            col += 1
            if col == segment_length:
                col = 0
                row += 1
        # print(matrix[row - 1])
        # print(matrix[row])
        if col < segment_length:
            for i in range(col):
                if matrix[row][col - 1] != matrix[row - 1][col - (1 + i)]:
                    matrix[row][col:segment_length] = matrix[row - 1][col - i:segment_length - i]
                    break
        # print(matrix[row - 1])
        # print(matrix[row])
        if int(len(str(bin(len(matrix)))) - 2) * 7 > segment_length:
            if need_log:
                log.output(log.WARN, str(__name__), str(sys._getframe().f_code.co_name),
                           "The proportion of index in whole sequence may be high. \n"
                           "It is recommended to increase the length of output DNA sequences "
                           "or to divide the file into more segment pools")
        return matrix, size

    except IOError:
        log.output(log.ERROR, str(__name__), str(sys._getframe().f_code.co_name),
                   "The operation was not performed correctly. Please execute the operation again!")


# noinspection PyBroadException,PyProtectedMember
# def write_all_from_binary(path, matrix, size, need_log=False):
#     """
#     introduction: Writing binary matrix to document.
#
#     :param path: File path.
#                   Type: string
#
#     :param matrix: A matrix in which each row represents a binary segment that will be used for DNA sequence generation.
#                     Type: two-dimensional list(int)
#
#     :param size: This refers to file size, to reduce redundant bits when transferring DNA to binary files.
#                   Type: int
#
#     :param need_log: choose to output log file or not.
#     """
#     m = Monitor()
#
#     try:
#         with open(path, "wb+") as file:
#             if need_log:
#                 log.output(log.NORMAL, str(__name__), str(sys._getframe().f_code.co_name),
#                            "Write file from binary matrix: " + path)
#
#             # Change bit to byte (8 -> 1), and write a file as bytes
#             bit_index = 0
#             temp_byte = 0
#             for row in range(len(matrix)):
#                 if need_log:
#                     m.output(row + 1, len(matrix))
#                 for col in range(len(matrix[0])):
#                     bit_index += 1
#                     temp_byte *= 2
#                     temp_byte += matrix[row][col]
#                     if bit_index == 8:
#                         if size > 0:
#                             file.write(struct.pack("B", int(temp_byte)))
#                             bit_index = 0
#                             temp_byte = 0
#                             size -= 1
#     except IOError:
#         log.output(log.ERROR, str(__name__), str(sys._getframe().f_code.co_name),
#                    "The file selection operation was not performed correctly. Please execute the operation again!")
#

# noinspection PyBroadException,PyProtectedMember
def read_dna_file(path, need_log=False):
    """
    introduction: Reading DNA sequence set from documents.

    :param path: File path.
                  Type: string

    :return dna_sequences: A corresponding DNA sequence string in which each row acts as a sequence.
                           Type: one-dimensional list(string)

    :param need_log: need output log.
    """

    m = Monitor()

    dna_sequences = []

    try:
        with open(path, "r") as file:
            if need_log:
                log.output(log.NORMAL, str(__name__), str(sys._getframe().f_code.co_name),
                           "Read DNA sequences from file: " + path)

            # Read current file by line
            lines = file.readlines()
            for index in range(len(lines)):
                if need_log:
                    m.output(index + 1, len(lines))
                    time.sleep(0.01)
                line = lines[index]
                dna_sequences.append([line[col] for col in range(len(line) - 1)])
                # for i in range(0, len(dna_sequences[0]),2):
                #     if dna_sequences[index][i:i+2] == ['T', 'A']:
                #         dna_sequences[index] = dna_sequences[index][0:i]
                #         break
                #     if dna_sequences[index][i:i+2] == ['G', 'C']:
                #         dna_sequences[index] = dna_sequences[index][0:i+4]
                #         break
                #     if dna_sequences[index][i:i+2] == ['A', 'T']:
                #         dna_sequences[index] = dna_sequences[index][0:i+4]
                #         break
        return dna_sequences
    except IOError:
        log.output(log.ERROR, str(__name__), str(sys._getframe().f_code.co_name),
                   "The file selection operation was not performed correctly. Please execute the operation again!")


# noinspection PyProtectedMember,PyBroadException
def write_dna_file(path, dna_sequences, need_log=False):
    """
    introduction: Writing DNA sequence set to documents.

    :param path: File path.
                  Type: string

    :param dna_sequences: Generated DNA sequences.
                          Type: one-dimensional list(string)

    :param need_log: choose to output log file or not.
    """

    m = Monitor()

    try:
        with open(path, "w") as file:
            if need_log:
                log.output(log.NORMAL, str(__name__), str(sys._getframe().f_code.co_name),
                           "Write DNA sequences to file: " + path)
            for row in range(len(dna_sequences)):
                if need_log:
                    m.output(row + 1, len(dna_sequences))
                    time.sleep(0.01)
                file.write("".join(dna_sequences[row]) + "\n")
        return dna_sequences
    except IOError:
        log.output(log.ERROR, str(__name__), str(sys._getframe().f_code.co_name),
                   "The file selection operation was not performed correctly. Please execute the operation again!")


def sep_four(n):  # 把二进制数按4位分割
    mylist = []
    for i in range(0, len(n) // 4):
        a = int(n[4 * i:4 * i + 4], 2)
        mylist.append("{:x}".format(a))  # 转成16进制，并添加到列表中
    return mylist


def sep_Sixteen(n):  # 把二进制数按4位分割
    mylist = []
    for i in range(0, len(n) // 16):
        a = int(n[16 * i:16 * i + 16], 2)
        mylist.append(format(a))  # 转成10进制，并添加到列表中
    return mylist


def find_all(string, sub):
    start = 0
    pos = []
    while True:
        start = string.find(sub, start)
        if start == -1:
            return pos
        pos.append(start)
        start += len(sub)


def mybin(num):
    numm = num.encode('utf-8')
    nummm = int(numm, 16)
    bstr = bin(nummm)
    l = (len(bstr) - 2) % 4
    if l > 0:
        bstr = bstr[:2] + ('0' * (4 - l)) + bstr[2:]
    bstr = bstr[2:]
    return bstr


def getPlans(lis, CC, jude=True):
    if jude: lis = [[[i] for i in lis[0]]] + lis[1:]
    if len(lis) > 2:
        for i in lis[0]:
            for j in lis[1]:
                getPlans([[i + [j]]] + lis[2:], CC, False)
    elif len(lis) == 2:
        for i in lis[0]:
            for j in lis[1]:
                CC.append(i + [j])
    return CC
def getNumofCommonSubstr(str1, str2):
    lstr1 = len(str1)
    lstr2 = len(str2)
    record = [[0 for i in range(lstr2 + 1)] for j in range(lstr1 + 1)]
    maxNum = 0
    p = 0

    for i in range(lstr1):
        for j in range(lstr2):
            if str1[i] == str2[j]:
                record[i + 1][j + 1] = record[i][j] + 1
                if record[i + 1][j + 1] > maxNum:
                    maxNum = record[i + 1][j + 1]
                    p = i + 1
    return lstr2 - maxNum
