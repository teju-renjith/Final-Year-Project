# -*- coding: utf-8 -*-
"""FYP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vF0hN9w3HZ8bVLcMowwYlgBiNpnk4Q0y
"""

import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

# DECISION TREE CLASSIFIER

your_dataset = pd.read_csv('Annex A - Dataset with 50 chosen features.csv')

filtered_dataset = your_dataset[your_dataset['family'] != 'L']
X = filtered_dataset.drop('family', axis=1)
y = filtered_dataset['family']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
# print(classification_report(y_test, y_pred))

# RANDOM FOREST

your_dataset = pd.read_csv('Annex A - Dataset with 50 chosen features.csv')

X = filtered_dataset.drop('family', axis=1)
y = filtered_dataset['family']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)
y_pred = rf_classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
# print(classification_report(y_test, y_pred))

# GRADIENT BOOSTING

your_dataset = pd.read_csv('Annex A - Dataset with 50 chosen features.csv')

X = filtered_dataset.drop('family', axis=1)
y = filtered_dataset['family']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

gb_classifier = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
gb_classifier.fit(X_train, y_train)
y_pred = gb_classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
# print(classification_report(y_test, y_pred))

# LOGISTIC REGRESSION

your_dataset = pd.read_csv('Annex A - Dataset with 50 chosen features.csv')

filtered_dataset = your_dataset[your_dataset['family'] != 'L']
X = filtered_dataset.drop('family', axis=1)
y = filtered_dataset['family']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train, y_train)
y_pred = log_reg.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
# print(classification_report(y_test, y_pred))


# NAIVE BAYES

your_dataset = pd.read_csv('Annex A - Dataset with 50 chosen features.csv')

filtered_dataset = your_dataset[your_dataset['family'] != 'L']
X = filtered_dataset.drop('family', axis=1)
y = filtered_dataset['family']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

naive_bayes = GaussianNB()
naive_bayes.fit(X_train, y_train)
y_pred = naive_bayes.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
# print(classification_report(y_test, y_pred))


# NEW FEATURE TESTING

# new_input = [[0,0,0,0,0,0,0,0,0,1,0,8,8,0,0,0,0,1,6,1,1,6,6,20,19,0,18,2,35,28,0,3,3,3,3,0,3,0,11,5,0,0,0,0,0,0,38,0,1,4073]]
original_feature_names = [
    'proc_pid', 'file', 'urls', 'type', 'name', 'ext_urls', 'path', 'program', 'info',
    'positives', 'families', 'description', 'sign_name', 'sign_stacktrace', 'arguments', 'api',
    'category', 'imported_dll_count', 'dll', 'pe_res_name', 'filetype', 'pe_sec_name', 'entropy',
    'hosts', 'requests', 'mitm', 'domains', 'dns_servers', 'tcp', 'udp', 'dead_hosts', 'proc',
    'beh_command_line', 'process_path', 'tree_command_line', 'children', 'tree_process_name',
    'command_line', 'regkey_read', 'directory_enumerated', 'regkey_opened', 'file_created',
    'wmi_query', 'dll_loaded', 'regkey_written', 'file_read', 'apistats', 'errors', 'action', 'log'
]

test = pd.read_csv('Test.csv')
test_row = test.loc[0, original_feature_names].values
test_data = []
test_data.append(test_row)
new_input_df = pd.DataFrame(data=test_data, columns=original_feature_names)

prediction = clf.predict(new_input_df)
print(f"Decision Tree predicts: {prediction[0]}")

prediction = rf_classifier.predict(new_input_df)
print(f"Random forest predicts: {prediction[0]}")

prediction = gb_classifier.predict(new_input_df)
print(f"Gradient booster predicts: {prediction[0]}")

prediction = log_reg.predict(new_input_df)
print(f"Logistic Regression predicts: {prediction[0]}")

prediction = naive_bayes.predict(new_input_df)
print(f"Naive Bayes predicts: {prediction[0]}")
