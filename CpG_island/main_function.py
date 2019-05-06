import numpy as np
import function


#  two models, order: A C G T
nt = np.array([['aa', 'ca', 'ga', 'ta'],
               ['ac', 'cc', 'gc', 'tc'],
               ['ag', 'cg', 'gg', 'tg'],
               ['at', 'ct', 'gt', 'tt']])
non_cpg = np.array([[0.180, 0.274, 0.426, 0.120],
                    [0.171, 0.368, 0.274, 0.188],
                    [0.161, 0.339, 0.375, 0.125],
                    [0.079, 0.355, 0.348, 0.182]])
cpg = np.array([[0.300, 0.205, 0.285, 0.210],
                [0.322, 0.298, 0.078, 0.302],
                [0.248, 0.246, 0.298, 0.208],
                [0.177, 0.239, 0.292, 0.292]])

#  increase two models for a fitness output 
cpg = cpg / cpg.max() * 2
non_cpg = non_cpg / non_cpg.max() * 2

#  get sequence
seq = input("Please enter your sequence: ")
#  test sequence
#  seq = """CGCGCGCCGCGCGCGCGCGCGCGCGCGCGCG"""

#  initialization
seq = seq.lower()

#  count number of every components for frequency matrix
f = [seq.count(j) for i in nt for j in i]  # get frequency of every components
f_after = []  # change to be matrix
for i in range(4):
    f_after.append(f[4*i:4*(i+1)])

#  compute the p_cpg and p_non_cpg
p_cpg = function.compute_p(cpg, f_after)
p_non_cpg = function.compute_p(non_cpg, f_after)

#  compute the times between p_cpg and p_non_cpg
p = p_cpg / p_non_cpg
print('p =', p, 'p_cpg =', p_cpg, 'p_non_cpg =', p_non_cpg)

#  judge if the sequence is consistent with CpG
if p > 1:
    print("Congratulation! This sequence is consistent with CpG island!")
else:
    print("Sorry, this sequence is not consistent with CpG island.")





