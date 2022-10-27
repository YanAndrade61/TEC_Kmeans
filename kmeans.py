from dataclasses import replace
import string
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

class Kmeans:

    def __init__(self, data: list, k : int = 2):
        self.data = data
        self.k = k

    def recalculate_centroids(self,clusters):
        
        centroids = [np.mean(clusters[i],axis=0) for i in range(self.k)]
        
        return centroids

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
    
    def simulate(self, first_centroids : str = "random_point", it: int = 1000, error_stop: float = 0.001):

        if first_centroids == "random_point":
            self.centroids = self.data[np.random.randint(self.data.shape[0], size=self.k), :].copy()
        elif first_centroids == "random_vector":
            self.centroids = [np.random.randint(min,max) for min,max in zip(self.data.min(axis=0),self.data.max(axis=0))]
        else:
            print("Please enter a valid strategie: random_point or random_vector")
            return

        for i in range(it):
            stop = 0
            clusters = self.generate_clusters()
            centroids = self.recalculate_centroids(clusters)
    
            for c_new,c_past in zip(centroids,self.centroids):
                if np.linalg.norm(c_new-c_past) < error_stop: stop += 1

            if stop == self.k: break

            self.centroids = centroids

        self.clusters = clusters

        return clusters

    def view_clusters(self,path_save : str):
        colors = cm.rainbow(np.linspace(0, 1, 5))
        plt.figure()
        for i in range(self.k):

            if len(self.clusters[i]) > 0:
                coord_x = np.array(self.clusters[i])[:,0]
                coord_y = np.array(self.clusters[i])[:,1]
                plt.plot(coord_x,coord_y,"o",color=colors[i])
                plt.plot(self.centroids[i][0],self.centroids[i][1],"o",markersize=10,
                        markeredgecolor="black",color=colors[i],label=f"Centroid {i}")
        
        plt.title(f"Kmeans with {self.k} clusters")
        plt.legend()
        plt.savefig(path_save)
        plt.show()