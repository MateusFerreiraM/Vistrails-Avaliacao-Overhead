import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
import time

def main():
    print("Loading Iris dataset...")
    iris = load_iris()
    X, y = iris.data, iris.target

    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    print("Building pipeline...")
    # Pipeline with StandardScaler and SVC
    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('svc', SVC())
    ])

    print("Setting up GridSearchCV...")
    # Parameters for the grid search
    parameters = {
        'svc__C': 10. ** np.arange(-3, 3),
        'svc__gamma': 10. ** np.arange(-3, 3)
    }

    grid = GridSearchCV(pipe, parameters, cv=5)

    print("Training GridSearchCV...")
    start_time = time.time()
    grid.fit(X_train, y_train)
    end_time = time.time()

    print(f"Training completed in {end_time - start_time:.4f} seconds")
    
    score = grid.score(X_test, y_test)
    print(f"Best parameters: {grid.best_params_}")
    print(f"Test Score: {score:.4f}")

if __name__ == '__main__':
    main()
