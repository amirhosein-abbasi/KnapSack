

from random import random
import math
from problem import *
from xmlrpc.client import MAXINT


knapsack = Problem()
knapsack.input()


class Algorithms :



    def geneticAlg(self,problem):

        minCost = MAXINT
        bestPath = ""



        population=[]
        populationFitness=[]



        n=8
        m=int(n/2)
        p =0.99
        crossCount = 1
        iteration=5

        bestValue = 0
        population = problem.generateRandomPopulation(n)
        bestNode=population[0]
        worstNode = population[0]
        middleNode = population[0]
        newPopulation = []
        while(1==1):
            print("**********")

            print("the CUR :",population)

            newPopulation=self.generateNewPopulation(problem,population ,m , p , crossCount )

            print("the NEW :", newPopulation)

            validatedNewPopulation= problem.validatePopulation(newPopulation)

            print("the VAL :", validatedNewPopulation)

            mergedPopulation =list(set(validatedNewPopulation)|set(population))

            print("the MER :", mergedPopulation)

            if(len(mergedPopulation) > n):
                population =self.choosePopulation(mergedPopulation,n)
            else :
                population = mergedPopulation


            print("the RES :", population)


            if(problem.fitness(self.setBestNode(problem, population))>bestValue ):
                bestNode = self.setBestNode(problem, population)
                bestValue = problem.fitness(bestNode)


            for node in population:
                if(problem.fitness(node)<problem.fitness(worstNode)):
                    worstNode=node
            population.sort()
            middleNode=population[int(len(population)/2)]
            print("BEST NODE :" ,bestNode,"with the cost :",problem.fitness(bestNode) )
            print("WORS NODE :", worstNode,"with the cost :",problem.fitness(worstNode))
            print("MIDDlLE NODE :", middleNode,"with the cost :",problem.fitness(middleNode))


            if(iteration==0):
               print("we found the best combination of objects with using : ",bestNode,"with the value of : ",problem.fitness(bestNode))
               return
            iteration = iteration - 1


    def generateNewPopulation (self,problem, population,n , p,crossCount ) :

        selectedNodes=[]
        selectedNodes = self.selection(population , n)

        crossoverNodes=[]
        crossoverNodes = self.crossover(selectedNodes,crossCount)


        mutatedNodes=[]
        mutatedNodes=self.mutation(crossoverNodes , p)

        listUnique = []

        for node in mutatedNodes:
            if(node not in listUnique):
                listUnique.append(node)

        validatedNodes = []

        for node in listUnique :
            if(problem.validateNode(node)==1):
                  validatedNodes.append(node)


        newPopulation=validatedNodes
        return newPopulation

    def selection( self , population , n ):

         randList =random.sample(range(0,len(population)), n)

         selectedPopulation=[]


         for i in randList :
             selectedPopulation.append(population[i])

         return selectedPopulation


    def crossover(self, population,crossCount):

        for i in range (0,len(population)-1)  :
            if(i%2 ==0):
                firstParent = population[i]
                secondParent=population[i+1]

                first1 = firstParent[0:crossCount]
                second1 = firstParent[crossCount:len(firstParent)]
                first2 = secondParent[0:crossCount]
                second2 = secondParent[crossCount:len(secondParent)]
                node1 = first1 + second2
                node2 = first2 + second1

                population[i]=node1
                population[i+1]=node2

        return population




    def mutation(self, population , p):

       for k in range(0,len(population)) :
           node=population[k]
           if(p>random.random()):
               i = random.randint(0,len(node)-1)
               if(int(node[i])== 0):
                   str = node[0:i] + '1' + node[i+1:len(node)]
                   node=str
               else :
                   str = node[0:i] + '0' + node[i+1:len(node)]
                   node = str
           population[k] = node

       return population

    def setBestNode(self,problem,population):

        allValues=problem.populationFitness(population)
        maxList =allValues.index(max(allValues))

        return population[maxList]

    def choosePopulation(self, population, k):

        result = []
        smpl = random.sample(range(0, len(population)), k)
        for i in smpl:
            result.append(population[i])
        return result


alg=Algorithms()
alg.geneticAlg(knapsack)
