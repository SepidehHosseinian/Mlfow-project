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

import mlflow
from pyspark.sql.functions import struct, col
logged_model = 'runs:/3bff5968bae1448c8c92fa0745d61163/model'

# Load model as a Spark UDF. Override result_type if the model does not return double values.
loaded_model = mlflow.pyfunc.spark_udf(spark, model_uri=logged_model, result_type='double')

# Predict on a Spark DataFrame.
df.withColumn('predictions', loaded_model(struct(*map(col, df.columns))))