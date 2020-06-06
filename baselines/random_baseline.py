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
    dev_labels, dev_ids = zip(*dev_csv)
    dev_labels = list(map(int, dev_labels))
    dev_ids = list(map(int, dev_ids))

    pred = [random.randint(0, 999) for _ in range(len(dev_labels))]

    print('Accuracy: {}'.format(accuracy_score(dev_labels, pred)))

    with open('baselines_predictions/random_baseline.csv', 'w') as fp:
    	writer = csv.writer(fp)
    	writer.writerow(['uid', 'pid'])

    	for p, i in zip(pred, dev_ids):
    		writer.writerow([p, i])
