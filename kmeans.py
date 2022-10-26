import numpy as np
import matplotlib.pyplot as plt

class kmeans:

    def __init__(self, data: list, k : int = 2):
        self.k = k
        self.data = data
        self.centroids = self.first_centroids1()

    def first_centroids1(self):

        centroids = self.data[np.random.randint(self.data.shape[0], size=self.k), :].copy()

        return centroids

    def first_centroids2(self):
        centroids = list()
        
        for i in range(self.k):
            c = [np.random.randint(min,max) for min,max in zip(self.data.min(axis=0),self.data.max(axis=0))]
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
            self.recalculate_centroids(clusters)
        
        self.view_clusters(clusters)

        return clusters

    def view_clusters(self,clusters):
        #Tratar o dcit antes do plot
        #Seaborn
        color = [(np.random.random(),np.random.random(),np.random.random(),1.0) for i in range(self.k)]
        plt.figure()
        
        for i in range(self.k):
            if len(clusters[i]) > 0:
                coord_x = np.array(clusters[i])[:,0]
                coord_y = np.array(clusters[i])[:,1]
                plt.plot(coord_x,coord_y,"o",color=color[i])

        plt.xscale
        plt.savefig("clusters.png")
        plt.show()