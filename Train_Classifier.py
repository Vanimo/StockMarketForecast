'''
Created on 17 May 2013

@author: Floris
'''
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import KFold, cross_val_score

def main():
    pipelinedNB()

def pipelinedNB():
    text_clf = Pipeline([('vect', CountVectorizer()),
                         ('tfidf', TfidfTransformer()),
                         ('clf', MultinomialNB())])
    data, target = getData()
    kf = KFold(len(data), n_folds=10)
    print np.average(cross_val_score(text_clf, data, target, cv=kf))
    
def getData():
    from Methods.IO import readData
    readData = readData("data/ClassifiedIBM.txt")
    data = []
    target = []
    for line in readData:
        target.append(int(line[0]))
        data.append(line[1])
    target = np.array(target)
    return data, target

if __name__ == '__main__':
    main()