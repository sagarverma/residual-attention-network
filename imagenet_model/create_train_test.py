from random import shuffle
from os import listdir, path
import json
import sys 
import csv

class_map= {'bags':0,'belts':1,'dresses':2,'eyewear':3,'footwear':4,
    'hats':5,'leggings':6,'outerwear':7,'pants':8,'skirts':9,'tops':10}


shuffle_data = True
dataset_path = '../../../datasets/street2shop/'

meta_path = dataset_path + 'meta/json/'
images_path = dataset_path + '/images/'

meta_files = listdir(meta_path)

train_images = []
train_labels = []

for filename in meta_files:
    if 'train' in filename:
        fin = open(meta_path + filename, 'r')
        train_data = json.loads(fin.read())
        fin.close()

        for dat in train_data:
            if path.exists(images_path + str(dat['photo']) + '.jpg'):
                train_images.append(dat['photo'])
                train_labels.append(class_map[filename[12:-5]])

            if path.exists(images_path + str(dat['product']) + '.jpg'):
                train_images.append(dat['product'])
                train_labels.append(class_map[filename[12:-5]])

if shuffle_data:
    c = list(zip(train_images, train_labels))
    shuffle(c)
    train_images, train_labels =zip(*c)

test_images = []
test_labels = []

for filename in meta_files:
    if 'test' in filename:
        fin = open(meta_path + filename, 'r')
        test_data = json.loads(fin.read())
        fin.close()

        for dat in test_data:
            if path.exists(images_path + str(dat['photo']) + '.jpg'):
                test_images.append(dat['photo'])
                test_labels.append(class_map[filename[11:-5]])

            if path.exists(images_path + str(dat['product']) + '.jpg'):
                test_images.append(dat['product'])
                test_labels.append(class_map[filename[11:-5]])

print len(train_images), len(test_images)


w_train = csv.writer(open('street2shop_train.csv','w'), delimiter=' ')

for i in range(len(train_images)):
    w_train.writerow([train_images[i],train_labels[i]])


w_test = csv.writer(open('street2shop_test.csv','w'), delimiter=' ')

for i in range(len(test_images)):
    w_test.writerow([test_images[i],test_labels[i]])