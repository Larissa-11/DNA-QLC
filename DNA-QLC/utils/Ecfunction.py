import numpy as np
import copy


def subcreat(dna_sequence, sequences_Errorcorrection, Error_index_pc):
    index = len(Error_index_pc[0])
    dna_create_all = []

    for row in range(0, len(Error_index_pc), 1):
        i = 0
        p = 0
        dna_create = [[0 for _ in range(len(dna_sequence))] for _ in
                      range(2 ** index)]
        for j in range(0, len(dna_sequence), 1):
            if j in Error_index_pc[row]:
                if j == 0:
                    dna_create[i][j] = list(sequences_Errorcorrection.get(j))[0]
                    dna_create[i + 1][j] = list(sequences_Errorcorrection.get(j))[1]
                    p += 1
                else:
                    for i in range(0, 2 ** p, 1):
                        dna_create[i][0:j + 1] = dna_create[i][0:j] + list(list(sequences_Errorcorrection.get(j))[0])
                        dna_create[i + 2 ** p][0:j + 1] = dna_create[i][0:j] + list(
                            list(sequences_Errorcorrection.get(j))[1])
                    p += 1
            elif j not in Error_index_pc[row]:
                if dna_create[0][0] == 0:
                    dna_create[0][j] = dna_sequence[j]
                else:
                    b = 0
                    a = 0
                    while dna_create[b][0] != 0:
                        a += 1
                        b += 1
                        if b == 2 ** index:
                            break
                    for c in range(0, a, 1):
                        dna_create[c][j] = dna_sequence[j]
        dna_create_all = dna_create_all + dna_create
        dna_create_all_unique = []
        for i in dna_create_all:
            if i not in dna_create_all_unique:
                dna_create_all_unique.append(i)
    sequence = Error_correction(dna_create_all_unique)
    return sequence


def delcreat(sequence, dna_create_all, row):
    for j in range(0, len(sequence), 2):
        if j + 1 != len(sequence):
            if sequence[j:j + 2] == ['A', 'T']:
                sequences_dict = {j: 'A', j + 1: 'T'}
                return delerrcreat(sequences_dict, sequence, dna_create_all, row)
            elif sequence[j:j + 2] == ['T', 'A']:
                sequences_dict = {j: 'T', j + 1: 'A'}
                return delerrcreat(sequences_dict, sequence, dna_create_all, row)
            elif sequence[j:j + 2] == ['C', 'G']:
                sequences_dict = {j: 'C', j + 1: 'G'}
                return delerrcreat(sequences_dict, sequence, dna_create_all, row)
            elif sequence[j:j + 2] == ['G', 'C']:
                sequences_dict = {j: 'G', j + 1: 'C'}
                return delerrcreat(sequences_dict, sequence, dna_create_all, row)
            elif sequence[j:j + 2] == ['A', 'A']:
                sequences_dict = {j: 'A', j + 1: 'A'}
                return delerrcreat(sequences_dict, sequence, dna_create_all, row)
            elif sequence[j:j + 2] == ['T', 'T']:
                sequences_dict = {j: 'T', j + 1: 'T'}
                return delerrcreat(sequences_dict, sequence, dna_create_all, row)
            elif sequence[j:j + 2] == ['C', 'C']:
                sequences_dict = {j: 'C', j + 1: 'C'}
                return delerrcreat(sequences_dict, sequence, dna_create_all, row)
            elif sequence[j:j + 2] == ['G', 'G']:
                sequences_dict = {j: 'G', j + 1: 'G'}
                return delerrcreat(sequences_dict, sequence, dna_create_all, row)
        else:
            dna_create_all_end = []
            if sequence[len(sequence) - 1] == 'A':
                for i in range(len(dna_create_all)):
                    dna_create_all_end.append(dna_create_all[i] + ['C'])
                    dna_create_all_end.append(dna_create_all[i] + ['G'])
                    dna_create_all_end.append(dna_create_all[i][0:len(sequence) - 1] + ['C'] + ['A'])
                    dna_create_all_end.append(dna_create_all[i][0:len(sequence) - 1] + ['G'] + ['A'])
            elif sequence[len(sequence) - 1] == 'T':
                for i in range(len(dna_create_all)):
                    dna_create_all_end.append(dna_create_all[i] + ['C'])
                    dna_create_all_end.append(dna_create_all[i] + ['G'])
                    dna_create_all_end.append(dna_create_all[i][0:len(sequence) - 1] + ['C'] + ['T'])
                    dna_create_all_end.append(dna_create_all[i][0:len(sequence) - 1] + ['G'] + ['T'])
            elif sequence[len(sequence) - 1] == 'C':
                for i in range(len(dna_create_all)):
                    dna_create_all_end.append(dna_create_all[i] + ['A'])
                    dna_create_all_end.append(dna_create_all[i] + ['T'])
                    dna_create_all_end.append(dna_create_all[i][0:len(sequence) - 1] + ['A'] + ['C'])
                    dna_create_all_end.append(dna_create_all[i][0:len(sequence) - 1] + ['T'] + ['C'])
            elif sequence[len(sequence) - 1] == 'G':
                for i in range(len(dna_create_all)):
                    dna_create_all_end.append(dna_create_all[i] + ['A'])
                    dna_create_all_end.append(dna_create_all[i] + ['T'])
                    dna_create_all_end.append(dna_create_all[i][0:len(sequence) - 1] + ['A'] + ['G'])
                    dna_create_all_end.append(dna_create_all[i][0:len(sequence) - 1] + ['T'] + ['G'])
            dna = Error_correction(dna_create_all_end)
            return dna


