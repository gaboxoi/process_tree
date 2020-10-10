import json
from ProcessClass import Process
from ProcessTreeClass import ProcessTree

node_relation = {}
node_val = {}


def read_file(file_name):

    f = open("json/" + file_name + ".json")
    data = json.load(f)
    main_process_id = 0
    for i in data["Processes"]:
        node = Process(i)
        if(node.processType == "Main process"):
            main_process_id = node.processId
        node_relation.update({node.processId: []})
        node_val.update({node.processId: node})
        if(node.parentId in node_relation):
            node_relation.get(node.parentId).append(node.processId)
    return main_process_id

def link_node(tree_list,root):
    chil_list = node_relation.get(root)
    for i in chil_list:
        tree_list.append(node_val.get(i))
        link_node(tree_list, i)


def flatten_tree(file_name):
    main_process_id = read_file(file_name)
    tree_list = []
    tree_list.append(node_val.get(main_process_id))
    link_node(tree_list, main_process_id)
    return ProcessTree(tree_list)



