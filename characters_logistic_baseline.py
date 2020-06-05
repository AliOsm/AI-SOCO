import os
import csv
import argparse
import numpy as np


from string import printable
printable = { char:idx for idx, char in enumerate(printable) }
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression


def load_labels(split):
    with open(os.path.join(args.data_dir, '{}.csv'.format(split)), 'r') as fp:
        reader = csv.reader(fp)
        problems = list(reader)
    problems = problems[1:]
    return problems


def load_data(split, split_csv):
    problems = list()
    for row in split_csv:
        with open(os.path.join(args.data_dir, split, row[1]), 'r') as fp:
            problems.append(fp.read())
    return problems


def vectorize_data(data):
    vec_data = list()
    for d in data:
        vec = [0] * len(printable)
        for char in d:
            if char in printable:
                vec[printable[char]] += 1
        vec_data.append(vec)
    return vec_data


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', default='data_dir')
    args = parser.parse_args()

    train_csv = load_labels('train')
    train_labels = list(zip(*train_csv))[0]
    train_labels = list(map(int, train_labels))
    dev_csv = load_labels('dev')
    dev_labels = list(zip(*dev_csv))[0]
    dev_labels = list(map(int, dev_labels))

    train_data = load_data('train', train_csv)
    dev_data = load_data('dev', dev_csv)

    train_data = vectorize_data(train_data)
    dev_data = vectorize_data(dev_data)

    logistic_classifier = LogisticRegression(max_iter=100, verbose=1, n_jobs=6)
    logistic_classifier.fit(train_data, train_labels)

    pred = logistic_classifier.predict(dev_data)

    print('Accuracy: {}'.format(accuracy_score(dev_labels, pred)))
