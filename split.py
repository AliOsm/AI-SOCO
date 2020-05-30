import os
import csv
import shutil
import random
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--files_dir', default='crawl_dir/dataset_sun_may_24_15_39_27_2020')
    parser.add_argument('--data_dir', default='data_dir')
    args = parser.parse_args()

    os.mkdir(os.path.join(args.data_dir, 'train'))
    os.mkdir(os.path.join(args.data_dir, 'dev'))
    os.mkdir(os.path.join(args.data_dir, 'test'))

    with open(os.path.join(args.files_dir, 'info.csv'), 'r') as fp:
        reader = csv.reader(fp)
        problems = list(reader)
    problems = problems[1:]

    users = list(set(problem[0] for problem in problems))
    random.shuffle(users)

    submissions = list(set(problem[0] + problem[1] for problem in problems))
    random.shuffle(submissions)
    submissions = { submission:i for i, submission in enumerate(submissions) }

    for i in range(len(problems)):
        problems[i].append(users.index(problems[i][0]))
        problems[i].append(submissions[problems[i][0] + problems[i][1]])

    train_problems = list()
    dev_problems = list()
    test_problems = list()

    for i in range(0, len(problems), 100):
        current_user_problems = problems[i:i + 100]
        random.shuffle(current_user_problems)
        train_problems.extend(current_user_problems[:50])
        dev_problems.extend(current_user_problems[50:75])
        test_problems.extend(current_user_problems[75:])

    for split, split_problems in zip(['train', 'dev', 'test'], [train_problems, dev_problems, test_problems]):
        with open(os.path.join(args.data_dir, '{}.csv'.format(split)), 'w') as fp:
            writer = csv.writer(fp)
            writer.writerow(['uid', 'pid'])

            for split_problem in split_problems:
                writer.writerow([split_problem[-2], split_problem[-1]])
                shutil.copy(split_problem[-6], os.path.join(args.data_dir, split, str(split_problem[-1])))
