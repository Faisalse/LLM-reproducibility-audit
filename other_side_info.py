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



print("####### Was the evaluation procedure described in detail, e.g., leave-one-out, cross-validation? ###############")
evaluation_procedure  = data_Top_sequential["Evaluation procedure"]
evaluation_procedure_dict = defaultdict(int)

for value in evaluation_procedure:
    if not pd.isna(value):
        value_ = value.split(",")
        evaluation_procedure_dict[value_[0].strip()] +=1
    else:
        evaluation_procedure_dict["NA"] +=1
        
for key, value in evaluation_procedure_dict.items():
    print(f"{key}:  {value}")




print("####### Is the ratio of the validation dataset mentioned? ###############")
validation_data  = data_Top_sequential["Validation dataset"]
validation_data_dict = defaultdict(int)

for value in validation_data:
    if not pd.isna(value):
        value_ = value.split(",")
        validation_data_dict[value_[0].strip()] +=1
    else:
        validation_data_dict["NA"] +=1
        
for key, value in validation_data_dict.items():
    print(f"{key}:  {value}")


print("####### Optimization metric ###############")
optimization_metric  = data_Top_sequential["Optimization metric"]
optimization_metric_dict = defaultdict(int)

for value in optimization_metric:
    if not pd.isna(value):
        value_ = value.split(",")
        optimization_metric_dict[value_[0].strip()] +=1
    else:
        optimization_metric_dict["NA"] +=1
        
for key, value in optimization_metric_dict.items():
    print(f"{key}:  {value}")



print("####### Evaluation (Full vs. Sampled) ###############")
evaluation_full  = data_Top_sequential["Evaluation (Full vs. Sampled)"]
evaluation_full_dict = defaultdict(int)

for value in evaluation_full:
    if not pd.isna(value):
        value_ = value.split(",")
        evaluation_full_dict[value_[0].strip()] +=1
    else:
        evaluation_full_dict["N/A"] +=1
        
for key, value in evaluation_full_dict.items():
    print(f"{key}:  {value}")


print("############################## Evauation measures ###############")
evaluation_measures  = data_Top_sequential["Evauation measures"]
evaluation_full_dict = defaultdict(int)

for value in evaluation_measures:
    if not pd.isna(value):
        value_ = value.split(",")
        for i in value_:
            evaluation_full_dict[i.strip()] +=1
    else:
        evaluation_full_dict["N/A"] +=1
        
for key, value in evaluation_full_dict.items():
    print(f"{key}:  {value}")


print("############################## Used datasets ###############")
used_datasets  = data_Top_sequential["Used datasets"]
used_datasets_dict = defaultdict(int)

for value in used_datasets:
    datasets = value.split(",")
    for data_ in datasets:
        if "amazon" in data_.lower():
            used_datasets_dict["Amazon"]+=1
        elif "gowalla" in data_.lower():
            used_datasets_dict["Gowalla"]+=1
        elif "movielens" in data_.lower():
            used_datasets_dict["MovieLens"]+=1
        elif "yelp" in data_.lower():
            used_datasets_dict["Yelp"]+=1
        elif "mind" in data_.lower():
            used_datasets_dict["MIND"]+=1
        elif "inspired" in data_.lower():
            used_datasets_dict["INSPIRED"]+=1
        elif "reddit" in data_.lower():
            used_datasets_dict["Reddit"]+=1
        
        elif "google" in data_.lower():
            used_datasets_dict["Google"]+=1
        
        elif "redial" in data_.lower():
            used_datasets_dict["ReDial"]+=1
        
        elif "foursquare" in data_.lower():
            used_datasets_dict["Foursquare"]+=1

        else:
            used_datasets_dict[data_.strip()]+=1
            used_datasets_dict["total"]+=1
        
    

        
for key, value in used_datasets_dict.items():
    print(f"{key}:  {value}")


print("############################## Statistical test ###############")
statistical_test  = data_Top_sequential["Statistical test"]
statistical_test_dict = defaultdict(int)

for value in statistical_test:
    if not pd.isna(value):
            statistical_test_dict[value.strip()] +=1
    else:
        statistical_test_dict["N/A"] +=1
        
for key, value in statistical_test_dict.items():
    print(f"{key}:  {value}")

print("Faisal")

