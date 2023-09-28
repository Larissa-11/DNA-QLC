from numpy import fromfile, uint8


def read_bits_from_file(path, need_logs=True):
    if need_logs:
        print("Read binary matrix from file: " + path)

    values = fromfile(file=path, dtype=uint8)
    if need_logs:
        print("There are " + str(len(values) * 8) + " bits in the inputted file. ")

    return len(values) * 8


def read_dna_file(path, need_logs=True):
    dna_sequences = []

    with open(path, "r") as file:
        if need_logs:
            print("Read DNA sequences from file: " + path)

        # Read current file by line
        lines = file.readlines()

        for index, line in enumerate(lines):
            dna_sequences.append(list(line.replace("\n", "")))

    return dna_sequences


def motifs(sequence,motifs_count):
    motifs= ["GGC", "GAATTC"]

    for missing_segment in motifs:
        if missing_segment in "".join(sequence):
            motifs_count ="".join(sequence).count(missing_segment) + motifs_count
    return motifs_count


img_path = '../images/Mona Lisa.jpg'
DNA_path = '../Data/Yin-Yang.dna'
bit_size = read_bits_from_file(img_path)
dna_sequences = read_dna_file(DNA_path)
a = len(dna_sequences)
b = len(dna_sequences[0])
nt_size = a * b
print("Number of oligos:", a)
print("Net information density:%.2f" %(bit_size / nt_size))

gc_all = []
for i in range(a):
    g = dna_sequences[i].count('G')
    c = dna_sequences[i].count('C')
    seq_len = len(dna_sequences[i])
    gc_content = (g + c) / seq_len
    gc_all.append(gc_content)
max_gc = max(gc_all)
min_gc = min(gc_all)
print('The minimum GC content is :%.0f%%' % (max_gc * 100))
print('The maximum GC content is :%.0f%%' % (min_gc * 100))

motifs_count = 0
for i in range(a):
    motifs_count = motifs(dna_sequences[i], motifs_count)

print('The motifs_count is :%d' %(motifs_count))

