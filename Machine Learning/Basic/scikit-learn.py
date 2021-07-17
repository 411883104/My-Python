from sklearn.datasets import load_boston
boston=load_boston()
X=boston.data
Y=boston.target

print(X.shape)
print(Y.shape)