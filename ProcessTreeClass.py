from ProcessClass import Process
from BasicStack import Stack

class ProcessTree:

    def __init__(self, process_list):
        self.process_list = process_list


    def get_process_list(self):
        return self.process_list


    def set_process_list(self, process_list):
        self.process_list = process_list

    def list_all_sub_tree(self):

        sub_tree_list = []
        stack = Stack([])

        for p in reversed(self.process_list):

            list_temp = Stack([])
            if(stack.isEmpty() or (stack.peek()).peek().parentId != p.processId):
                list_temp.push(p)
                stack.push(list_temp)
                sub_tree_list.append(ProcessTree(list_temp.to_list()))
            else:
                temp = []
                count = 0
                list_temp = Stack([])
                while(not stack.isEmpty() and (stack.peek()).peek().parentId == p.processId):

                    list_temp = stack.pop()
                    temp += list_temp.to_list()
                    count += 1
                    list_temp.push(p)
                    # stack.push(list_temp)
                    sub_tree_list.append(ProcessTree(list_temp.to_list()))

                if(count > 1):
                    temp.insert(0, p)
                    sub_tree_list.append(ProcessTree(temp))
                    temp.reverse()
                    stack.push(Stack(temp))
                elif (count == 1):
                    stack.push(list_temp)
        return sub_tree_list




    def show_node(self):
        tree_string = ""
        for node in self.process_list:
            tree_string = tree_string +  str(node.processId) + " "
        return tree_string