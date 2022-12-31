#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Bio import SeqIO

sequences = [] 

# reading fasta
for seq_record in SeqIO.parse("R1.txt", "fasta"):
    sequences.append(str(seq_record.seq))
    l = len(seq_record)

# finding p_distance    
def distance(s1, s2):
    d = 0
    for i in range(l):
        if s1[i] != s2[i]:
            d += 1
    p_dist = d/l
    return '%.5f'% (p_dist) #according to sample output .5f

# making matrix
for i in range(len(sequences)):
    for j in range(len(sequences)):
        print(distance(sequences[i],sequences[j]), end=" ")
    print()

