#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
print([x for x in Unique(['A','a','B','b'], ignore_case=True)])
print([x for x in Unique(data1)])



# Реализация задания 2