import pandas as pd
import numpy as np
import math
from collections import defaultdict
# Reproducibility of LLM-based Recommender Systems: The Case Study of P5 Paradigm

data_Top_sequential = pd.read_csv("LLMs - List_of_considered_variables.csv")
data_Top_sequential = data_Top_sequential.iloc[1:].reset_index(drop=True)
data_Top_sequential = data_Top_sequential.reset_index(drop=True)
data_Top_sequential = data_Top_sequential.drop(data_Top_sequential.columns[0], axis=1)
data_Top_sequential = data_Top_sequential.drop(data_Top_sequential.columns[1], axis=1)

data_Top_sequential = data_Top_sequential.transpose()
data_Top_sequential.columns = data_Top_sequential.iloc[0]
data_Top_sequential = data_Top_sequential.iloc[1:].reset_index(drop=True)



print("####### Was the hyperparameter optimization procedure described for proposed model? ###############")
proposed_model_opt_procedure  = data_Top_sequential["Proposed model opt. procedure"]
proposed_model_opt_procedure_dict = defaultdict(int)

for value in proposed_model_opt_procedure:
    if not pd.isna(value):
        proposed_model_opt_procedure_dict[value.strip()] +=1
    else:
        proposed_model_opt_procedure_dict["NA"] +=1
        
for key, value in proposed_model_opt_procedure_dict.items():
    print(f"{key}:  {value}")


print("####### Was the hyperparameter optimization procedure described for baseline model? ###############")
baseline_model_opt_procedure  = data_Top_sequential["Baseline model opt. procedure"]
baseline_model_opt_procedure_dict = defaultdict(int)

for value in baseline_model_opt_procedure:
    if not pd.isna(value):
        baseline_model_opt_procedure_dict[value.strip()] +=1
    else:
        baseline_model_opt_procedure_dict["NA"] +=1
        
for key, value in baseline_model_opt_procedure_dict.items():
    print(f"{key}:  {value}")


print("####### Were the searched ranges for the hyperparameters reported for proposed model? ###############")
proposed_hyperparameter_ranges  = data_Top_sequential["Proposed model hyperparameter ranges"]
proposed_hyperparameter_ranges_dict = defaultdict(int)

for value in proposed_hyperparameter_ranges:
    if not pd.isna(value):
        proposed_hyperparameter_ranges_dict[value.strip()] +=1
    else:
        proposed_hyperparameter_ranges_dict["NA"] +=1
        
for key, value in proposed_hyperparameter_ranges_dict.items():
    print(f"{key}:  {value}")


print("############################################ Were the searched ranges for the hyperparameters reported for baseline model? ###############")
baseline_hyperparameter_ranges  = data_Top_sequential["Baseline model hyperparameter ranges"]
baseline_hyperparameter_ranges_dict = defaultdict(int)

for value in baseline_hyperparameter_ranges:
    if not pd.isna(value):
        baseline_hyperparameter_ranges_dict[value.strip()] +=1
    else:
        baseline_hyperparameter_ranges_dict["NA"] +=1
        
for key, value in baseline_hyperparameter_ranges_dict.items():
    print(f"{key}:  {value}")


print("####### Were the best hyperparameters reported for each dataset? ###############")
proposed_hyperparameter_ranges_per_dataset  = data_Top_sequential["Proposed model optimal hyperparameters"]
proposed_hyperparameter_ranges_per_dataset_dict = defaultdict(int)

for value in proposed_hyperparameter_ranges_per_dataset:
    if not pd.isna(value):
        proposed_hyperparameter_ranges_per_dataset_dict[value.strip()] +=1
    else:
        proposed_hyperparameter_ranges_per_dataset_dict["NA"] +=1
        
for key, value in proposed_hyperparameter_ranges_per_dataset_dict.items():
    print(f"{key}:  {value}")


print("####### Were the best hyperparameters reported for each dataset? ###############")
baseline_hyperparameter_ranges_per_dataset  = data_Top_sequential["Baseline model optimal hyperparameters"]
baseline_hyperparameter_ranges_per_dataset_dict = defaultdict(int)

for value in baseline_hyperparameter_ranges_per_dataset:
    if not pd.isna(value):
        baseline_hyperparameter_ranges_per_dataset_dict[value.strip()] +=1
    else:
        baseline_hyperparameter_ranges_per_dataset_dict["NA"] +=1
        
for key, value in baseline_hyperparameter_ranges_per_dataset_dict.items():
    print(f"{key}:  {value}")



print("######################## Embedding size ################################")
embedding_size  = data_Top_sequential["Embedding size"]
embedding_size_dict = defaultdict(int)

for value in embedding_size:
    if not pd.isna(value):
        embedding_size_dict[value.strip()] +=1
    else:
        embedding_size_dict["NA"] +=1
        
for key, value in embedding_size_dict.items():
    print(f"{key}:  {value}")


print("######################## Were the experiments run multiple times to control randomness? ################################")
randomness  = data_Top_sequential["Randomness control"]
randomness_dict = defaultdict(int)

for value in randomness:
    if not pd.isna(value):
        value_ = value.split(",")[0]
        randomness_dict[value_.strip()] +=1
    else:
        randomness_dict["NA"] +=1
        
for key, value in randomness_dict.items():
    print(f"{key}:  {value}")


print("Faisal")
