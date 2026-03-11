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


######################### Was a public dataset used? ################################
print("######################### Was a public dataset used? ################################")
dataset_public_used  = data_Top_sequential["Public dataset"]
dataset_public_used_dict = defaultdict(int)

for value in dataset_public_used:
    if not pd.isna(value):
        value_ = value.split(",")
        dataset_public_used_dict[value_[0].strip()] +=1
    else:
        dataset_public_used_dict["NA"] +=1

dataset_public_used_dict = dict(sorted(dataset_public_used_dict.items()))
for key, value in dataset_public_used_dict.items():
    print(f"{key}:  {value}")


######################### If private data was used, was the choice justified? ################################
print("########## If private data was used, was the choice justified? #######")
private_used  = data_Top_sequential["Private dataset"]
private_used_dict = defaultdict(int)

for value in private_used:
    if not pd.isna(value):
        value_ = value.split(",")
        private_used_dict[value_[0].strip()] +=1
    else:
        private_used_dict["NA"] +=1
    
private_used_dict = dict(sorted(private_used_dict.items()))
for key, value in private_used_dict.items():
    print(f"{key}:  {value}")


######################### Were download links provided? ################################
print("######### Were download links provided? ##########")
dataset_public_used  = data_Top_sequential["Downloadable dataset"]
dataset_public_used_dict = defaultdict(int)

for value in dataset_public_used:
    if not pd.isna(value):
        value_ = value.split(",")
        dataset_public_used_dict[value_[0].strip()] +=1
    else:
        dataset_public_used_dict["NA"] +=1

dataset_public_used_dict = dict(sorted(dataset_public_used_dict.items()))
for key, value in dataset_public_used_dict.items():
    print(f"{key}:  {value}")

######################### Were preprocessed datasets made available for all datasets? ################################
print("########### Were preprocessed datasets made available for all datasets? #########")
processed_used  = data_Top_sequential["Preprocessed dataset"]
processed_used_dict = defaultdict(int)

for value in processed_used:
    if not pd.isna(value):
        value_ = value.split(",")
        processed_used_dict[value_[0].strip()] +=1
    else:
        processed_used_dict["NA"] +=1

processed_used_dict = dict(sorted(processed_used_dict.items()))
for key, value in processed_used_dict.items():
    print(f"{key}:  {value}")


######################### Were train/validation/test splits shared for all datasets? ################################
print("########### Were train/validation/test splits shared for all datasets? ##########")
data_splits_used  = data_Top_sequential["Data splits"]
data_splits_used_used_dict = defaultdict(int)

for value in data_splits_used:
    if not pd.isna(value):
        value_ = value.split(",")
        data_splits_used_used_dict[value_[0].strip()] +=1
    else:
        data_splits_used_used_dict["NA"] +=1

data_splits_used_used_dict = dict(sorted(data_splits_used_used_dict.items()))
for key, value in data_splits_used_used_dict.items():
    print(f"{key}:  {value}")

######################### Were filtering details provided? ################################
print("########### Were filtering details provided? #############")
data_filtering_used  = data_Top_sequential["Data filtering"]
data_filtering_used_used_dict = defaultdict(int)

for value in data_filtering_used:
    if not pd.isna(value):
        value_ = value.split(",")
        data_filtering_used_used_dict[value_[0].strip()] +=1
    else:
        data_filtering_used_used_dict["NA"] +=1

data_filtering_used_used_dict = dict(sorted(data_filtering_used_used_dict.items()))
for key, value in data_filtering_used_used_dict.items():
    print(f"{key}:  {value}")


######################### Was additional context/metadata used, and was it documented? ################################
print("############ Was additional context/metadata used, and was it documented? ############")
side_information_used  = data_Top_sequential["Side information"]
side_information_used_dict = defaultdict(int)

for value in side_information_used:
    if not pd.isna(value):
        value_ = value.split(",")
        for i in value_:
            side_information_used_dict[i.strip()] +=1
    else:
        side_information_used_dict["NA"] +=1

side_information_used_dict = dict(sorted(side_information_used_dict.items()))
for key, value in side_information_used_dict.items():
    print(f"{key}:  {value}")

######################### Were the used embeddings publicly shared? ################################
print("########## Were the used embeddings publicly shared? ############")
embedding_shared  = data_Top_sequential["Used embeddings"]
embedding_shared_dict = defaultdict(int)

for value in embedding_shared:
    if not pd.isna(value):
        value_ = value.split(",")
        embedding_shared_dict[value_[0].strip()] +=1
    else:
        embedding_shared_dict["NA"] +=1
    
embedding_shared_dict = dict(sorted(embedding_shared_dict.items()))
for key, value in embedding_shared_dict.items():
    print(f"{key}:  {value}")


######################### Were the recommendation files saved for datasets? ################################
print("############ Were the recommendation files saved for datasets? ##############")
recommendation_files_shared  = data_Top_sequential["Recommendation files"]
recommendation_files_shared_dict = defaultdict(int)

for value in recommendation_files_shared:
    if not pd.isna(value):
        value_ = value.split(",")
        recommendation_files_shared_dict[value_[0].strip()] +=1
    else:
        recommendation_files_shared_dict["NA"] +=1

recommendation_files_shared_dict = dict(sorted(recommendation_files_shared_dict.items()))
for key, value in recommendation_files_shared_dict.items():
    print(f"{key}:  {value}")


######################### Are the statistics of the datasets documented before or after preprocessing? ################################
print("######### Are the statistics of the datasets documented before or after preprocessing? ############")
data_statics_shared  = data_Top_sequential["Dataset statistics"]
data_statics_shared_dict = defaultdict(int)

for value in data_statics_shared:
    if not pd.isna(value):
        value_ = value.split(",")
        data_statics_shared_dict[value_[0].strip()] +=1
    else:
        data_statics_shared_dict["NA"] +=1
    
data_statics_shared_dict = dict(sorted(data_statics_shared_dict.items()))
for key, value in data_statics_shared_dict.items():
    print(f"{key}:  {value}")

print("Faisal")
