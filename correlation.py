from pandas import read_csv

import seaborn as sns
import matplotlib.pyplot as plt

data = read_csv("C://Users//Stefan Schönig//Desktop//Data Analysis II//Übung//FeatureSelection//train.csv")
X = data.iloc[:,0:20]  #independent columns
y = data.iloc[:,-1]    #target column i.e price range

#get correlations of each features in dataset
corrmat = data.corr("pearson")
corrmat2 = data.corr("spearman")

top_corr_features = corrmat.index
top_corr_features2 = corrmat2.index
plt.figure(figsize=(20,20))

#plot heat map
sns.heatmap(data[top_corr_features].corr("pearson"),annot=True,cmap="coolwarm")
plt.figure(figsize=(20,20))
sns.heatmap(data[top_corr_features2].corr("spearman"),annot=True,cmap="RdYlGn")
plt.show()