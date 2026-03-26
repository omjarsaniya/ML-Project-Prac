# End To End ML Project

import dagshub
dagshub.init(repo_owner='ombjarsaniya123', repo_name='ML-Project-Prac.', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)
  
  REMOVED
  REMOVED

export MLFLOW_TRACKING_USERNAME='ombjarsaniya123'
export MLFLOW_TRACKING_PASSWORD='REMOVED'
