import utils as U
import pdb
import numpy as np
import csv
import os
import shutil

def make_dir(dirname):
    if os.path.isdir(dirname):
        shutil.rmtree(dirname)
        os.mkdir(dirname)
    else:
        os.mkdir(dirname)

def write_csv(filename, rows, headers):
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter="|")
        writer.writerow(headers)
        for row in rows:
            writer.writerow(row)


train_dir = 'data/train/train'
val_dir   = 'data/train/valid'
make_dir(train_dir)
make_dir(val_dir)


csv_data = U.load_csv('data/train/training_variants', delimiter=",")
headers = csv_data[0]
data = csv_data[1:]

training_text = U.load_csv('data/train/training_text')
id_to_text_mapping = {}

for row in training_text[1:]:
    id_to_text_mapping[row[0]] = row[1]

rand = np.random.permutation(data)
train = rand[:2900]
valid = rand[2900:]

train_text = []
for row in train:
    id = row[0]
    text = id_to_text_mapping[id]
    train_text.append((id,text))

valid_text = []
for row in valid:
    id = row[0]
    text = id_to_text_mapping[id]
    valid_text.append((id,text))


print(np.asarray(train_text).shape)
print(np.asarray(train).shape)
write_csv('data/train/train/training_text.csv', train_text, ["ID", "Text"])
write_csv('data/train/train/training_variants.csv', train, ['ID', 'Gene', 'Variation', 'Class'])

write_csv('data/train/valid/valid_text.csv', valid_text, ["ID", "Text"])
write_csv('data/train/valid/valid_variants.csv', valid, ['ID', 'Gene', 'Variation', 'Class'])
