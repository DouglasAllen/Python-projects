from ctypes import *
class linknode(Structure):
    pass
linknode._fields_ = [
                           ("nextNode", POINTER(linknode)),
                           ("intData", c_int),
                         ]
                
class linked_list():
    """ our own linked list based on ctypes """
    head_node = None
   
    def add(self, int_data):
        node_to_add = linknode()
        node_to_add.intData = int_data
        node_to_add.nextNode = None
        if (self.head_node == None):
            self.head_node = node_to_add
            return
        else:
            traverse_node = self.head_node
            #while(not(traverse_node.nextNode == None)):
            print(traverse_node.nextNode)
            
if __name__ == "__main__":
    ll = linked_list()
    ll.add(5)
    ll.add(6)
    
    
from ctypes import *
#~ from see import see
import sys
class linknode(Structure):
    pass
linknode._fields_ = [
                ("nextNode", POINTER(linknode)),
                ("intData", c_int),
                ]
class linked_list():
    """ our own linked list based on ctypes """
    head_node = None
   
    def add(self, int_data):
        node_to_add = linknode(intData = c_int(int_data))
        if (self.head_node == None):
            self.head_node = node_to_add
        else:
            traverse_node = self.head_node
            node = traverse_node
            try:
                while node.nextNode.contents:
                    node = node.nextNode.contents
            except ValueError:
                node.nextNode = POINTER(linknode)(node_to_add)
            except:
                pass
    def __getitem__(self, n):
        node = self.head_node
        for i in range(n):
            node = node.nextNode.contents
        return node
                
if __name__ == "__main__":
    ll = linked_list()
    for i in range(10):
        print("Adding %s"%(i))
        ll.add(i)
    print( ll[9].intData)