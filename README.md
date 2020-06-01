# AI-SOCO
Official FIRE2020 AI-SOCO task repository containing dataset, evaluation tools and baselines.

## Introduction
General authorship identification is essential to the detection of undesirable deception of others’ content misuse or exposing the owners of some anonymous hurtful content. This is done by revealing the author of that content. **A**uthorship **I**dentification of **SO**urce **CO**de (AI-SOCO) focuses on uncovering the author who wrote some piece of code. This facilitates solving issues related to cheating in academic, work and open source environments. Also, it can be helpful in detecting the authors of malware softwares over the world.

Full task description can be found [here](https://docs.google.com/presentation/d/1b74NkU3EXsve5g3henE2taaw1MTm5V8nF-Gt73sma78/edit?usp=sharing).

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
In `baseline.py` you can find our baseline model which achieved **62.128%** accuracy on the development dataset.
We vectorize the source codes using TF-IDF and build a KNN classifier on top of the representations.

## Evaluation
The task will be evaluated using **Accuracy** metric as the dataset is balanced.

## Deadlines
- 15th June - open track websites
- 30th June – training data release
- 31st July – test data release
- 7th September – run submission deadline
- 20th September – results declared
- 31st October – Working notes and overview papers due (tentative)
- 10th-13th December - FIRE 2020 (One additional day likely)

## License
The dataset is distributed under the [MIT](/LICENSE) license.