def delerrcreat(sequences_dict, sequence, dna_create_all, row):
    if len(dna_create_all) != 0:
        dna_create_all.pop(0)
    index = sequences_dict.keys()
    index = list(index)
    if index[-1] <= 15:
        dna_create = []
        for i in range(0, index[-1], 1):
            if sequence[index[-1] - 1 - i] == 'A' or sequence[index[-1] - 1 - i] == 'T':
                dna_create.append(sequence[0:index[-1] - i] + ['C'] + sequence[index[-1] - i:index[-1]])
                dna_create.append(sequence[0:index[-1] - i] + ['G'] + sequence[index[-1] - i:index[-1]])
            else:
                dna_create.append(sequence[0:index[-1] - i] + ['A'] + sequence[index[-1] - i:index[-1]])
                dna_create.append(sequence[0:index[-1] - i] + ['T'] + sequence[index[-1] - i:index[-1]])
        for i in range(0, index[-1], 1):
            if sequence[index[-1] - i - 1] == 'A' or sequence[index[-1] - i - 1] == 'T':
                dna_create.append(sequence[0:index[0] - i] + ['C'] + sequence[index[0] - i:index[-1]])
                dna_create.append(sequence[0:index[0] - i] + ['G'] + sequence[index[0] - i:index[-1]])
            else:
                dna_create.append(sequence[0:index[0] - i] + ['A'] + sequence[index[0] - i:index[-1]])
                dna_create.append(sequence[0:index[0] - i] + ['T'] + sequence[index[0] - i:index[-1]])
        if sequence[0] == 'A' or sequence[0] == 'T':
            dna_create.append(['C'] + sequence[0:index[-1]])
            dna_create.append(['G'] + sequence[0:index[-1]])
        else:
            dna_create.append(['A'] + sequence[0:index[-1]])
            dna_create.append(['T'] + sequence[0:index[-1]])

        index_dna = []
        for r in range(len(dna_create)):
            for c in range(0, len(dna_create[r]), 2):
                if dna_create[r][c:c + 2] == ['A', 'T']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['T', 'A']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['A', 'A']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['T', 'T']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['G', 'C']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['C', 'G']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['G', 'G']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['C', 'C']:
                    index_dna.append(r)
        index_dna.reverse()
        new_index_dna = list(set(index_dna))
        new_index_dna.sort(key=index_dna.index)
        for r in new_index_dna:
            dna_create.pop(r)
        for r in range(len(dna_create)):
            dna_create[r] = dna_create[r] + sequence[index[-1]:len(sequence)]

        dna_create_all = dna_create_all + dna_create
        dna_create_all_unique = []
        for i in dna_create_all:
            if i not in dna_create_all_unique:
                dna_create_all_unique.append(i)

        if len(dna_create_all_unique[0]) < row:
            return delcreat(dna_create_all_unique[0], dna_create_all_unique, row)

        else:
            dna = Error_correction(dna_create_all_unique)
            return dna
    else:
        dna_create = []
        for i in range(0, 15, 1):
            if sequence[index[-1] - i - 1] == 'A' or sequence[index[-1] - i - 1] == 'T':
                dna_create.append(sequence[0:index[-1] - i] + ['C'] + sequence[index[-1] - i:index[-1]])
                dna_create.append(sequence[0:index[-1] - i] + ['G'] + sequence[index[-1] - i:index[-1]])
            else:
                dna_create.append(sequence[0:index[-1] - i] + ['A'] + sequence[index[-1] - i:index[-1]])
                dna_create.append(sequence[0:index[-1] - i] + ['T'] + sequence[index[-1] - i:index[-1]])
        for i in range(0, 15, 1):
            if sequence[index[-1] - i - 1] == 'A' or sequence[index[-1] - i - 1] == 'T':
                dna_create.append(sequence[0:index[0] - i] + ['C'] + sequence[index[0] - i:index[-1]])
                dna_create.append(sequence[0:index[0] - i] + ['G'] + sequence[index[0] - i:index[-1]])
            else:
                dna_create.append(sequence[0:index[0] - i] + ['A'] + sequence[index[0] - i:index[-1]])
                dna_create.append(sequence[0:index[0] - i] + ['T'] + sequence[index[0] - i:index[-1]])
        index_dna = []
        for r in range(len(dna_create)):
            for c in range(0, len(dna_create[r]), 2):
                if dna_create[r][c:c + 2] == ['A', 'T']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['T', 'A']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['A', 'A']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['T', 'T']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['G', 'C']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['C', 'G']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['G', 'G']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['C', 'C']:
                    index_dna.append(r)
        index_dna.reverse()
        new_index_dna = list(set(index_dna))
        new_index_dna.sort(key=index_dna.index)
        for r in new_index_dna:
            dna_create.pop(r)
        for r in range(len(dna_create)):
            dna_create[r] = dna_create[r] + sequence[index[-1]:len(sequence)]

        dna_create_all = dna_create_all + dna_create
        dna_create_all_unique = []
        for i in dna_create_all:
            if i not in dna_create_all_unique:
                dna_create_all_unique.append(i)
        if len(dna_create_all_unique[0]) < row:
            return delcreat(dna_create_all_unique[0], dna_create_all_unique, row)

        else:
            dna = Error_correction(dna_create_all_unique)
            return dna


