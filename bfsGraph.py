## a bfs class which contins method to add remove
class Classbfs:

      def __init__(self):
          self.dataStructure=[]

      def isEmpty(self):
          return self.dataStructure==[]

      def __str__(self):
           return str(self.dataStructure)
      def add(self,value):
          self.dataStructure.append(value)
      def remove(self,):
         return self.dataStructure.pop(0)

## gets the value till it find the first given words and returns the list
def getAllConnections(first, last, parentNode):
    last = last.value
    connetions = [last]

    if last in parentNode:
        node = parentNode[last]
        while node != first.value:
            connetions.append(node)
            node = parentNode[node]
    else:
        " No word Connection"
    connetions.append(first.value)
    return connetions[::-1]
##a breadth first search appraoch to create the graph
def bfs(first, last, nodes):
    bfsObject=Classbfs()
    bfsObject.add(first)

    parentNode={}
    parentNode[first.value]=None

    while(not bfsObject.isEmpty()):

          child=bfsObject.remove()

          for edges in child.edges:
              node=edges.value

              if node not in parentNode:
                 parentNode[node]=child.value
                 if node == last.value:
                     return parentNode
                 bfsObject.add(nodes[edges.value])

    return parentNode
