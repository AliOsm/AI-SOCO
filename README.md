# AI-SOCO
Official [FIRE 2020](http://fire.irsi.res.in/fire/2018/home) **A**uthorship **I**dentification of **SO**urce **CO**de (AI-SOCO) task repository containing dataset, evaluation tools and baselines.

10 - 13 December, Institute for Development and Research in Banking Technology, Hyderabad

Welcome to pariticipate on our Codalab competition [here](https://competitions.codalab.org/competitions/25135)!

All participants are welcome to open new [issue](https://github.com/AliOsm/AI-SOCO/issues/new) about dataset issues!

## Introduction
General authorship identification is essential to the detection of undesirable deception of others' content misuse or exposing the owners of some anonymous hurtful content. This is done by revealing the author of that content. **A**uthorship **I**dentification of **SO**urce **CO**de (AI-SOCO) focuses on uncovering the author who wrote some piece of code. This facilitates solving issues related to cheating in academic, work and open source environments. Also, it can be helpful in detecting the authors of malware softwares over the world.

The detection of cheating in academic communities is significant to properly address the contribution of each researcher. Also, in work environments, credit sometimes goes to people that did not deserve it. Such issues of plagiarism could arise in open source projects that are available on public platforms. Similarly, this could be used in public or private online coding contests whether done in coding interviews or in official coding training contests to detect the cheating of applicants or contestants. A system like this could also play a big role in detecting the source of anonymous malicious softwares.

The dataset is composed of source codes collected from the open submissions in the [Codeforces](http://codeforces.com/) online judge. Codeforces is an online judge for hosting competitive programming contests such that each contest consists of multiple problems to be solved by the participants. A Codeforces participant can solve a problem by writing a solution for it using any of the available programming languages on the website, and then submitting the solution through the website. The solution's result can be correct (accepted) or incorrect (wrong answer, time limit exceeded, etc.).

In our dataset, we selected 1,000 users and collected 100 source codes from each one. So, the total number of source codes is 100,000. All collected source codes are correct, bug-free, compile-ready and written using the C++ programming language using different versions. For each user, all collected source codes are from unique problems.

Given the pre-defined set of source codes and their writers, the task is to build a system that is able to detect the writer given any new, unseen before source codes from the previously defined writers list.

### Example
Given the following bug-free and ready to compile C++ source code:

```c++
#include <string>
#include <iostream>
#include <ctype.h>
using namespace std;
 
int main() {
    string s;
    cin >> s;
    s[0] = toupper(s[0]);
    cout << s << endl;
    return 0;
}
```

You need to build a system that can determine the source code writer from list consists of 1,000 writers.

## Dataset Structure
In `data_dir` directory there are the following:
- `train.csv` file which contains 50K pairs of `uid`s (User IDs) and `pid`s (Problem IDs). Each `uid` appears 50 times in the file with 50 different `pid`s.
- `train` directory which contains 50K files, each file with different `pid` represents the C++ source code that will be the input to your system.
- `dev.csv` file is similar to `train.csv`, but it will be used to evaluation your system while developing, so it is not allowed to use it in the training phase.
- `dev` directory is similar to `train`, but it will be used to evaluation your system while developing, so it is not allowed to use it in the training phase.

## Baseline
- [**Random Baseline**](random_baseline.py) is simply predicting a random writer for each piece of code from the list of 1,000 writers (from 0 to 999). Its accuracy reaches around **0.1%**.
- [**TF-IDF KNN Baseline**](tfidf_knn_baseline.py) vectorizes the source codes using [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) method with **10K** features and builds a [KNN](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) classifier with **25** neighbors on top of that representations extracted from TF-IDF. Its accuracy on the development set is **62.128%** which is much better than the random baseline. Keep in mind that this baseline is very slow and it will take you about **4** hours to predict all examples in the development set using **6** threads.

## Evaluation
Systems will be evaluated and ranked based on **Accuracy** metric. An evaluation [script](scorer.py) is available on the Github repository.

## Deadlines
- 15th June - open track websites
- 30th June – training and development data release
- 31st July – test data release
- 7th September – run submission deadline
- 20th September – results declared
- 31st October – Working notes and overview papers due (tentative)
- 10th-13th December - FIRE 2020 (One additional day likely)

## License
The dataset is distributed under the [MIT](/LICENSE) license.
