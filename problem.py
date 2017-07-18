#!/usr/bin/python
import string
import math
import random
from xmlrpc.client import MAXINT




class Node :
    objects = ""
    visited = 0


class Problem :
    objNum = 0
    weights = []
    values = []
    capacity = 0

    def input(self) :


        self.objNum = int(input('Enter number of objects: '))


        x = input('Enter the weights of objects : ')
        self.weights=x.split()
        self.weights = list(map(int,self.weights))


        z =input('Enter the values of objects : ')
        self.values = z.split()
        self.values = list(map(int, self.values))

        self.capacity = int(input('Enter the capacity of the knapsack: '))

    def fitness(self, node):


        nodeValue=0

        for i in range (0,self.objNum) :
            if(int(node[i])==1):
                nodeValue+=self.values[i]

        return nodeValue



    def generateRandomPopulation(self , n):

        allPopulation=[]

        for i in range(int(math.pow(2, self.objNum))):
            allPopulation.append(('{0:0' + str(self.objNum) + 'b}').format(i))

        print("all population  : ", allPopulation)

        randomPopulation=[]

        i=0
        while i < n  :
            smpl = random.randint(0,len(allPopulation)-1)
            if(self.validateNode(allPopulation[smpl]) == 1):
                randomPopulation.append(allPopulation[smpl])
                i=i+1

        print("random population :", randomPopulation)
        return randomPopulation

    def validatePopulation(self,population):

        resultList=[]

        for i in range (0,len(population)):
            if(self.validateNode(population[i])==1):
                resultList.append(population[i])

        return resultList

    def populationFitness(self,population):
        listFitness=[]

        for node in population :
            listFitness.append(self.fitness(node))

        return listFitness

    def validateNode(self , node):

        nodeWeight = 0

        for i in range (0,len(node)) :
            if(node[i]==str(1)) :
                nodeWeight = nodeWeight + self.weights[i]
        if(nodeWeight > self.capacity):
            return 0
        else :
            return 1




