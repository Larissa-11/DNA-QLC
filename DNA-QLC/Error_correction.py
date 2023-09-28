import numpy as np
from utils import data_handle, Ecfunction
import copy

input_path = "./Data/Mona Lisa error.dna"
output_path = "./Data/error2/"

dna_sequences = data_handle.read_dna_file(input_path)
m = len(dna_sequences)
r = []
for i in range(0, m, 1):
    r.append(len(dna_sequences[i]))
row = max(r, key=r.count)
seq = []
delindex = []
insindex = []
for i in range(0, m, 1):
    if len(dna_sequences[i]) == row:  # Correct substitution errors
        sequences_index = {}
        sequences_Errorcorrection = {}
        for j in range(0, row, 2):
            if dna_sequences[i][j:j + 2] == ['A', 'T']:
                sequences_dict = {j: 'A', j + 1: 'T'}
                sequences_index.update(sequences_dict)
            elif dna_sequences[i][j:j + 2] == ['T', 'A']:
                sequences_dict = {j: 'T', j + 1: 'A'}
                sequences_index.update(sequences_dict)
            elif dna_sequences[i][j:j + 2] == ['C', 'G']:
                sequences_dict = {j: 'C', j + 1: 'G'}
                sequences_index.update(sequences_dict)
            elif dna_sequences[i][j:j + 2] == ['G', 'C']:
                sequences_dict = {j: 'G', j + 1: 'C'}
                sequences_index.update(sequences_dict)
            elif dna_sequences[i][j:j + 2] == ['A', 'A']:
                sequences_dict = {j: 'A', j + 1: 'A'}
                sequences_index.update(sequences_dict)
            elif dna_sequences[i][j:j + 2] == ['T', 'T']:
                sequences_dict = {j: 'T', j + 1: 'T'}
                sequences_index.update(sequences_dict)
            elif dna_sequences[i][j:j + 2] == ['C', 'C']:
                sequences_dict = {j: 'C', j + 1: 'C'}
                sequences_index.update(sequences_dict)
            elif dna_sequences[i][j:j + 2] == ['G', 'G']:
                sequences_dict = {j: 'G', j + 1: 'G'}
                sequences_index.update(sequences_dict)
        if sequences_index:
            index = sequences_index.keys()
            for j in range(0, len(dna_sequences[0]), 1):
                if j in index:
                    if sequences_index.get(j) == 'G':
                        sequences_Errorcorrection[j] = []
                        sequences_Errorcorrection[j].append('A')
                        sequences_Errorcorrection[j].append('T')
                    elif sequences_index.get(j) == 'C':
                        sequences_Errorcorrection[j] = []
                        sequences_Errorcorrection[j].append('A')
                        sequences_Errorcorrection[j].append('T')
                    elif sequences_index.get(j) == 'A':
                        sequences_Errorcorrection[j] = []
                        sequences_Errorcorrection[j].append('G')
                        sequences_Errorcorrection[j].append('C')
                    elif sequences_index.get(j) == 'T':
                        sequences_Errorcorrection[j] = []
                        sequences_Errorcorrection[j].append('G')
                        sequences_Errorcorrection[j].append('C')
            l = 0
            sequences_Error_list = [[0 for _ in range(2)] for _ in
                                    range(len(list(sequences_Errorcorrection.keys())) // 2)]
            sequences_Errorcorrection_index = list(sequences_Errorcorrection.keys())
            for index_i in range(0, len(list(sequences_Errorcorrection.keys())), 2):
                sequences_Error_list[l][0] = sequences_Errorcorrection_index[index_i]
                sequences_Error_list[l][1] = sequences_Errorcorrection_index[index_i + 1]
                l += 1
            Error_index_pc = list()
            if len(sequences_Error_list) == 1:
                Error_index_pc.append([sequences_Error_list[0][0]])
                Error_index_pc.append([sequences_Error_list[0][1]])
            else:
                Error_index_pc = data_handle.getPlans(sequences_Error_list, Error_index_pc)
            sequence = Ecfunction.subcreat(dna_sequences[i], sequences_Errorcorrection, Error_index_pc)
            if seq == []:
                if np.array(sequence).shape[0] == 1:
                    seq.append(sequence[0])
                else:
                    for i in range(0, len(sequence), 1):
                        seq.append(sequence[i])
            else:
                if np.array(sequence).shape[0] == 1:
                    for r in range(0, len(seq), 1):
                        seq[r].extend(sequence[0])
                else:
                    seqdna = list()
                    for r in range(0, len(seq), 1):
                        for i in range(0, len(sequence), 1):
                            temp_ = copy.deepcopy(seq[r])
                            seqdna.append(temp_)
                    seq = seqdna
                    j = 0
                    for r in range(0, len(seq), 1):
                        seq[r].extend(sequence[j])
                        j += 1
                        if j == len(sequence):
                            j = 0
        else:
            if seq == []:
                temp_ = copy.deepcopy(dna_sequences[i])
                seq.append(temp_)
            else:
                for j in range(0, len(seq), 1):
                    temp_ = copy.deepcopy(dna_sequences[i])
                    seq[j].extend(temp_)
    elif len(dna_sequences[i]) < row:  # Correct deletion errors
        dna_create_all = []
        sequence = Ecfunction.delcreat(dna_sequences[i], dna_create_all, row)
        delindex.append(i)
        if seq == []:
            if np.array(sequence).shape[0] == 1:
                seq.append(sequence[0])
            else:
                for i in range(0, len(sequence), 1):
                    seq.append(sequence[i])
        else:
            if np.array(sequence).shape[0] == 1:
                for r in range(0, len(seq), 1):
                    seq[r].extend(sequence[0])
            else:
                seqdna = list()
                for r in range(0, len(seq), 1):
                    for i in range(0, len(sequence), 1):
                        temp_ = copy.deepcopy(seq[r])
                        seqdna.append(temp_)
                seq = seqdna
                j = 0
                for r in range(0, len(seq), 1):
                    seq[r].extend(sequence[j])
                    j += 1
                    if j == len(sequence):
                        j = 0
    elif len(dna_sequences[i]) > row:  # Correct insertion errors
        dna_create_all = []
        sequence = Ecfunction.insercreat(dna_sequences[i], dna_create_all, row)
        insindex.append(i)
        if seq == []:
            if np.array(sequence).shape[0] == 1:
                seq.append(sequence[0])
            else:
                for i in range(0, len(sequence), 1):
                    seq.append(sequence[i])
        else:
            if np.array(sequence).shape[0] == 1:
                for r in range(0, len(seq), 1):
                    seq[r].extend(sequence[0])
            else:
                seqdna = list()
                for r in range(0, len(seq), 1):
                    for i in range(0, len(sequence), 1):
                        temp_ = copy.deepcopy(seq[r])
                        seqdna.append(temp_)
                seq = seqdna
                j = 0
                for r in range(0, len(seq), 1):
                    seq[r].extend(sequence[j])
                    j += 1
                    if j == len(sequence):
                        j = 0

for i in range(len(seq)):
    seq_part = Ecfunction.cut(seq[i], row)
    i_str = str(i)
    path = output_path + "Mona Lisa" + i_str + ".dna"
    with open(path, "w") as file:
        for j in range(len(seq_part)):
            file.write("".join(seq_part[j]) + "\n")
