# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 20:15:34 2020

@author: erolc
"""
#import libraries
import pipeline_caller
import os
caller = pipeline_caller.PipelineCaller()
my_directory = os.getcwd()

#functions for reading and writing data (same as part_1)
inp_path,out_path,token_path = my_directory+"\\in\\in.txt",my_directory+"\\out\\out.txt",my_directory+"\\my_token.txt"
def read_input(input_path):
    with open(input_path,encoding = "utf8") as file:
        result = file.readlines()
    return result
def write_output(output_path,items):
    file = open(output_path,"w",encoding = "utf8")
    items = map(lambda x: x + '\n', items)
    for e in items:
        file.write(e)
    file.close()

# my dataset is already formatted sentence by sentence. Thus, I will apply dependency parser to these sentences directly.
token = read_input(token_path)[0] #get ITU NLP API token from directory.
def dependency_parser(input_path,output_path,token=token):
    my_data,output = read_input(input_path)[:150],[] #ITU NLP API has limits for every user. Thus, I will analyze first 150 sentences. 
    for e in my_data:
        snt,deptags,dependents = e[:-1],{},{}
        result = caller.call("pipelineNoisy", snt, token) #Here I applied whole NLP pipeline to my sentences. Because Noisy Dependency Parser doesn't work properly.
        for e in result.split("\n"): #Here, I am cleaning the NLP pipeline results.
            splitted_word = e.split("\t")
            if len(splitted_word) > 1 and splitted_word[1] != "_":
                deptags[splitted_word[1]] = (splitted_word[-1],splitted_word[-2]) # Constructing a hash table to keep dependency tags for every words.
                dependents[splitted_word[0]] = splitted_word[1]
            elif len(splitted_word) > 2: #This elif block is added for tool-specific cleaning.
                deptags[splitted_word[2]] = (splitted_word[-1],splitted_word[-2])
                dependents[splitted_word[0]] = splitted_word[2]
        sentence_with_deps = ""
        for f in snt.split():
            if f in deptags:
                sentence_with_deps += f+"("+deptags[f][0]+" -> " #Reconstructing the sentences as Word-1 (dependency token-1 -> dependent word-1) Word-2 (dependency token-2 -> dependent word-2) ... Word-n (dependency token-n -> dependent word-n).
                if deptags[f][1] != "0": #These blocks discriminates root and others.
                    sentence_with_deps += dependents[deptags[f][1]]+") "
                else: 
                    sentence_with_deps += "root) "
        output.append(sentence_with_deps[:-1])
    write_output(output_path,output) #writing data to the output file.

dependency_parser(inp_path,out_path) #running dependency parser.                 

        
            
            