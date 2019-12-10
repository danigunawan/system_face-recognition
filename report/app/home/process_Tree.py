import os
import numpy as np
import heapq 
from . import config
import random
import pickle

class Node:
    """ Node in vp-tree """
    def __init__(self):
        self.index = -1 
        self.threshold = 0.0
        self.left = None
        self.right = None

class vptree:
    """
        This is class vp-tree
        It includes the following important parts : build and search
        Complexity:
            Build : O(n*log(n)*(time read file hard disk))
            Search: O(long(n)*time read file hard disk)
    """
    def __init__(self,maximum):
        self.items = np.arange(1,maximum+1) 
        self.current_Ranking = config.Range_find
        self.heap = []
        self.path = config.origin_HOG_npy
    """ 
        Implement distance with Euclid distance 
        between feature and file.npy in data
    """
    def distance(self,a,b):
        a1 = np.load(os.path.join(self.path,str(a)+".npy")) # path
        a2 = np.load(os.path.join(self.path,str(b)+".npy"))
        return np.linalg.norm(a1-a2)
    """ 
        Impelement distance with Euclid distance 
        between feature and data npy
    """    
    def _distance(self,a,b):
        a1 = np.load(os.path.join(self.path,str(a)+".npy"))
        
        return np.linalg.norm(a1-b)
    """
        partition array two part
        In the worst-case, It calls about n times
        In the best case, It calls about log(n) times
    """    
    def _partition(self,first,middle,last,key):
        (self.items[middle] , self.items[last]) = (self.items[last],self.items[middle])
        pivot = self.items[last]
        R = self.distance(pivot,key)
        i = first - 1 
        for j in range(first,last):
            if self.distance(self.items[j],key) < R:
                i= i+1
                (self.items[i],self.items[j])= (self.items[j],self.items[i])
        (self.items[i+1],self.items[last]) = (self.items[last], self.items[i+1])
        return (i+1)

    def build(self,lower,upper):
        if lower == upper:
            return None
        node = Node()
        node.index = lower 
        if upper-lower > 1:
            #middle = round((lower+upper)/2)
            middle = random.randint(lower,upper)
            sp = self._partition(lower+1,middle,upper,self.items[lower])
            
            node.threshold = self.distance(self.items[lower],self.items[sp])

            node.index = lower
            node.left = self.build(lower+1,middle)
            node.right = self.build(middle+1,upper)
        return node 

    def search(self, node = None , target = [] , k = 0 ):
        if node == None:
            return 
        
        dist = self._distance(self.items[node.index],target)

        if dist < self.current_Ranking:
            if len(self.heap) == k:
                self.heap = heapq.nsmallest(len(self.heap)-1,self.heap,key = None)

            heapq.heappush(self.heap,(dist,self.items[node.index]))
            if len(self.heap) == k:
                self.current_Ranking = self.heap[len(self.heap)-1][0] 
        if node.left == None and node.right == None:
            return
        if dist<node.threshold:
            if dist-self.current_Ranking<=node.threshold:
                self.search(node.left,target,k)
            if dist+self.current_Ranking>=node.threshold:
                self.search(node.right,target,k)
        else:
            if dist+self.current_Ranking>=node.threshold:
                self.search(node.right,target,k)
            if dist-self.current_Ranking<=node.threshold:
                self.search(node.left,target,k)