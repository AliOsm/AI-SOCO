import os
import csv
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--files_dir', default='crawl_dir/dataset_sun_may_24_15_39_27_2020')
    args = parser.parse_args()

    solutions_per_country = dict()
    unique_problems = set()
    solutions_per_problem = dict()
    solutions_per_index = dict()

    with open(os.path.join(args.files_dir, 'info.csv'), 'r') as fp:
        reader = csv.reader(fp)
        next(reader)
        for row in reader:
            if row[-3] in solutions_per_country:
                solutions_per_country[row[-3]] += 1
            else:
                solutions_per_country[row[-3]] = 1
            unique_problems.add(row[2] + row[4])
            if row[2] + row[4] in solutions_per_problem:
                solutions_per_problem[row[2] + row[4]] += 1
            else:
                solutions_per_problem[row[2] + row[4]] = 1
            if row[4] in solutions_per_index:
                solutions_per_index[row[4]] += 1
            else:
                solutions_per_index[row[4]] = 1

    users_count = 0
    solutions_count = 0
    whitespaces_count = 0
    tokens_count = 0
    unique_tokens = set()
    solutions_per_language = dict()

    for i in os.listdir(args.files_dir):
        if os.path.isdir(os.path.join(args.files_dir, i)):
            users_count += 1

            for j in os.listdir(os.path.join(args.files_dir, i, 'ok')):
                temp = len(os.listdir(os.path.join(args.files_dir, i, 'ok', j)))
                solutions_count += temp

                for k in os.listdir(os.path.join(args.files_dir, i, 'ok', j)):
                    with open(os.path.join(args.files_dir, i, 'ok', j, k), 'r') as fp:
                        content = fp.read()
                        for char in content:
                        	if char.isspace():
                        		whitespaces_count += 1
                        content = content.split()
                        tokens_count += len(content)
                        unique_tokens.update(content)

                if j in solutions_per_language:
                    solutions_per_language[j] += temp
                else:
                    solutions_per_language[j] = temp

    print('Users Count: {}'.format(users_count))
    print('Solutions Count: {}'.format(solutions_count))
    print('Tokens Count: {}'.format(tokens_count))
    print('Whitespaces Count: {}'.format(whitespaces_count))
    print('Unique Tokens: {}'.format(len(unique_tokens)))
    print('AVG. Solutions/User: {:.3f}'.format(solutions_count / users_count))
    print('AVG. Tokens/Solution: {:.3f}'.format(tokens_count / solutions_count))
    print('AVG. Whitespaces/Solution: {:.3f}'.format(whitespaces_count / solutions_count))
    print('Solutions/Language:')
    for language in sorted(solutions_per_language):
        print('\t{}:\t{}'.format(language, solutions_per_language[language]))

    print('Unique Countries: {}'.format(len(solutions_per_country)))
    print('AVG. Solutions/Country: {:.3f}'.format(sum([solutions_per_country[elem] for elem in solutions_per_country])/ len(solutions_per_country)))
    print('Unique Problems: {}'.format(len(unique_problems)))
    print('Maximum Solutions/Problem: {}'.format(max([solutions_per_problem[elem] for elem in solutions_per_problem])))
    print('Minimum Solutions/Problem: {}'.format(min([solutions_per_problem[elem] for elem in solutions_per_problem])))
    sorted_ = sorted([solutions_per_problem[elem] for elem in solutions_per_problem])
    print('AVG. Solutions/Problem: {:.3f}'.format(solutions_count / len(unique_problems)))
    print('Median Solutions/Problem: {}'.format(sorted_[int(len(sorted_) / 2)]))
    print('Solutions/Index:')
    for index in sorted(solutions_per_index):
        print('\t{}:\t{}'.format(index, solutions_per_index[index]))
