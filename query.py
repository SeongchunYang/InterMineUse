# Author : Seongchun Yang
# Affiliation : Kyoto University

# Commandline version of mousemine query.
# Input list should be provided as a text with each line denoting a GOterm.
# DO NOT add comma, period or others at the end of each line after the GOterm.

import os
import pandas as pd
from mousemine.mousemine_query import grab, save_to_csv

with open(input('Provide an absolute path for the text file (.txt) containing GOterms: ')) as file:
    lines = file.readlines()
    terms = [line.rstrip() for line in lines]

data = grab(terms)
save_to_csv(data,filepath=os.path.curdir)
