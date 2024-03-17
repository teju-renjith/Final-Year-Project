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

from sklearn.metrics import accuracy_score, classification_report


# DECISION TREE CLASSIFIER

your_dataset = pd.read_csv('Annex A - Dataset with 50 chosen features.csv')

filtered_dataset = your_dataset[your_dataset['family'] != 'L']
X = filtered_dataset.drop('family', axis=1)
y = filtered_dataset['family']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

class_weights = {'G': 1, 'E': 6}
clf = DecisionTreeClassifier(class_weight=class_weights)
clf.fit(X_train, y_train)

# clf = DecisionTreeClassifier()
# clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(classification_report(y_test, y_pred))


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
print(f"The model predicts: {prediction[0]}")