def insercreat(sequence, dna_create_all, row):
    for j in range(0, len(sequence), 2):
        if j + 2 != len(sequence) - 1:
            if sequence[j:j + 2] == ['A', 'T']:
                sequences_dict = {j: 'A', j + 1: 'T'}
                DNA = insererrcreat(sequences_dict, sequence, dna_create_all, row)
                return DNA
            elif sequence[j:j + 2] == ['T', 'A']:
                sequences_dict = {j: 'T', j + 1: 'A'}
                DNA = insererrcreat(sequences_dict, sequence, dna_create_all, row)
                return DNA
            elif sequence[j:j + 2] == ['C', 'G']:
                sequences_dict = {j: 'C', j + 1: 'G'}
                DNA = insererrcreat(sequences_dict, sequence, dna_create_all, row)
                return DNA
            elif sequence[j:j + 2] == ['G', 'C']:
                sequences_dict = {j: 'G', j + 1: 'C'}
                DNA = insererrcreat(sequences_dict, sequence, dna_create_all, row)
                return DNA
            elif sequence[j:j + 2] == ['A', 'A']:
                sequences_dict = {j: 'A', j + 1: 'A'}
                DNA = insererrcreat(sequences_dict, sequence, dna_create_all, row)
                return DNA
            elif sequence[j:j + 2] == ['T', 'T']:
                sequences_dict = {j: 'T', j + 1: 'T'}
                DNA = insererrcreat(sequences_dict, sequence, dna_create_all, row)
                return DNA
            elif sequence[j:j + 2] == ['C', 'C']:
                sequences_dict = {j: 'C', j + 1: 'C'}
                DNA = insererrcreat(sequences_dict, sequence, dna_create_all, row)
                return DNA
            elif sequence[j:j + 2] == ['G', 'G']:
                sequences_dict = {j: 'G', j + 1: 'G'}
                DNA = insererrcreat(sequences_dict, sequence, dna_create_all, row)
                return DNA
        else:
            dna_create_all_end = []
            for i in range(1,15,1):
                DNA = copy.deepcopy(sequence)
                DNA.pop(len(sequence[0]) - i)
                dna_create_all_end.append(DNA)
            index_dna = []
            for r in range(len(dna_create_all_end)):
                for c in range(0, len(dna_create_all_end[r]), 2):
                    if dna_create_all_end[r][c:c + 2] == ['A', 'T']:
                        index_dna.append(r)
                    elif dna_create_all_end[r][c:c + 2] == ['T', 'A']:
                        index_dna.append(r)
                    elif dna_create_all_end[r][c:c + 2] == ['A', 'A']:
                        index_dna.append(r)
                    elif dna_create_all_end[r][c:c + 2] == ['T', 'T']:
                        index_dna.append(r)
                    elif dna_create_all_end[r][c:c + 2] == ['G', 'C']:
                        index_dna.append(r)
                    elif dna_create_all_end[r][c:c + 2] == ['C', 'G']:
                        index_dna.append(r)
                    elif dna_create_all_end[r][c:c + 2] == ['G', 'G']:
                        index_dna.append(r)
                    elif dna_create_all_end[r][c:c + 2] == ['C', 'C']:
                        index_dna.append(r)
            index_dna.reverse()
            new_index_dna = list(set(index_dna))
            new_index_dna.sort(key=index_dna.index)
            for r in new_index_dna:
                dna_create_all_end.pop(r)
            dna = Error_correction(dna_create_all_end)
            return dna




