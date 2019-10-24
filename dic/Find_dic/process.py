from typing import Tuple
from django.conf import settings
import json

class TrieNode(object):    
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.word_finished = False 
        self.counter = 1
        self.index = -1
        self.recomend = []

def add(root, word: str,index = -1):
    node = root
    for char in word:
        found_in_child = False
        node.recomend.append(index)
        for child in node.children:
            if child.char == char:
                child.counter += 1
                node = child
                found_in_child = True
                
                break
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node
    node.word_finished = True
    node.index = index 

def find_prefix(root, prefix: str):
    node = root
    if not root.children:
        return -1
    if not prefix:
        return -1
    for char in prefix:
        char_not_found = True
        for child in node.children:
            if child.char == char:
                char_not_found = False
                node = child
                break
        if char_not_found:
            return -1
            #return node.recomend
    return node.index
def test(find_name):
    """
        load data
    """
    try:
        with open('find_dic/data.json') as json_dataset:
            dataset = json.load(json_dataset)
    except FileNotFoundError:
        json_data = {"test": []}
    """
        process
    """
    root = TrieNode('*')
    for x in dataset:
        add(root,dataset[x]["name"],x)
    idx = None
    idx = find_prefix(root,find_name)

    # if len(idx)== 0:
    #     return {
    #         "name":"not found",
    #         "mean":"not found"
    #     }
    # dem = 0 
    # result = {}
    # for x in idx:
    #     print("toi la x trong for ",x)
    #     result[dem] = {
    #         "name":dataset[x]["name"],
    #         "mean":dataset[x]["mean"]
    #     }
    #     dem = dem + 1
    # print("toi la kq")
    # print(result)
    # return result
    if idx == -1:
        return {
            "name":find_name,
            "mean":"not found"
        }
    return {
        "name":dataset[idx]["name"],
        "mean":dataset[idx]["mean"]
    }
