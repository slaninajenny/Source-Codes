
from pandas import read_csv
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier

df = read_csv("C://Users//Stefan Schönig//Desktop//Data Analysis II//Übung//FeatureSelection//train.csv")
X = df.iloc[:,0:20]  #independent columns
y = df.iloc[:,-1]    #target column i.e price range

clf = RandomForestClassifier(n_estimators=30, max_depth=None, min_samples_split=2, random_state=0)
scores = cross_val_score(clf, X, y, cv=10)
scores.mean()

print(scores.max())