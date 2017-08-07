import csv
import numpy as np
import sys
import pdb
csv.field_size_limit(sys.maxsize)

def load_csv(filename, delimiter='|'):
    data = []
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONE, delimiter=delimiter)
        for line in reader:
            data.append(line)
    return np.asarray(data)


def id_class():
  mapping = {}
  data = load_csv('data/train/training_variants', delimiter=",")
  for id,gene,mut_type,mut_class in data[1:]:
    mapping[id] = mut_class

  return mapping


