import function

# Information
print("Notation:\n"
      "Default threshold is 100%. \n")

# input sequences and window size
# seq_a, seq_b, win_size = function.input_sequence()

# test sequence
if not seq_a:
    seq_a = '''CAGGACGACCCAAGCAAGCAAGCAAGCAGCGAGTACATACATACATACTAGGCAGCCAGGCAGCCATGGC
    GCCCACCGTGATGATGGCCTCGTCGGCCACCGCCGTCGCTCCGTTCCAGGGGCTCAAGTCCACCGCCAGC
    CTCCCCGTCGCCCGCCGCTCCTCCAGAAGCCTCGGCAACGTCAGCAACGGCGGAAGGATCCGGTGCATGC
    AGGTGTGGCCGGCCTACGGCAACAAGAAGTTCGAGACGCTGTCGTACCTGCCGCCGCTGTCGACGGACGA
    CCTGCTGAAGCAGGTGGACTACCTGCTGCGCAACGGCTGGATACCCTGCCTCGAGTTCAGCAAGGTCGGC
    TTCGTGTACCGCGAGAACTCCACCTCCCCGTGCTACTACGACGGCCGCTACTGGACCATGTGGAAGCTGC
    CCATGTTCGGCTGCAACGACGCCACCCAGGTGTACAAGGAGCTGCAGGAGGCCATCAAATCCTACCCGGA
    CGCCTTCCACCGCGTCATCGGCTTCGACAACATCAAGCAGACGCAGTGCGTCAGCTTCATCGCCTACAAG
    CCCCCGGGCAGCGACTAGACCGCGCCCGCCGGCCGCCCCCCGCCGGCTAGCTAGCTAGCTAGCTCCTGCG
    TGAGCTAGTAGCTAGTGCCATGCGTCGTCTCTGTCGTTCGGTTTTGCTTCGGGTCACCGTACCCTTTGCT
    TGCTTGGTTTCTTCTTTCCTTTTTTCCTTTTTTTTTTCTTCTTTTCCCCGGCCATGGTTCCTTTGCTTTC
    AGCAGTTCTCTGTGATGTGATGTATCCATTGTTGCAAGCATGCATGGCCTTGCATTGGCT'''
if not seq_b:
    seq_b = '''GTCCCACATCCGCTTCGTCACGCCCCAACGAGAGGCGGACGCGGATCCAGCGACATGGACATGGCTCTAT
    ATATGCCGTCGGTGGGGGAGCCCCTACAGGACGACCCAAGCAAGCAAGCTCGATCTACTACTACTACTAG
    CTGGTACACATACTAGCCAGCCTGCCAGCCAGCTTGCCATGGCGCCCACCGTGATGATGGCCTCGTCGGC
    AACCGCCGTCGCCCCGTTCCAGGGTCTCAAGTCCGCCGCCAGCCTCCCCGTCGCCCGCCGCAGCACCAGG
    AGCCTCGGCAACGTCAGCAACGGCGGAAGGATCCGGTGCATGCAGGTGTGGCCGGCCTACGGCAACAAGA
    AGTTCGAGACGCTGTCGTACCTGCCGCCGCTGTCGACGGACGACCTGCTGAAGCAGGTGGACTACCTGCT
    GCGCAACGGCTGGATACCCTGCCTCGAGTTCAGCAAGCTCGGGTTCGTGTACCGCGAGAACTCCACCTCC
    CCGTGCTACTACGACGGCCGCTACTGGACCATGTGGAAGCTGCCCATGTTCGGCTGCACCGACGCCACGC
    AGGTGTACAAGGAGCTGCAGGAGGCCATCGCCGCGTACCCGGACGCCTTCCACCGCGTCATCGGCTTCGA
    CAACGTCAGGCAGACGCAGTGCGTCAGCTTCATCGCCTACAAGCCCCCCGGCAGCGAGTAGAGACCGTGG
    CTAGATCGACCCATGGCCATGCCTCTGCCTGTTGATCGGATCACCTTCTTGCATTGGTTCCTCTCTCTCT
    CTCCCTCCTTTTTTTTCCCTTTATCTCATCATTTCTTTTCTCCTGCATGCAATGGTTCCTTTTGCTTCCA
    ACAATTCTCCTGCTGATGTATCCAGCATGGCATCATCCATCTACAATTACGTACGTAGTGCAACGACTGT
    CGATTCGTTGGGTGAGGAACATATATGTGAATGCAAGCTCCGGCTACCATACATGTGTAATGTGTAATAG
    ATATATATACAAAACTGCCGAGGCGCCGACAATACTTTAATAACTGGTCCTTTT'''

# win_size = 10
for win_size in range(1, 11):
    # initialization list
    lst_alg = function.initialization_list(seq_a, seq_b, win_size)

    # alignment
    lst_alg_filled = function.alignment(lst_alg, win_size)

    # output
    function.show_picture(lst_alg_filled, win_size)
