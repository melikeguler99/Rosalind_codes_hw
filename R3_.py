#!/usr/bin/env python
# coding: utf-8

# In[ ]:


lines = [line.strip() for line in open('R3.txt')]

# Ordering contigs by their lengths from the longest (c1) to the shortest (cn).
c_lengths = sorted([len(a) for a in lines])[::-1]

# the length of contig number 
total = sum(c_lengths)

#Calculate the cutoff value by summing all contigs and multiplying by the threshold percentage (x).

# N50 calculation

for N50_val in c_lengths:
    length_sum = sum((L for L in c_lengths if L >= N50_val))
    if length_sum > (total/2):
        break
N50 = N50_val

# N75 Calculation

for N75_val in c_lengths:
    length_sum = sum((L for L in c_lengths if L >= N75_val))
    if length_sum > 0.75 * total:
        break
N75 = N75_val

print(f"{N50} {N75}")

