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
print("######################### Were the hardware resources (GPU/TPU/CPU, RAM) specified? ################################")
hardware_used  = data_Top_sequential["Hardware details"]
hardware_used_dict = defaultdict(int)
# number of time GPUs information reported
hardware_info_reported = defaultdict(int)

for value in hardware_used:
    if not pd.isna(value):
        value_ = value.split(",")
        hardware_info_reported[value.strip()] +=1
        for i in value_:
            if "NVIDIA" in i:
                hardware_used_dict[i.strip()] +=1
    else:
        hardware_used_dict["NA"] +=1
        hardware_info_reported["NA"] +=1

hardware_used_dict = dict(sorted(hardware_used_dict.items()))
for key, value in hardware_used_dict.items():
    print(f"{key}:  {value}")


######################### Was a public dataset used? ################################
print("######################### Is a library requirements file (software dependencies) provided? ################################")
requirement_file  = data_Top_sequential["Requirements file"]
requirement_file_dict = defaultdict(int)

for value in requirement_file:
    
    value_ = value.split(",")
    requirement_file_dict[value_[0]] +=1 
    
requirement_file_dict = dict(sorted(requirement_file_dict.items()))
for key, value in requirement_file_dict.items():
    print(f"{key}:  {value}")


print("######################### Were CUDA/cuBLAS/cuDNN versions provided? ################################")
intermediate_libraries  = data_Top_sequential["Intermediate libraries"]
intermediate_libraries_dict = defaultdict(int)

for value in intermediate_libraries:
    
    if not pd.isna(value):
        value_ = value.split(",")
        intermediate_libraries_dict[value_[0]] +=1
    else:
        intermediate_libraries_dict["NA"] +=1
    
intermediate_libraries_dict = dict(sorted(intermediate_libraries_dict.items()))
for key, value in intermediate_libraries_dict.items():
    print(f"{key}:  {value}")


print("######################### Were the computing time documented? ################################")
runtime_cost  = data_Top_sequential["Runtime cost"]
runtime_cost_dict = defaultdict(int)

for value in runtime_cost:
    
    if not pd.isna(value):
        value_ = value.split(",")
        runtime_cost_dict[value_[0]] +=1
    else:
        runtime_cost_dict["NA"] +=1
    
runtime_cost_dict = dict(sorted(runtime_cost_dict.items()))
for key, value in runtime_cost_dict.items():
    print(f"{key}:  {value}")


print("######################### Was energy usage or environmental cost reported? ################################")
carbon_footprint  = data_Top_sequential["Carbon footprint"]
carbon_footprint_dict = defaultdict(int)

for value in carbon_footprint:
    
    if not pd.isna(value):
        value_ = value.split(",")
        carbon_footprint_dict[value_[0]] +=1
    else:
        carbon_footprint_dict["NA"] +=1
    
carbon_footprint_dict = dict(sorted(carbon_footprint_dict.items()))
for key, value in carbon_footprint_dict.items():
    print(f"{key}:  {value}")


print("################### Were instructions provided for small-scale replication (e.g., subset experiments)? ############")
reproduction_limited_resources  = data_Top_sequential["Reproduction with limited resources"]
reproduction_limited_resources_dict = defaultdict(int)

for value in reproduction_limited_resources:
    
    if not pd.isna(value):
        value_ = value.split(",")
        reproduction_limited_resources_dict[value_[0]] +=1
    else:
        reproduction_limited_resources_dict["NA"] +=1
    
reproduction_limited_resources_dict = dict(sorted(reproduction_limited_resources_dict.items()))
for key, value in reproduction_limited_resources_dict.items():
    print(f"{key}:  {value}")

print("Faisal")