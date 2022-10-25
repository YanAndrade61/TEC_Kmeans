import pandas as pd
import numpy as np

class kmeans:

    def __init__(self, data: list, k : int = 2):
        self.k = k
        self.data = data
        self.centroids = self.first_centroids()

    def first_centroids(self):
        centroids = list()
        for i in range(self.k):
            c = [np.random.randint(p) for p in self.data.max(axis=0)]
            centroids.append(c)
        return centroids
    
    def recalculate_centroids(self,clusters):
        for i in range(self.k):
            self.centroids[i] = np.mean(clusters[i],axis=0)

    def generate_clusters(self):

        clusters = {x: list() for x in range(self.k)}

        for p in self.data:
            groupe = 0
            dist = np.inf
            for i,c in enumerate(self.centroids):
                if dist > np.linalg.norm(c-p):
                    dist = np.linalg.norm(c-p)
                    groupe= i
            clusters[groupe].append(p)

        return clusters
    
    def simulate(self,it):

        for i in range(it):
            clusters = self.generate_clusters()
            self.recalculate_centroids()
        
        return clusters

    def view_clusters(self):
        
        cores = [(np.random.random(),np.random.random(),np.random.random(),1.0) for i in range(2)]
        
        for i in self.k:

            pass

def main():
    data = pd.read_csv("s02.txt")
    data = data.to_numpy()
    print("oi",data)