

class Process:

    def __init__(self, dict):
        self.oid = dict["OID"]
        self.processId = dict["ProcessID"]
        self.parentId = dict["ParentPID"]
        self.commandLine = dict["CommandLine"]
        self.image = dict["Image"]
        self.processType = dict["ProcessType"]
        self.creationTimestamp = dict["CreationTimestamp"]

    def compare(self, other):
        pass


