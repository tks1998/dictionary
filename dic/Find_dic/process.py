from typing import Tuple
from django.conf import settings
import pickle
import os
from . import config
#from .trie import TrieNode

from django.conf import settings


class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.word_finished = False
        self.index = -1


def add(root, word: str, index=-1):
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
    if node.word_finished == 1:
        node.word_finished = -1
        return True
    return False   
def make_tree():
    filePath = os.path.join(os.path.dirname(__file__), "data2.txt")
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


def test(find_name):
    if (config.Build_Tree == False):
        config.root = make_tree()
        config.Build_Tree = True
    
    idx = find_prefix(config.root, find_name)
    if idx == -1:
        return {
            "name": find_name,
            "mean": "not found"
        }
    filePath = os.path.join(os.path.dirname(__file__), "data2.txt")
    f = open(filePath, 'r')
    f.seek(idx)
    mean = f.readline().split(':')[1]
    return {
        "name": find_name,
        "mean": mean
    }
