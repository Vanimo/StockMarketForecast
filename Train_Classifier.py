'''
Created on 17 May 2013

@author: Floris
'''
import numpy as np
from Methods import CustomFeatures
from scipy.sparse import hstack

from sklearn import svm, cross_validation
from sklearn import preprocessing
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import KFold, cross_val_score


def main():
    #pipelinedNB()
    extendedTraining()

def extendedTraining():
    data, target = getData()
    
    # As seen in Lab6, goal detection
    vect = CountVectorizer(min_df=1)
    tweets_vector = vect.fit_transform(data)
    tf_transformer = TfidfTransformer(use_idf=False).fit(tweets_vector)
    tweets_vector_tf = tf_transformer.transform(tweets_vector)
    
    # Custom features
    emotions = CustomFeatures.getEmotions()
    custom_features = np.zeros((tweets_vector_tf.shape[0],1))
    index = 0
    for index in range(len(data)):
        custom_features[index, 0] = CustomFeatures.getTweetEmotion_3states(data[index], emotions)
    
    # No longer need original data
    data = []
    
    tweets_matrix = hstack([tweets_vector_tf, custom_features])
    print tweets_vector_tf.shape
    print tweets_matrix.shape
    
    min_max_scaler = preprocessing.MinMaxScaler()
    
    tweets_matrix = min_max_scaler.fit_transform(tweets_matrix.toarray())
    svmCost = 5
    svmGamma = 0.1
    clf = svm.SVC(C=svmCost, gamma=svmGamma)
    #clf.fit(tweets_matrix, target)
    print np.mean(cross_validation.cross_val_score(clf, tweets_matrix, target, cv=5))
    
# This one has the .toarray error
# def extendedTraining():
#     data, target = getData()
#     
#     # As seen in Lab6, goal detection
#     vect = CountVectorizer(min_df=1)
#     tweets_vector = vect.fit_transform(data)
#     tf_transformer = TfidfTransformer(use_idf=False).fit(tweets_vector)
#     tweets_vector_tf = tf_transformer.transform(tweets_vector)
#     
#     custom_features = CustomFeatures.getTweetEmotion_3states(data)
#     
#     tweets_matrix = np.hstack([tweets_vector_tf, custom_features])
#     
#     min_max_scaler = preprocessing.MinMaxScaler()
#     tweets_matrix = min_max_scaler.fit_transform(tweets_matrix.toarray())
#     svmCost = 5
#     svmGamma = 0.1
#     clf = svm.SVC(C=svmCost, gamma=svmGamma)
#     #clf.fit(tweets_matrix, target)
#     print np.mean(cross_validation.cross_val_score(clf, tweets_matrix, target, cv=5))

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
        data.append(line[1].lower())
    target = np.array(target)
    return data, target

if __name__ == '__main__':
    main()