def insererrcreat(sequences_dict, sequence, dna_create_all, row):
    if len(dna_create_all) != 0:
        dna_create_all.pop(0)
    index = sequences_dict.keys()
    index = list(index)
    if index[-1] <= 15:
        dna_create = []
        for i in range(index[-1], -1, -1):
            sequence_c = copy.deepcopy(sequence)
            sequence_c.pop(i)
            dna_create.append(sequence_c[0:index[-1]])
        index_dna = []
        for r in range(len(dna_create)):
            for c in range(0, len(dna_create[r]), 2):
                if dna_create[r][c:c + 2] == ['A', 'T']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['T', 'A']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['A', 'A']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['T', 'T']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['G', 'C']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['C', 'G']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['G', 'G']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['C', 'C']:
                    index_dna.append(r)
        index_dna.reverse()
        new_index_dna = list(set(index_dna))
        new_index_dna.sort(key=index_dna.index)
        for r in new_index_dna:
            dna_create.pop(r)
        for r in range(len(dna_create)):
            dna_create[r] = dna_create[r] + sequence[index[-1]+1:len(sequence)]

        dna_create_all = dna_create_all + dna_create
        dna_create_all_unique = []
        for i in dna_create_all:
            if i not in dna_create_all_unique:
                dna_create_all_unique.append(i)

        if len(dna_create_all_unique[0]) > row:
            return insercreat(dna_create_all_unique[0], dna_create_all_unique, row)

        else:
            dna = Error_correction(dna_create_all_unique)
            return dna
    else:
        dna_create = []
        for i in range(index[-1], index[-1] - 15, -1):
            sequence_c = copy.deepcopy(sequence)
            sequence_c.pop(i)
            dna_create.append(sequence_c[0:index[-1]])
        index_dna = []
        for r in range(len(dna_create)):
            for c in range(0, len(dna_create[r]), 2):
                if dna_create[r][c:c + 2] == ['A', 'T']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['T', 'A']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['A', 'A']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['T', 'T']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['G', 'C']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['C', 'G']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['G', 'G']:
                    index_dna.append(r)
                elif dna_create[r][c:c + 2] == ['C', 'C']:
                    index_dna.append(r)
        index_dna.reverse()
        new_index_dna = list(set(index_dna))
        new_index_dna.sort(key=index_dna.index)
        for r in new_index_dna:
            dna_create.pop(r)
        for r in range(len(dna_create)):
            dna_create[r] = dna_create[r] + sequence[index[-1]+1:len(sequence)]

        dna_create_all = dna_create_all + dna_create
        dna_create_all_unique = []
        for i in dna_create_all:
            if i not in dna_create_all_unique:
                dna_create_all_unique.append(i)
        if len(dna_create_all_unique[0]) > row:
            return insercreat(dna_create_all_unique[0], dna_create_all_unique, row)

        else:
            dna = Error_correction(dna_create_all_unique)
            return dna


