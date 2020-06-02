import os
import csv
import random
import argparse


from sklearn.metrics import accuracy_score


def load_labels(split):
    with open(os.path.join(args.data_dir, '{}.csv'.format(split)), 'r') as fp:
        reader = csv.reader(fp)
        problems = list(reader)
    problems = problems[1:]
    return problems


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', default='data_dir')
    args = parser.parse_args()

    dev_csv = load_labels('dev')
    dev_labels = list(zip(*dev_csv))[0]
    dev_labels = list(map(int, dev_labels))

    pred = [random.randint(0, 999) for _ in range(len(dev_labels))]

    print('Accuracy: {}'.format(accuracy_score(dev_labels, pred)))
