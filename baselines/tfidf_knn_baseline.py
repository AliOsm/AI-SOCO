import os
import csv
import argparse


from tqdm import tqdm
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer


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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', default='data_dir')
    args = parser.parse_args()

    train_csv = load_labels('train')
    train_labels, train_ids = zip(*train_csv)
    train_labels = list(map(int, train_labels))
    train_ids = list(map(int, train_ids))
    dev_csv = load_labels('dev')
    dev_labels, dev_ids = zip(*dev_csv)
    dev_labels = list(map(int, dev_labels))
    dev_ids = list(map(int, dev_ids))

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

    with open('baselines_predictions/tfidf_knn_baseline.csv', 'w') as fp:
        writer = csv.writer(fp)
        writer.writerow(['uid', 'pid'])

        for p, i in zip(pred, dev_ids):
            writer.writerow([p, i])
