from utils import data_handle
import random

input_path = "../Data/Mona Lisa.dna"
output_path = "../Data/Mona Lisa error.dna"
nucleotide_insertion = 0.005
nucleotide_mutation = 0.01
nucleotide_deletion = 0.005
dna_sequences = data_handle.read_dna_file(input_path)

total_indices = [sequence_index for sequence_index in range(len(dna_sequences))]
chosen_index_insert = []
chosen_index_mutat = []
chosen_index_delet = []
# insertion errors
for insertion_iteration in range(int(len(dna_sequences) * nucleotide_insertion)):
    chosen_index = random.choice(total_indices)
    chosen_index_insert.append(chosen_index)
    dna_sequences[chosen_index].insert(random.randint(0, len(dna_sequences[chosen_index]) - 1),
                                       random.choice(['A', 'C', 'G', 'T']))

# mutation errors
for mutation_iteration in range(int(len(dna_sequences) * nucleotide_mutation)):
    chosen_index = random.choice(total_indices)
    if chosen_index not in chosen_index_insert:
        chosen_index_mutat.append(chosen_index)
    else:
        while chosen_index in chosen_index_insert:
            chosen_index = random.choice(total_indices)
        chosen_index_mutat.append(chosen_index)
    chosen_index_in_sequence = random.randint(0, len(dna_sequences[chosen_index]) - 1)
    chosen_nucleotide = dna_sequences[chosen_index][chosen_index_in_sequence]
    # dna_sequences[chosen_index][chosen_index_in_sequence] = \
    #     random.choice(list(filter(lambda nucleotide: nucleotide != chosen_nucleotide,
    #                               ['A', 'C', 'G', 'T'])))
    if chosen_nucleotide == "A" or chosen_nucleotide == "T":
        dna_sequences[chosen_index][chosen_index_in_sequence] = random.choice(['C', 'G'])
    else:
        dna_sequences[chosen_index][chosen_index_in_sequence] = random.choice(['A', 'T'])

# deletion errors
for deletion_iteration in range(int(len(dna_sequences) * nucleotide_deletion)):
    chosen_index = random.choice(total_indices)
    if chosen_index not in chosen_index_insert and chosen_index not in chosen_index_mutat:
        chosen_index_delet.append(chosen_index)
    else:
        while chosen_index in chosen_index_insert:
            chosen_index = random.choice(total_indices)
        chosen_index_delet.append(chosen_index)
    del dna_sequences[chosen_index][random.randint(0, len(dna_sequences[chosen_index]) - 1)]

data_handle.write_dna_file(output_path, dna_sequences)
