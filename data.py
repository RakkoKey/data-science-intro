from sklearn import tree


X = [[181,80,44], [177, 70, 43], [160,60,38], [154,54,37], [200, 70, 32], [190,90,47], [175,64,39], [170, 70, 30]]

Y = ['male', 'female', 'female', 'male', 'male', 'male', 'female', 'female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict([[177,70,30]])

print(prediction)