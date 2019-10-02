import random
import sys

# generate random integer values
from random import seed


infinity = 1, 2, 3, 2**10000
class State:

    def __init__(self, name=None, matrix=None, fitness=-1):
        self.name = name
        self.matrix = matrix
        self.fitness = fitness
class Problem:

    def __init__(self):
        self.initstate = State()

    def read_input(self):
        pass

    def initialstate(self):
        return self.initstate

    def actions(self, state):
        return []

    def result(self, state, action):
        return None

    def evaluate(self, state):
        return 0



class Node:

    def __init__(self, state=None, parent=None):

        self.state = state

        self.parentNode = parent
class randomHillClimbing:

      def __init__(self,problem):

          self.generate = 0
          self.expand = 0
          self.path = list()
          self.problem=problem
          self.visted=0
          self.end=None

      def basic(self):
          currentnode = Node(state=self.problem.initial_state())

          while True:
                self.expand += 1
                self.path.append(currentnode)
                maxVal=infinity
                maxNode=None

                for node in self.problem.actions(currentnode.state):
                     self.visted+=1
                     next = Node(state=self.problem.result(currentnode.state,node))
                     nextNodeval=self.problem.evaluate(next.state)

                     if nextNodeval > maxVal:
                         maxVal = nextNodeval
                         maxNode=nextNodeval
                currentVal =self.problem.evaluate(currentnode.state)
                if maxVal <=currentVal:
                    self.end=currentnode
                    return currentnode
                currentnode=maxNode

      def randomRestartFunction(self):

          ans=None
          maxTemp = -float(infinity)
          iter =10

          for i in range(iter):

              sol= self.basic()
              if(self.problem.evaluate(sol.state)>maxTemp):
                  ans=sol
                  maxTemp=self.problem.evaluate(ans)

          return ans
def swap(index1,index2,list):

     list[index1],list[index2]=list[index2],list[index1]

     return list
def change(index,op,list):
    list[index]=op
    return list

def evaulate(num1,op,num2):


    if op == "*" :
       return int(num1) * int(num2)
    if op=="+":
        return int(num1)+int(num2)
    if op == "-":
        return int(num1)-int(num2)
    if op == "/":
        if(num2!=0):
           return int(num1) / int(num2)
        else:
            return "nan"



def main():
    numberSet= [3, 3, 7, 3, 3, 4, 6, 7, 3, 5, 8, 2, 7, 6, 4, 4, 1, 2, 2, 8, 3, 2, 3, 0, 2, 3, 3, 7, 7, 3, 2, 9, 0, 2, 0, 4, 3, 0,
      2, 7, 1, 3, 7, 1, 7, 0, 7, 8, 4, 1, 9, 9, 2, 3, 5, 0, 4, 9, 1, 4, 6, 0, 1, 1, 4, 5, 1, 9, 7, 4, 5, 3, 7, 2, 9, 7,
      2, 0, 1, 8, 1, 4, 3, 9, 3, 5, 3, 6, 6, 8, 9, 7, 7, 9, 4, 6, 7, 1, 6, 6]

    op=['+','-','*','/']


    target=3127

    random.shuffle(numberSet)
    random.shuffle(op)

    opList=[]
    for i in range(len(numberSet)):

        opList.append(numberSet[i])
        opList.append(op[random.randint(0,3)])
    sum=evaulate(opList[0],opList[1],opList[2])

    prevMin = sys.float_info.max

    print("before")
    print(opList)
    while(True):


            swapOrChange= random.randrange(1,3)

            print("swap" + str(swapOrChange))

            index2=0
            index1=0
            if(swapOrChange==1):

                index1=random.randrange(0,len(opList)-2,2)
                index2= random.randrange(0,len(opList)-2,2)
                print(index2)
                print(index1)
                print(opList[index1])
                print(opList[index2])
                if(index1==index2):
                    index2=random.randrange(0,len(opList)-2,2)
                opList=swap(index1,index2,opList)
            if(swapOrChange==2):
               opList=change(random.randrange(1,len(opList)-2,2) , op[random.randint(0,3)],opList)

            print("after")
            print(opList[index1])
            print(opList[index2])
            for i in range(3, len(opList) - 1, 2):

                if (i + 1) < len(opList):

                    if sum == "nan":
                        print()
                    if (evaulate(sum, opList[i], opList[i + 1]) == "nan"):
                        print()
                    else:
                        sum = evaulate(sum, opList[i], opList[i + 1])
            sum = abs(sum)
            distanceFromTarget = abs(target - sum)
            print(distanceFromTarget)

            if (distanceFromTarget <= prevMin):
                prevMin = distanceFromTarget
                print("pre" + str(prevMin))
            else:
                break







if __name__ == '__main__':

     main()