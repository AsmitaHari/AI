
from bfsGraph import bfs,getAllConnections ##gets the methods from the bfs class

##reads the words from the file and creates a list of words which differ by a char from the given word
def readFromDict(filename):
    words=[w.strip() for w in open(filename) if w==w.lower()]

    oneCharDiffLetter={}
    for word in words:

        for index in range(len(word)):
            difference = word[:index] + '*' + word[index + 1:]
            if difference in oneCharDiffLetter:
                oneCharDiffLetter[difference].append(word)
            else:
                oneCharDiffLetter[difference] = [word]
    return oneCharDiffLetter ##returs the lsit of words
## a node class which holds the value and edges list

class bfsNode:
      def __init__(self,value):
          self.value=value
          self.edges=[]
      __slots__ = ('value','edges')


##creates the noighbour for each of the given word
def createGraph(firstWord, secondWord):
    if firstWord not in Connections:##checks the first word is the list
        node = bfsNode(firstWord)
        node.edges.append(bfsNode(secondWord))
        Connections[firstWord] = node
    else:

        connections = Connections[firstWord].edges
        ##if the first exists it checks for the second word and appends it to the list

        if secondWord not in [existing.value for existing in connections]:
            connections.append(bfsNode(secondWord))

    if secondWord not in Connections:
        node = bfsNode(secondWord)
        node.edges.append(bfsNode(secondWord))
        Connections[secondWord] = node
    else:

        connections = Connections[secondWord].edges

        if firstWord not in [existing.value for existing in connections]:
            connections.append(bfsNode(firstWord))


##call the create tgraph function by going through each of words
def bfsWordGraph(dict):
    for key in dict:
        list = dict[key]
        for start in list:
            for end in list:
                if start != end:
                   createGraph(start, end)

##checks the bfs tree if there exists a path between the first and the second word
def printPath(firsword,secondword):

    returnValue=""
    if firsword in Connections:
       first=Connections[firsword]

       if secondword in Connections:
           end=Connections[secondword]
           previous = bfs(first,end,Connections)

           shortestPath= getAllConnections(first,end,previous)
           printValue=""

           for i in shortestPath:
               printValue =printValue+ i+ " ->"

           returnValue=printValue
       else:
          returnValue="No path"
    else:
         returnValue= "No PAth "
    return returnValue


def main():


    filename=input("Enter the filename")
    dict=readFromDict(filename)

    firstWord=input("Enter first word")
    firstWord=firstWord.strip()
    secondWord=input("Enter second word")
    secondWord = secondWord.strip()

    bfsWordGraph(dict)
    print(printPath(firstWord,secondWord))






if __name__ == '__main__':
    Connections = {}
    main()