from utils import log
import sys
from utils import data_handle, index_operator, LC
import numpy as np



def encode(binary_str, output_path, segment_length=290, need_log=False, need_index=True):
    """
        introduction: Use the selected method, convert the binary file to DNA sequence
                      set and output the DNA sequence set.


        :param binary_str: Binary string.
                            Type: String.

        :param output_path: The path of DNA sequence set you need to use to .
                             Type: String.

        :param need_index: Declare whether the binary sequence indexes are required
                           in the DNA sequences.
                            Type: bool.

        :param segment_length: The cut length of DNA sequence.
                          Considering current DNA synthesis factors, we usually
                          set 240 bases as a sequence.

        :param need_log: Show the log.
        """
    if binary_str is None or len(binary_str) == 0:
        log.output(log.ERROR, str(__name__), str(sys._getframe().f_code.co_name),
                   "The input file path is invalid!")

    if output_path is None or len(binary_str) == 0:
        log.output(log.ERROR, str(__name__), str(sys._getframe().f_code.co_name),
                   "The output file path is invalid!")
    input_matrix, size = data_handle.read_binary_from_all(binary_str, segment_length, need_log)
    if need_index:
        input_matrix, index_binary_length = index_operator.connect_all(input_matrix, need_log)
    input_matrix_lc = []
    for i in range(len(input_matrix)):
        ind=[]
        input_matrix_lc.append(LC.encode_lc(input_matrix[i]))
        for j in range(len(input_matrix_lc[0])):
            ind.append(j + 1)
        # pla_1 = np.dot(input_matrix_lc, ind)
    input_matrix_length = len(input_matrix_lc[0])
    dna_sequences = [[0 for _ in range(((input_matrix_length ) // 3) * 2)] for _ in
                     range(len(input_matrix_lc))]
    for row in range(0, len(input_matrix_lc)):
        col = 0
        for i in range(0, (input_matrix_length), 3):
            if input_matrix_lc[row][i:i + 3] == [0, 0, 0]:
                dna_sequences[row][col:col + 2:1] = ['T', 'C']
            elif input_matrix_lc[row][i:i + 3] == [0, 0, 1]:
                dna_sequences[row][col:col + 2] = ['T', 'G']
            elif input_matrix_lc[row][i:i + 3] == [0, 1, 0]:
                dna_sequences[row][col:col + 2] = ['A', 'C']
            elif input_matrix_lc[row][i:i + 3] == [0, 1, 1]:
                dna_sequences[row][col:col + 2] = ['A', 'G']
            elif input_matrix_lc[row][i:i + 3] == [1, 0, 0]:
                dna_sequences[row][col:col + 2] = ['C', 'T']
            elif input_matrix_lc[row][i:i + 3] == [1, 0, 1]:
                dna_sequences[row][col:col + 2] = ['C', 'A']
            elif input_matrix_lc[row][i:i + 3] == [1, 1, 0]:
                dna_sequences[row][col:col + 2] = ['G', 'T']
            else:
                dna_sequences[row][col:col + 2] = ['G', 'A']
            col = col + 2
    data_handle.write_dna_file(output_path, dna_sequences, need_log)

