# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 21:21:15 2020

@author: erolc
"""

#import libraries
import os
import json

#functions for reading and writing data 
my_directory = os.getcwd()
inp_path,out_path = my_directory+"\\in\\in.txt",my_directory+"\\out\\out.json"
def read_input(input_path):
    with open(input_path,encoding = "utf8") as file:
        result = file.readlines()
    return result
def write_output(output_path, finaldata):
    with open(output_path, "w",encoding = "utf8") as jsondata:
        json.dump(finaldata,jsondata, ensure_ascii=False)
data = read_input(inp_path)              

"""
Task-1:
In this HW, I will build hash table data structure to keep my data more reachable.
Hash tables are very efficient for most of the data analysis tasks. Reaching 
to the value of any element of the hash table keys has O(1) time complexity.     

Task-2:
Since JSON format uses list of hash tables, this is the best format for me. 
Also, I am experienced in this format. Thus, I chose JSON to export my data.


Task-3:
In my course project, I want to create a new dataset from scratch. This will be
a clear and well structured dataset. Thus, I am working on a different dataset for homework
and I do not need any meta-data at this stage.
"""

def structure_data(data=data):
    result = {}
    for e in data: # Basically, I trace my data and create lists for dependency structures.
        list_of_analysis = e[:-1].split("(")
        result[list_of_analysis[0]] = [] #Working on the first element.
        temp = list_of_analysis[0]
        for f in list_of_analysis[1:-1]: #Since I used split function, first and last elements will be outliers. I should work on them separately. This is why [1:-1]
            words_and_tags = f.split()
            result[temp].append((words_and_tags[2][:-1],words_and_tags[0]))
            temp = words_and_tags[3]
            if temp not in result:
                result[temp] = []
        words_and_tags = list_of_analysis[-1].split() #Working on the last element.
        result[temp].append((words_and_tags[2][:-1],words_and_tags[0]))
    return result

write_output(out_path,structure_data())


      
            