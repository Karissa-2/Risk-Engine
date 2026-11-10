# Imports breakdown

File: log_regression.ipynb

| Import | Purpose |
|---- |-------|
| ColumnTransformer | Applies different preprocessing methods to different columns. |
| StandardScaler | Standardizes numerical data so features have comparable scales. |
| OneHotEncoder | Converts categorical values into numerical representations. |
| FunctionTransformer | Applies a custom function to the data. |
| Pipeline | Combines multiple preprocessing steps and runs them in sequence. |


## Graphs
| Graph | Purpose |
|---- |-------|
| Confusion Matrix | A tabular summary used to evaluate the performance of a classification model by comparing its predicted class labels against the actual ground truth label. It explicitly shows where a model gets confused, distinguishing between harmless mistakes and critical failures. |
| Receiver Operating Characteristic (ROC) Curve| A graph that shows the performance of a binary classification model across all possible classification thresholds. |
| Precision-Recall (PR) Curve | A graphical plot that evaluates the performance of a binary classification model by showing the trade-off between precision and recall across every possible classification threshold. When you specifically want to study the trade-off between precision (how many predicted attacks are real) and recall (how many real attacks are caught).|

## Interpreting the Graphs for Attack Prediction

Assuming the labels are **0 = normal traffic** and **1 = attack**, both graphs show how well the model identifies attacks.

### Confusion Matrix

The confusion matrix compares each test example's actual label with the model's prediction:

|  | Predicted normal | Predicted attack |
|---|---|---|
| **Actually normal** | Correctly cleared traffic | **False alarm**: normal traffic flagged as an attack |
| **Actually an attack** | **Missed attack**: attack classified as normal | **Detected attack** |

It shows the counts for each outcome. Missed attacks and false alarms are different kinds of errors, and which matters more depends on the use case.

### ROC Curve

The ROC curve shows how the model's results change as its decision threshold varies:

- **Y-axis — true-positive rate:** the proportion of actual attacks caught.
- **X-axis — false-positive rate:** the proportion of normal traffic mistakenly flagged as attacks.

Lowering the threshold to catch more attacks can also increase false alarms. A curve closer to the upper-left corner generally indicates better separation between attacks and normal traffic; the diagonal represents roughly random performance.
