import sys, binascii, pickle, time
from utils import log, data_handle, index_operator
from utils.monitor import Monitor

import numpy as np


def decode(input_path=None, output_path=None, has_index=True, need_log=False):
    """
       introduction: Use the selected method, convert DNA sequence set to the binary
                     file and output the binary file.

       :param input_path: The path of DNA sequence set you need to convert.
                          Type: String.

       :param output_path: The path of binary file consistent with previous
                           documents.
                            Type: String.

       :param has_index: Declare whether the DNA sequences contain binary sequence
                         indexes.
                          Type: bool.

       :param need_log: Show the log.
       """
    if input_path is None or len(input_path) == 0:
        log.output(log.ERROR, str(__name__), str(sys._getframe().f_code.co_name),
                   "The input file path is not valid!")

    if output_path is None or len(output_path) == 0:
        log.output(log.ERROR, str(__name__), str(sys._getframe().f_code.co_name),
                   "The output file path is not valid!")
    dna_sequences = data_handle.read_dna_file(input_path, need_log)
    Monitor().restore()
    time.sleep(0.01)
    if need_log:
        log.output(log.NORMAL, str(__name__), str(sys._getframe().f_code.co_name),
                   "Convert DNA sequences to binary matrix.")
    matrix = convert_binaries(dna_sequences, need_log)
    Monitor().restore()
    time.sleep(0.01)
    if has_index:
        indexes, data_set = index_operator.divide_all(matrix, need_log)
        output_matrix = index_operator.sort_order(indexes, data_set, need_log)
        # j = len(output_matrix[0])
        # col = len(output_matrix[0])
        # row = len(output_matrix) - 1
        # i = 0
        # a = 1
        # print(output_matrix[row -1])
        # print(output_matrix[row])
        # while j:
        #     if output_matrix[row][-20:] == output_matrix[row - 1][col - i - 20:j]:
        #         for r in range(col - i - 21, 0, -1):
        #             if output_matrix[row][-20 - a] != output_matrix[row - 1][r]:
        #                 break
        #             a += 1
        #         b = col - 20 - a
        #         output_matrix[row] = output_matrix[row][0:b + 1]
        #         break
        #     else:
        #         j -= 1
        #         i += 1
        row = len(output_matrix) - 1
        str1 = ''.join(str(m) for m in output_matrix[row-1])
        str2 = ''.join(str(m) for m in output_matrix[row])
        res = data_handle.getNumofCommonSubstr(str1, str2)
        output_matrix[row] = output_matrix[row][0:res + 1]

    for i in range(len(output_matrix)):
        output_matrix[i] = ''.join(str(m) for m in output_matrix[i])
    output_matrix = ''.join(output_matrix)

    output_matrix_s = output_matrix.split('01001100010010010101001101010100')
    output_matrix_s.pop(0)
    output_matrix_16 = [[] for _ in range(len(output_matrix_s))]
    for i in range(0, len(output_matrix_s), 1):
        if i < len(output_matrix_s) - 2:
            output_matrix_16[i] = data_handle.sep_four(output_matrix_s[i])
            output_matrix_16[i] = ''.join(output_matrix_16[i])
            if len(output_matrix_16[i]) % 2 != 0:
                output_matrix_16[i] = output_matrix_16[i] + b'0'
            output_matrix_16[i] = [binascii.a2b_hex(output_matrix_16[i])]
        else:
            output_matrix_16[i] = data_handle.sep_Sixteen(output_matrix_s[i])
            for j in range(len(output_matrix_16[i])):
                output_matrix_16[i][j] = int(output_matrix_16[i][j])
            output_matrix_16[i] = tuple(output_matrix_16[i])
    with open(output_path, 'wb') as f:
        pickle.dump(output_matrix_16, file=f)


def convert_binaries(dna_sequences, need_log):
    """
    introduction: Convert DNA sequences to binary matrix.
                  One DNA sequence <-> two-line binaries.

    :param dna_sequences: The DNA sequence of len(matrix) rows.
                        Type: One-dimensional list(string).

    :param need_log: Show the log.

    :return matrix: The binary matrix corresponding to the DNA sequences.
                     Type: Two-dimensional list(int).
    """

    # matrix = [[0 for _ in range(len(dna_sequences[0]) // 2 * 3)] for _ in range(len(dna_sequences))]
    matrix = [[] for _ in range(len(dna_sequences))]
    for row in range(0, len(dna_sequences), 1):
        if need_log:
            Monitor().output(row + 1, len(dna_sequences))
            time.sleep(0.01)
        for i in range(0, len(dna_sequences[0]), 2):
            if dna_sequences[row][i:i + 2] == ['T', 'C']:
                l = [0, 0, 0]
                matrix[row].extend(l)
            elif dna_sequences[row][i:i + 2] == ['T', 'G']:
                l = [0, 0, 1]
                matrix[row].extend(l)
            elif dna_sequences[row][i:i + 2] == ['A', 'C']:
                l = [0, 1, 0]
                matrix[row].extend(l)
            elif dna_sequences[row][i:i + 2] == ['A', 'G']:
                l = [0, 1, 1]
                matrix[row].extend(l)
            elif dna_sequences[row][i:i + 2] == ['C', 'T']:
                l = [1, 0, 0]
                matrix[row].extend(l)
            elif dna_sequences[row][i:i + 2] == ['C', 'A']:
                l = [1, 0, 1]
                matrix[row].extend(l)
            elif dna_sequences[row][i:i + 2] == ['G', 'T']:
                l = [1, 1, 0]
                matrix[row].extend(l)
            elif dna_sequences[row][i:i + 2] == ['G', 'A']:
                l = [1, 1, 1]
                matrix[row].extend(l)
    for row in range(0, len(matrix), 1):
        index = []
        for j in range(len(matrix[0]) - 1):
            if np.log2(j + 1) - int(np.log2(j + 1)) == 0:
                index.extend([j])
        matrix[row].pop(-1)
        index.reverse()  # 对索引进行反转，使其从后往前删除
        for i in index:
            matrix[row].pop(i)
    return matrix
