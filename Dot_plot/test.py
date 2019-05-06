filename = "/home/andy/Desktop/sequence.fasta"
with open(filename) as file_o:
    lines = file_o.readlines()
    seq_a = ''
    for line in lines:
        seq_a = seq_a.join(line)
    print(seq_a)
