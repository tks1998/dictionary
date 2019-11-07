from django.conf import settings
import pickle
import os
from . import config
from django.conf import settings


class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.index = -1


def add(root, word: str, index=-1):
    print(index)
    node = root
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.char == char:
                node = child
                found_in_child = True
                break
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node
    print(word,index)
    node.index = index
    return 


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
            # return node.recomend
    return node.index
def delete_word(root,prefix:str):
    node = root
    if not root.children:
        return False
    if not prefix:
        return False
    for char in prefix:
        char_not_found = True
        for child in node.children:
            if child.char == char:
                char_not_found = False
                node = child
                break
        if char_not_found:
            return False   # It not in dictionary -> don't sucess delete it
    if node.index != -1:
        node.index = -1
        return True
    return False   

def make_tree():
    filePath = os.path.join(os.path.dirname(__file__), "data.txt")
    f = open(filePath, 'r')

    root = TrieNode('*')
    while True:
        offset = f.tell()
        line = f.readline()
        if not line:
            break
        name = line.split(':')[0]
        add(root, name, offset)
    return root

def get_request_and_delete(name):
    if (config.Build_Tree == False):
        config.root = make_tree()
        config.Build_Tree = True
    pickle_out = open("root.pickle","wb")   # cap nhat -> ghi vao file pickle
    pickle.dump(config.root, pickle_out)
    pickle_out.close()
    return {"status":delete_word(config.root,name)}
def get_request_and_add(name:str,mean:str):
    if (config.Build_Tree == False):
        config.root = make_tree()
        config.Build_Tree = True
    if find_prefix(config.root,name) != -1:
        return 
    # add word to file data
    new_word = name+":"+mean+"\n"
    filePath = os.path.join(os.path.dirname(__file__), "data.txt")
    f = open(filePath, 'a')
    idx =f.tell()
    f.writelines(new_word)
    
    f.close()
    # add new word 
    add(config.root,name,idx)
    # save struct root with pickle file 
    pickle_out = open("root.pickle","wb")
    pickle.dump(config.root, pickle_out)
    pickle_out.close()
    return  
def get_request_and_find(find_name):
    if (config.Build_Tree == False):
        config.root = make_tree()
        config.Build_Tree = True
    
    idx = find_prefix(config.root, find_name)
    if idx == -1:
        return {
            "name": find_name,
            "mean": "not found"
        }
    filePath = os.path.join(os.path.dirname(__file__), "data.txt")
    f = open(filePath, 'r')
    f.seek(idx)
    mean = f.readline().split(':')[1]
    f.close()
    pickle_out = open("root.pickle","wb")
    pickle.dump(config.root, pickle_out)
    pickle_out.close()
    return {
        "name": find_name,
        "mean": mean
    }
