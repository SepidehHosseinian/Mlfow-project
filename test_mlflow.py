import mlflow
import sklearn
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Load data
X, y = load_iris(return_X_y=True)

# Start a new MLflow run
with mlflow.start_run():

# Train a model
    model= LogisticRegression()
model.fit(X, y)

# Log parameters
mlflow.log_param("solver", model.solver)
mlflow.log_param("penalty", model.penalty)

# Log metrics
accuracy = model.score(X, y)
mlflow.log_metric("accuracy", accuracy)

# Log artifacts
mlflow.sklearn.log_model(model, "model")