import readJsonFile
from ProcessTreeClass import ProcessTree

tree = readJsonFile.flatten_tree("test")

tree_list  = tree.list_all_sub_tree()

for tree in tree_list:
    print(tree.show_node())
