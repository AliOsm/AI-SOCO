import csv
import argparse


from sklearn.metrics import accuracy_score


def load_labels(file_path):
	with open(file_path, 'r') as fp:
		reader = csv.reader(fp)
		labels = list(reader)

	assert(labels[0][0] == 'uid')
	assert(labels[0][1] == 'pid')

	labels = labels[1:]
	for i in range(len(labels)):
		labels[i][0] = int(labels[i][0])
		labels[i][1] = int(labels[i][1])
	return labels


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gold_file')
    parser.add_argument('--pred_file')
    args = parser.parse_args()

    gold = load_labels(args.gold_file)
    pred = load_labels(args.pred_file)

    assert(len(gold) == len(pred))

    gold = sorted(gold, key=lambda elem: elem[1])
    pred = sorted(pred, key=lambda elem: elem[1])

    gold = [elem[0] for elem in gold]
    pred = [elem[0] for elem in pred]

    print('Accuracy: {}'.format(accuracy_score(gold, pred)))
