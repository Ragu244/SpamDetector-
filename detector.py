import pickle as c
import os
import sys
import numpy as np
import io
from sklearn import *
from collections import Counter


def load(clf_file):
    with open(clf_file,'rb') as fp:
        clf = c.load(fp)
    return clf
    
def make_dict():
    direc = "C:/Users/Ragu/Desktop/sd/emails/"
    files = os.listdir(direc)
    emails = [direc + email for email in files]
    words = []
    c = len(emails)

    for email in emails:
        f = io.open(email,errors="ignore")
        blob = f.read()
        words += blob.split(" ")
        print(c)
        c -= 1

    for i in range(len(words)):
        if not words[i].isalpha():
            words[i] = ""

    dictionary = Counter(words)
    del dictionary[""]
    return dictionary.most_common(3000)


clf = load("text-classifier.mdl")
d = make_dict()

from six.moves import input as raw_input

while True:
    features = []
    inp = raw_input(">").split()
    if inp[0] == "exit":
        break
    for word in d:
        features.append(inp.count(word[0]))
    res = clf.predict([features])
    print(["Not Spam", "Spam!"][res[0]])
