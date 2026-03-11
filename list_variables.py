import pandas as pd
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

"""
# find how times different LLM models are used
llm_version = data_Top_sequential["LLM version"]
llm_version_dict = defaultdict(int)
for ver_ in llm_version:
    comma_based_split = ver_.split(",")
    for temp in comma_based_split:
        name = temp.split("-")[0]
        name = name.strip()
        llm_version_dict[name]+=1

llm_version_dict = dict(sorted(llm_version_dict.items(), key=lambda kv: kv[1], reverse=True))
print(llm_version_dict)

# OpenAI models
llm_version = data_Top_sequential["LLM version"]
open_ai = defaultdict(int)
open_model_list = list()
for ver_ in llm_version:
    
    if "OpenAI" in ver_:
        open_ai["number_papers"] +=1
        open_model_list.append(ver_)
        
    comma_based_split = ver_.split(",")
    for temp in comma_based_split:

        if "snaps not given" in temp:
            open_ai["snap_not_given"] +=1

        elif "snaps given" in temp:
            open_ai["snap_given"] +=1
        elif "both snaps and model version not given" in temp:
            open_ai["both_not_given"] +=1
      
print(open_ai)
"""
llm_version = data_Top_sequential["LLM version"]
temp_list = list()
for ver_ in llm_version:
    comma_based_split = ver_.split(",")
    for temp in comma_based_split:

        if "OpenAI".lower() not in temp.lower():
            temp_list.append(temp.strip())


for i in temp_list:
    print(i)



# Llama models....
llm_version = data_Top_sequential["LLM version"]
llama = defaultdict(int)
llama_model_list = list()
for ver_ in llm_version:
    if "llama" in ver_.lower():
        llama["number_papers"] +=1
        
    comma_based_split = ver_.split(",")
    for temp in comma_based_split:
        if "llama" in temp.lower():
            llama_model_list.append(temp)
            
            if "incomplete" in temp:
                llama["incomplete"]+=1


for i in llama_model_list:
    if "incomplete" in i.strip().lower():
        print(i.strip().lower())




# Other models
llm_version = data_Top_sequential["LLM version"]
other_models = defaultdict(int)
other_model_list = list()
for ver_ in llm_version:
    comma_based_split = ver_.split(",")
    for temp in comma_based_split:
        if "llama" not in temp.lower() and "openai" not in temp.lower():
            other_model_list.append(temp)







# Authors.......
authors =  data_Top_sequential["Country"]
authors_dict = defaultdict(int)

for name_ in authors:
    temp = name_.split(",")
    for i in temp:
        authors_dict[i.strip()] +=1
authors_dict = dict(sorted(authors_dict.items(), key=lambda kv: kv[1], reverse=True))            




university =  data_Top_sequential["University"]
university_dict = defaultdict(int)

for name_ in university:
    temp = name_.split(",")
    for i in temp:
        university_dict[i.strip()] +=1
university_dict = dict(sorted(university_dict.items(), key=lambda kv: kv[1], reverse=True))  
print("Faisal")