class TrieNode(object):    
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.word_finished = False 
        self.index = -1

def add(root, word: str,index = -1):
    node = root
    for char in word:
        found_in_child = False
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