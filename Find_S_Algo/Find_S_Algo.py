'''
This program is machine learning FindS concept learning algoritham

Goal : Induced a general function from specific tranning example

Given: A (large) set of training data of examples labeled as being members or non-members of a concept
Compute: A general function that fits the training data well and generalizes well to unseen/future data

Given:
Instances X: Possible days, each described by
	Sky, AirTemp, Humidity, Wind, Water, Forecast

Target function c: EnjoySport : X → {0, 1}
Hypotheses H: Conjunctions of literals.
	E.g. ⟨?, Cold, High, ?, ?, ?⟩.
Training examples D: Positive and negative examples of the target function
⟨x1, c(x1)⟩, . . . ⟨xm, c(xm)⟩
Determine: A hypothesis h in H such that h(x) = c(x) for all x in D.

'''
import csv;

def readFile(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        _list = list(reader)
        del _list[0];

    return _list;

def hypotheses(list):
    Hypotheses = [];
    for item in list:
        if(item[len(item)-1] == 'Yes'):
            if not Hypotheses:
                Hypotheses=item;

            for i in range(len(item)-1):
                if(Hypotheses[i]!=item[i]):
                    Hypotheses[i]='?';

    print(Hypotheses[0:len(item)-1]);

def main():
    trainning_data = readFile('file.csv');
    hypotheses(trainning_data);

if __name__ == "__main__":
    main();