def Error_correction(dna_sequence_Errorcorrection):
    dna_index = []
    dna_dc = []
    for row in range(0, len(dna_sequence_Errorcorrection), 1):
        Binary_error_correction = []
        for i in range(0, len(dna_sequence_Errorcorrection[0]), 2):
            if dna_sequence_Errorcorrection[row][i:i + 2] == ['T', 'C']:
                l = [0, 0, 0]
                Binary_error_correction.extend(l)
            elif dna_sequence_Errorcorrection[row][i:i + 2] == ['T', 'G']:
                l = [0, 0, 1]
                Binary_error_correction.extend(l)
            elif dna_sequence_Errorcorrection[row][i:i + 2] == ['A', 'C']:
                l = [0, 1, 0]
                Binary_error_correction.extend(l)
            elif dna_sequence_Errorcorrection[row][i:i + 2] == ['A', 'G']:
                l = [0, 1, 1]
                Binary_error_correction.extend(l)
            elif dna_sequence_Errorcorrection[row][i:i + 2] == ['C', 'T']:
                l = [1, 0, 0]
                Binary_error_correction.extend(l)
            elif dna_sequence_Errorcorrection[row][i:i + 2] == ['C', 'A']:
                l = [1, 0, 1]
                Binary_error_correction.extend(l)
            elif dna_sequence_Errorcorrection[row][i:i + 2] == ['G', 'T']:
                l = [1, 1, 0]
                Binary_error_correction.extend(l)
            elif dna_sequence_Errorcorrection[row][i:i + 2] == ['G', 'A']:
                l = [1, 1, 1]
                Binary_error_correction.extend(l)
        ind = []
        for i in range(len(Binary_error_correction)):
            ind.append(i + 1)
        pla_1 = np.dot(Binary_error_correction, ind)
        if pla_1 % (2 * len(Binary_error_correction)) == 0:
            dna_index.append(row)
            dna_dc.append(dna_sequence_Errorcorrection[row])
    return dna_dc


def cut(obj, sec):
    return [obj[i:i + sec] for i in range(0, len(obj), sec)]
