import pandas as pd
import seaborn as sns
from sklearn import datasets

# Load the iris dataset
iris_data = datasets.load_iris()
iris = pd.DataFrame(iris_data['data'], columns=iris_data['feature_names'])
species = pd.DataFrame(iris_data['target'], columns=['species_num'])

# Species is a number {0,1,2}. Set as a name and save to the iris DataFrame
def test_iris(x):
    if x==0: return "setosa"
    if x==1: return "versicolor"
    if x==2: return "virginica"

iris['species'] = species['species_num'].apply(lambda x: test_iris(x))

# Plot the data to get a feel for the data
sns.pairplot(iris, hue='species')

# Create the training and testing datasets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris.drop(['species'], axis=1),iris['species'], random_state=101, test_size=0.3)

# Create the model
from sklearn.svm import SVC
model = SVC()
model.fit(X_train,y_train)
y_predict = model.predict(X_test)

# How did the model do?
from sklearn.metrics import confusion_matrix,classification_report
print(confusion_matrix(y_test,y_predict))

print(classification_report(y_test,y_predict))

# Use GridSearch to find the best SVM parameters for our model
from sklearn.model_selection import GridSearchCV
param_grid = {'C': [0.1,1,10,100,1000], 'gamma':[1,0.1,0.01,0.001]}
grid = GridSearchCV(SVC(),param_grid,refit=True)
grid.fit(X_train,y_train)

# Use the best parameters from GridSearch to make our model run
y_grid = grid.predict(X_test)

# How did the refined model do?
print(confusion_matrix(y_test,y_grid))

print(classification_report(y_test,y_grid))