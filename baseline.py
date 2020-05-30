import os
import csv
import time
import argparse


from tqdm import tqdm
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer


def load_csv(split):
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', default='data_dir')
    args = parser.parse_args()

    train_csv = load_csv('train')
    train_labels = list(zip(*train_csv))[0]
    train_labels = list(map(int, train_labels))
    dev_csv = load_csv('dev')
    dev_labels = list(zip(*dev_csv))[0]
    dev_labels = list(map(int, dev_labels))

    train_data = load_data('train', train_csv)
    dev_data = load_data('dev', dev_csv)

    vectorizer = TfidfVectorizer(max_features=10000, sublinear_tf=True)
    train_features = vectorizer.fit_transform(train_data).toarray()
    dev_features = vectorizer.transform(dev_data).toarray()

    knn_classifier = KNeighborsClassifier(n_neighbors=25, n_jobs=6)
    knn_classifier.fit(train_features, train_labels)

    print('Predicting...')
    pred = list()
    for dev_feature in tqdm(dev_features):
        pred.extend(knn_classifier.predict([dev_feature]))
    print('Accuracy: {}'.format(accuracy_score(dev_labels, pred)))
