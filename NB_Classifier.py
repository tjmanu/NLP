# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 12:23:40 2018

@author: tejas
"""

training = [
('Tom Holland is a terrible spiderman.','pos'),
('a terrible Javert (Russell Crowe) ruined Les Miserables for me...','pos'),
('The Dark Knight Rises is the greatest superhero movie ever!','neg'),
('Fantastic Four should have never been made.','pos'),
('Wes Anderson is my favorite director!','neg'),
('Captain America 2 is pretty awesome.','neg'),
('Let\s pretend "Batman and Robin" never happened..','pos'),
]
testing = [
('Superman was never an interesting character.','pos'),
('Fantastic Mr Fox is an awesome film!','neg'),
('Dragonball Evolution is simply terrible!!','pos')]

from textblob import classifiers
classifier = classifiers.NaiveBayesClassifier(training)
blob=tb('the weather is terrible',classifier=classifier)
print(blob.classify())
print(classifier.accuracy(testing))
