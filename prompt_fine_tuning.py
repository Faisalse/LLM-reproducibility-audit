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



############
print("################## prompt_documentation ##################")
prompt_documentation  = data_Top_sequential["Prompt documentation"]
prompt_documentation_dict = defaultdict(int)
for value in prompt_documentation:
    if not isinstance(value, float):
        prompt_documentation_dict[value.strip()]+=1

for key, value in prompt_documentation_dict.items():
    print(f"{key}:  {value}")



############
print("##############    Prompt type #######################")
prompt_type           = data_Top_sequential["Prompt type"]
prompt_type_dict = defaultdict(int)

for value in prompt_type:
    if not isinstance(value, float):
        for temp in value.split(","):

            prompt_type_dict[temp.strip()] +=1

for key, value in prompt_type_dict.items():
    print(f"{key}:  {value}")


print("###################### Prompt tempate #############################")
prompt_template       = data_Top_sequential["Prompt templates"]
prompt_template_dict = defaultdict(int)

for value in prompt_template:

    if not isinstance(value, float):
        prompt_template_dict[value.strip()]+=1
for key, value in prompt_template_dict.items():
    print(f"{key}:  {value}")

print("############################### promot context length #################################")
prompt_context_length = data_Top_sequential["Context length"]
prompt_context_length_dict = defaultdict(int)

for value in prompt_context_length:
    if not isinstance(value, float):
        prompt_context_length_dict[value.strip()]+=1

for key, value in prompt_context_length_dict.items():
    print(f"{key}: {value}")

"""


print("######################### fine tuning material shared ######################################")
fine_tuning_materials = data_Top_sequential["Fine-tuning materials"]
fine_tuning_materials_dict = defaultdict(int)

for value in fine_tuning_materials:
    if not pd.isna(value):
        fine_tuning_materials_dict["in_number_papers_models_are_fine_tuned"] +=1
        value_ = value.split(",")
        for i in value_:
            fine_tuning_materials_dict[i.strip()] +=1

for key, value in fine_tuning_materials_dict.items():
    print(f"{key}: {value}")



print("######################### Fine tuning strategy ######################################")
fine_tuning_strategy = data_Top_sequential["Fine-tuning strategy"]
fine_tuning_strategy_dict = defaultdict(int)

for value in fine_tuning_strategy:
    if not pd.isna(value):
        value_ = value.split(",")
        for i in value_:
            fine_tuning_strategy_dict[i.strip()] +=1
            
for key, value in fine_tuning_strategy_dict.items():
    print(f"{key}: {value}")

print("######################### Checkpoints ######################################")
checkpoints = data_Top_sequential["Checkpoints"]
checkpoints_dict = defaultdict(int)
for value in checkpoints:
    if not pd.isna(value):
        value_ = value.split(",")
        checkpoints_dict[value_[0].strip()] +=1
            

for key, value in checkpoints_dict.items():
    print(f"{key}: {value}")



print("######################### Model weights ######################################")
model_weights = data_Top_sequential["Model weights"]
model_weights_dict = defaultdict(int)
for value in model_weights:
    if not pd.isna(value):
        value_ = value.split(",")
        for i in value_:
            model_weights_dict[i.strip()] +=1

for key, value in model_weights_dict.items():
    print(f"{key}: {value}")


print("######################### Tokenizer version ######################################")
tokenizer_version = data_Top_sequential["Tokenizer version"]
tokenizer_version_dict = defaultdict(int)
for value in tokenizer_version:
    if not pd.isna(value):
        tokenizer_version_dict[value.strip()] +=1
for key, value in tokenizer_version_dict.items():
    print(f"{key}: {value}")


print("######################### Vocabulary size ######################################")
vocabulary_size = data_Top_sequential["Vocabulary size"]
vocabulary_size_dict = defaultdict(int)
for value in vocabulary_size:
    if not pd.isna(value):
        value_ = value.split(",")
        vocabulary_size_dict[value_[0].strip()] +=1

for key, value in vocabulary_size_dict.items():
    print(f"{key}: {value}")

print("Faisal")
"""