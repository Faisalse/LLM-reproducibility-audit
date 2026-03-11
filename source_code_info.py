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


print("##############    Repository link #######################")
repository_link           = data_Top_sequential["Repository link"]
repository_link_dict= defaultdict(int)

for value in repository_link:
    
    value_ = value.split(",")
    repository_link_dict[value_[0].strip()] +=1

for key, value in repository_link_dict.items():
    print(f"{key}:  {value}")

print("#############################    Proposed model code #######################")

proposed_model           = data_Top_sequential["Proposal model(s)"]
proposed_model_dict = defaultdict(int)

for value in proposed_model:
    
    value_ = value.split(",")
    proposed_model_dict[value_[0].strip()] +=1

for key, value in proposed_model_dict.items():
    print(f"{key}:  {value}")


print("#############################    Baseline model(s) #######################")

baseline_model           = data_Top_sequential["Baseline model(s)"]
baseline_model_dict = defaultdict(int)

for value in baseline_model:
    
    if not pd.isna(value):
        value_ = value.split(",")
        baseline_model_dict[value_[0].strip()] +=1
    else:
        baseline_model_dict["baseline_model_not_used"] +=1

for key, value in baseline_model_dict.items():
    print(f"{key}:  {value}")



print("#############################    Hyperparameter-tuning code #######################")
proposed_hyper_tuning  = data_Top_sequential["Hyperparameter-tuning code"]
proposed_hyper_tuning_dict = defaultdict(int)

for value in proposed_hyper_tuning:
    if not pd.isna(value):
        value_ = value.split(",")
        proposed_hyper_tuning_dict[value_[0].strip()] +=1
    else:
        proposed_hyper_tuning_dict["NA"] +=1
for key, value in proposed_hyper_tuning_dict.items():
    print(f"{key}:  {value}")



print("#############################    Data preprocessing #######################")
data_processing_code  = data_Top_sequential["Data preprocessing"]
data_processing_code_dict = defaultdict(int)

for value in data_processing_code:
    if not pd.isna(value):
        value_ = value.split(",")
        data_processing_code_dict[value_[0].strip()] +=1
    else:
        data_processing_code_dict["NA"] +=1
for key, value in data_processing_code_dict.items():
    print(f"{key}:  {value}")


print("#############################    Statistical analysis #######################")
statistical  = data_Top_sequential["Statistical analysis"]
statistical_dict = defaultdict(int)

for value in statistical:
    if not pd.isna(value):
        value_ = value.split(",")
        statistical_dict[value_[0].strip()] +=1
    else:
        statistical_dict["NA"] +=1
for key, value in statistical_dict.items():
    print(f"{key}:  {value}")


print("#############################    Baseline implementation #######################")
baseline_implementation  = data_Top_sequential["Baseline implementation"]
baseline_implementation_dict = defaultdict(int)

for value in baseline_implementation:
    if not pd.isna(value):
        value_ = value.split(",")
        baseline_implementation_dict[value_[0].strip()] +=1
    else:
        baseline_implementation_dict["NA"] +=1
for key, value in baseline_implementation_dict.items():
    print(f"{key}:  {value}")


print("#############################    Supplementary info. #######################")
supplementary  = data_Top_sequential["Supplementary info."]
supplementary_dict = defaultdict(int)

for value in supplementary:
    if not pd.isna(value):
        value_ = value.split(",")
        supplementary_dict[value_[0].strip()] +=1
    else:
        supplementary_dict["NA"] +=1
for key, value in supplementary_dict.items():
    print(f"{key}:  {value}")

print("#############################    Docker file #######################")
docker  = data_Top_sequential["Docker file"]
docker_dict = defaultdict(int)

for value in docker:
    if not pd.isna(value):
        value_ = value.split(",")
        docker_dict[value_[0].strip()] +=1
    else:
        docker_dict["NA"] +=1
for key, value in docker_dict.items():
    print(f"{key}:  {value}")

print("#############################    Steps to run experiments on any platform #######################")
steps_to_algo_any_platform  = data_Top_sequential["Steps to run experiments on any platform"]
steps_to_algo_any_platform_dict = defaultdict(int)

for value in steps_to_algo_any_platform:
    if not pd.isna(value):
        value_ = value.split(",")
        steps_to_algo_any_platform_dict[value_[0].strip()] +=1
    else:
        steps_to_algo_any_platform_dict["NA"] +=1
for key, value in steps_to_algo_any_platform_dict.items():
    print(f"{key}:  {value}")

print("Faisal")

