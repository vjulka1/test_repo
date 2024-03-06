# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 08:13:52 2023

@author: priya
"""

with open("data.txt") as f:
    story = f.read()
    
    
print(story)

wlist=[]
for i in story.split():
    if i[0]=="<":
        wlist.append(i)
        
wset = set(wlist)
new_words = ["" for i in range(len(wset))]
w_dict = dict(zip(wset,new_words))
        
#print(wlist)
#print(wset)
#print(w_dict)

for i in w_dict.keys():
    w_dict[i] = input(f"what do you want to replace {i} with ")

print(w_dict)

with open("data.txt") as f:
    story = f.read()
 
words= story.split()
print(words)
 

for i in range(len(words)):
    if words[i] in w_dict.keys():
        words[i] = w_dict[words[i]]
print(words)

print(" ".join(words))
        
  